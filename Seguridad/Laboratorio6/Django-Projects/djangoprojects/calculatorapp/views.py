from django.shortcuts import render
from django.http import HttpResponse
from calculatorapp.hashes.md4 import MD4
from calculatorapp.hashes.sha1 import SHA1
from calculatorapp.hashes.md5 import MD5
from calculatorapp.hashes.sha256 import SHA256
from calculatorapp.hashes.hmac import HMAC
# Create your views here.


def index(request):
    return render(request,'index.html')

def submitquery(request):
    q = request.GET['query']
    h = request.GET['hash']
    try:
        ans = ""
        if h == "1":
            ans = MD4(q.encode()).hexdigest()
        elif h == "2":
            ans = MD5.hash(q)
        elif h == "3":
            ans = SHA1(q.encode()).hexdigest()
        elif h == "4":
            ans = SHA256(q).hexdigest()
        elif h == "5":
            k = request.GET['key']
            t = request.GET['type-hash']
            ans = HMAC(k.encode(), q.encode(), t).hexdigest()
        mydictionary = {
            "h": h,
            "q" : q,
            "ans" : ans,
            "error" : False,
            "result" : True
        }
        return render(request,'index.html',context=mydictionary)
    except ValueError as e:
        print(e)
        mydictionary = {
            "error" : True,
            "result" : False

        }
        return render(request,'index.html',context=mydictionary)
