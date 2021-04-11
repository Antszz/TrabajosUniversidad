import requests
import json
url = 'https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjE1OTQ3MTQyLCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D'
headers = {
    # ':authority': 'www.facebook.com',
    # ':path': 'POST',
    # ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-419,es;q=0.9',
    'cache-control': 'max-age=0',
    'content-length': '303',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'sb=X2VRYOmFA1N3VRS8_3WO3ksy; datr=YGVRYOYzJPFmubzwlDL5B9xd; locale=es_LA; fr=1n905XXThb92M5Fud.AWVLyFIn6fzYtI9baQ3fZNhMqOI.BgUWVf._-.AAA.0.0.BgUWWG.AWVtvXLZgP4; wd=933x937',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/?stype=lo&jlou=AfdYlutPisJJrGW5g23j53aGWIfrngzXRs2-o8yJdk-JP_rx_RXAJbGLXaOtYgt9GsOyitbw5Ss2dsLGVXCmFg5qz8q9VvE7fKBjo9UUIyul-w&smuh=24359&lh=Ac-0NurQR8_s_JFpQXg',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
}
data_login = {
    'jazoest': '2890',
    'lsd': 'AVq4LT8gRu8',
    'email': 'fabrisan333@gmail.com',
    'login_source': 'comet_headerless_login',
    'next': '',
    'encpass': '#PWD_BROWSER:5:1615947157:AehQANpkQsS8KCI3VbtJzptFb0DlYCMYhU9/GOnscU8xJesbckPc9+jcwyeprMflwDv1f1KK5ZkHTHDGbBmvzMPcyvUJmuyiktotgMG8iioo+P+h8sY6sOu+r/YUXvpJJOp4JsaSQ3YupvG5V6nt'
}
session = requests.session()
login_request = session.post(url, headers=headers, data=data_login)
if login_request.status_code == 200:
    print('SIIIIIIIIII')
url = 'https://www.facebook.com/RihanaMS'
test_page = session.get(url)
if login_request.status_code == 200:
    print('Siiiim')
    # f = open('holamundo.html','w')
    mensaje = login_request.text
    print(mensaje)
    # f.write(mensaje)
    # f.close()