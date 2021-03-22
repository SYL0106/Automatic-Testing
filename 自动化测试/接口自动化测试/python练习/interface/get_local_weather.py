"""
get local weather

"""
from common.send_method import SendMethod
from common.get_keyword import GetKeyword

class GetlocalWeather:
    def __init__(self,method="get"):
        self.url = "https://tianqiapi.com/api"
        self.method = method

    def get_local_weather(self,params):
        '''
        请求获取本地天气接口
        :return:response
        '''
        response = SendMethod.send_method(method=self.method,url=self.url,params=params)
        return response

    def get_city(self,response):
        """
        获取城市名称
        :return:city
        """
        city =  GetKeyword.get_value_by_keyword(response,"city")
        return city

if __name__ == '__main__':
    params = {"appid": "38992497",
              "appsecret": "pfpm5ZnJ"
              }
    getW =GetlocalWeather("get")
    print(getW.get_local_weather(params)) # 单接口测试
    print(getW.get_city(getW.get_local_weather(params))) # 业务关联测试
