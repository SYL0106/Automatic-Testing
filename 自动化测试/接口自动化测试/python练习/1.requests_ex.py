##目的：
# 1. requests的使用：查询（返回值-header、status-code、text、content）


import requests 
import json

url = "https://tianqiapi.com/api"
#?appid=38992497&appsecret=pfpm5ZnJ"
data = {"appid":38992497,"appsecret":"pfpm5ZnJ"}
resp = requests.get(url=url,params=data)
# print(resp.text)
# print(resp.status_code)
# print(resp.headers)
# print("________________")
# print(resp.content)


# json.dumps(): 将python字典对转化为json字符串
# json。loads(): 将json转化为 python字典格式
# print(json.dumps(resp.json(),indent=2,ensure_ascii=False))

# 2. 返回值格式化


print(json.dumps(resp.json(),indent=2,ensure_ascii=False))

# 2.post请求

# 2.1 语法 request.post(url,data=None,json=None，files=None)   
    #  1.xxx-form-urlencode（字典格式）
    #     data = {
    #     "name":"tom",
    #     "ID":"666"
    # }
    #  2.json格式的请求参数 ：requests.post(url=url,json=data);requests中会默认将header中的content_type转换为Json
    #    如果要指定header，添加请请求头，参考
    # headers = {"content_type":"application/json",
    #            "User-Agent":""
    #           }
    # requests.post(url=url,json=data,header=header)


#resp = requests.post(url=url,data=data)
