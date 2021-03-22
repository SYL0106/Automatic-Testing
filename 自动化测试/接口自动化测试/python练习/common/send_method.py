"""
send_method.py
    1. 封装接口请求方式
    2. 封装要素：method、url、params、response
    3. 实例返回济南当日天气
"""

import requests
class SendMethod:
    @staticmethod
    def send_method(method,url,params=None,data=None):
        if method == "get" or method == "delete":
            response =  requests.request(method=method, url=url, params=params)
        elif method =="post" or method =="put":
            response = requests.request(method=method, url=url, json=data)
        else:
            print("请求方式有误")
            response = None
        if method =="delete":
            return response.status_code
        else:
            return response.json()

if __name__ == '__main__':
    url = "https://tianqiapi.com/api"
    method = "get"
    params = {"appid":"38992497",
              "appsecret":"pfpm5ZnJ"
              }
    res = SendMethod.send_method(method=method,url=url,params=params)
    print(res)
