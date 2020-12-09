import struct
from functools import reduce


class SHA1:
    """An implementation of the SHA-1 hash algorithm."""

    width = 32
    mask = 0xFFFFFFFF

    h = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]

    def __init__(self, msg=None):
        """:param ByteString msg: The message to be hashed."""
        if msg is None:
            msg = b""

        self.msg = msg

        # Pre-processing: Total length is a multiple of 512 bits.
        ml = len(msg) * 8
        msg += b"\x80"
        msg += b"\x00" * (-(len(msg) + 8) % 64)
        msg += struct.pack(">Q", ml)

        # Process the message in successive 512-bit chunks.
        chunks = [msg[i : i + 64] for i in range(0, len(msg), 64)]
        self._process(chunks)

    def __repr__(self):
        if self.msg:
            return f"{self.__class__.__name__}({self.msg:s})"
        return f"{self.__class__.__name__}()"

    def __str__(self):
        return self.hexdigest()

    def __eq__(self, other):
        return self.h == other.h

    def int(self):
        """:return: The final hash value as an `int`."""
        return reduce(lambda x, y: (x << SHA1.width) | y, self.h)

    def bytes(self):
        """:return: The final hash value as a `bytes` object."""
        return struct.pack(">5L", *self.h)

    def hexbytes(self):
        """:return: The final hash value as hexbytes."""
        return self.hexdigest().encode()

    def hexdigest(self):
        """:return: The final hash value as a hexstring."""
        return "".join(f"{value:08x}" for value in self.h)

    def _process(self, chunks):
        for chunk in chunks:
            w = list(struct.unpack(">16L", chunk))

            # Extend the sixteen 32-bit words into eighty 32-bit words.
            for i in range(16, 80):
                value = w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16]
                w.append(SHA1.lrot(value, 1))

            # Initialize hash value for this chunk.
            a, b, c, d, e = self.h

            # Main loop.
            for i in range(len(w)):
                if i < 20:
                    f, k = d ^ (b & (c ^ d)), 0x5A827999
                elif i < 40:
                    f, k = b ^ c ^ d, 0x6ED9EBA1
                elif i < 60:
                    f, k = (b & c) | (d & (b | c)), 0x8F1BBCDC
                else:
                    f, k = b ^ c ^ d, 0xCA62C1D6

                temp = (SHA1.lrot(a, 5) + f + e + k + w[i]) & SHA1.mask
                e, d, c, b, a = d, c, SHA1.lrot(b, 30), a, temp

            # Add this chunk's hash to result so far.
            c_hash = [a, b, c, d, e]
            self.h = [((v + n) & SHA1.mask) for v, n in zip(self.h, c_hash)]

    @staticmethod
    def lrot(value, n):
        lbits, rbits = (value << n) & SHA1.mask, value >> (SHA1.width - n)
        return lbits | rbits