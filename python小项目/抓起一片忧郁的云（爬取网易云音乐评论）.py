from Crypto.Cipher import AES
from base64 import b64encode
import requests
import json
url='https://music.163.com/weapi/comment/resource/comments/get?csrf_token='
data={
    'csrf_token': "",
    'cursor': "-1",
    'offset': "0",
    'orderType': "1",
    'pageNo': "1",
    'pageSize': "20",
    'rid': "R_SO_4_1965138482",
    'threadId': "R_SO_4_1965138482"
}

e='010001'
f='00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g='0CoJUm6Qyw8W8jud'
i="3SNphXB03bCeqjOu"

'''    function   
    a(a)
    {
        var
    d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
    for (d = 0; a > d; d += 1)
    e = Math.random() * b.length,
        e = Math.floor(e),
            c += b.charAt(e);
    return c
    }
    function
    b(a, b)
    {
    var
    c = CryptoJS.enc.Utf8.parse(b)
    , d = CryptoJS.enc.Utf8.parse("0102030405060708")
    , e = CryptoJS.enc.Utf8.parse(a)
    , f = CryptoJS.AES.encrypt(e, c, {
        iv: d,
        mode: CryptoJS.mode.CBC
    });
    return f.toString()
    }
    function
    c(a, b, c)
    {
    var
    d, e;
    return setMaxDigits(131),
    d = new
    RSAKeyPair(b, "", c),
    e = encryptedString(d, a)
    }
    function
    d(d, e, f, g)
    {
    var
    h = {}
    , i = a(16);
    return h.encText = b(d, g),
    h.encText = b(h.encText, i),
    h.encSecKey = c(i, e, f),
    h
    }
    function
    e(a, b, d, e)
    {
    var
    f = {};
    return f.encText = c(a + e, b, d),
    f
    }
'''
def get_encSecKey():
    return "1c4e26b4e5c9c35b08df086e296f5a8fb0f75c61f50e17e7e460a240cc25ba57d68f1e0d14b396243b7b62b02d1af44378797c1614445d37b2f32eee6c897f75cf0fedbec78c1448428402f74376f0f684c70c51c84ff31963a13544182e210e84c50963a54ae2e578dc01ccfa12d15d89ce743a0a365227ac5dc240c8c56cbb"

def to_16(data):
    pad=16-len(data)%16
    data+=chr(pad)*pad
    return data

def get_params(data):
    first=enc_params(data,g)
    second=enc_params(first,i)
    return second

def enc_params(data,key):
    iv='0102030405060708'
    data=to_16(data)
    aes=AES.new(key=key.encode('utf-8'),IV=iv.encode('utf-8'),mode=AES.MODE_CBC)
    bs=aes.encrypt(data.encode('utf-8'))
    return str(b64encode(bs),'utf-8')

resp=requests.post(url,data={
    'params':get_params((json.dumps(data))),
    "encSecKey":get_encSecKey()
})
# print(resp.json())
def parse_return():
    data = json.loads(resp.content.decode('utf-8'))#将返回的值格式化为json
    hotcomm = data['data']['hotComments']
    print('--------------------------------------------------------------热门评论-------------------------------------------------------------------------------')
    if hotcomm:
        for hotitem in hotcomm:
             hotdata = {
                '用户名': hotitem['user']['nickname'],
                'content': hotitem['content'].replace('\r', ' '),
                '赞':hotitem['likedCount']
                }
             print(hotdata)
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
    else:
        print('没有热门评论')
        print('------------------------------------------------------------------------------------------------------------------------------------------------------------')
    comm = data['data']['comments']
    for item in comm:
        data = {
            '用户名': item['user']['nickname'],
            'content': item['content'].replace('\r', ' '),
            '赞': item['likedCount']
        }
        print(data)
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------')
parse_return()