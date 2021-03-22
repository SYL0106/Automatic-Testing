
import unittest
from common.get_keyword import GetKeyword
from interface.get_local_weather import GetlocalWeather

class TestGetWeather(unittest.TestCase):

    def test_get_localweather(self):
        """测试正常情况下获取本地天气"""
        params = {"appid": "38992497",
                  "appsecret": "pfpm5ZnJ"
                  }
        self.local_weather = GetlocalWeather("get")
        response = self.local_weather.get_local_weather(params)
        # 获取天气信息中的城市名称
        city = GetKeyword.get_value_by_keyword(response,"city")
        self.assertEqual(city,"济南")

if __name__ == '__main__':
    unittest.main()
