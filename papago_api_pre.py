import os
import ssl
import json
import urllib.request

def translate(txt, nmt_id, nmt_pw):
    """번역"""
    encText = urllib.parse.quote(txt)
    data = "source=en&target=ko&text=" + encText
    
    url = "https://openapi.naver.com/v1/papago/n2mt"
    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", nmt_id)
    request.add_header("X-Naver-Client-Secret", nmt_pw)
    res_ssl = ssl._create_unverified_context()
    response = urllib.request.urlopen(request, data=data.encode("utf-8"), context=res_ssl)
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read()
        
        res = json.loads(response_body.decode('utf-8'))
        return(res['message']['result']['translatedText'])

    else:
        return("Error Code:" + rescode) 