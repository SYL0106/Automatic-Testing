"""
get_keyword.py
    1. 在接口返回值中，通过关键字获取对应的值0
    2. 通过库”jsonpath“实现，需要安装并学习使用该库:
        jsonpath.jsonpath(obj,jsonpath表达式)：jsonpath表达式--$..关键字
"""
import jsonpath

data = {
    "cityid": "101120101",
    "city": "济南",
    "cityEn": "jinan",
    "country": "中国",
    "countryEn": "China",
    "update_time": "2021-03-21 21:46:46",
    "data": [
        {
            "day": "21日（星期日）",
            "date": "2021-03-21",
            "week": "星期日",
            "wea": "晴",
            "wea_img": "qing",
            "wea_day": "晴",
            "wea_day_img": "qing",
            "wea_night": "晴",
            "wea_night_img": "qing",
            "tem": "11℃",
            "tem1": "11℃",
            "tem2": "3℃",
            "humidity": "25%",
            "visibility": "30km",
            "pressure": "1006",
            "win": [
                "西北风",
                "南风"
            ],
            "win_speed": "3-4级",
            "win_meter": "小于12km/h",
            "sunrise": "06:13",
            "sunset": "18:23",
            "air": "55",
            "air_level": "良",
            "air_tips": "空气好，可以外出活动，除极少数对污染物特别敏感的人群以外，对公众没有危害！",
            "alarm": {
                "alarm_type": "",
                "alarm_level": "",
                "alarm_content": ""
            },
            "hours": [
                {
                    "hours": "22时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "6",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "23时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "5",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "00时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "5",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "01时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "5",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "02时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "4",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "03时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "4",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "04时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "3",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "05时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "3",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "06时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "4",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "07时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "5",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "08时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "5",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "09时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "7",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "10时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "10",
                    "win": "微风",
                    "win_speed": "8-9级"
                },
                {
                    "hours": "11时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "13",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "12时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "13时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "8-9级"
                },
                {
                    "hours": "14时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "8-9级"
                },
                {
                    "hours": "15时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "17",
                    "win": "微风",
                    "win_speed": "8-9级"
                },
                {
                    "hours": "16时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "17时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "18时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "15",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "19时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "20时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "21时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "7-8级"
                }
            ],
            "index": [
                {
                    "title": "紫外线指数",
                    "level": "很强",
                    "desc": "紫外线辐射极强，建议涂擦SPF20以上、PA  的防晒护肤品，尽量避免暴露于日光下。"
                },
                {
                    "title": "减肥指数",
                    "level": "一颗星",
                    "desc": "春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。"
                },
                {
                    "title": "血糖指数",
                    "level": "不易波动",
                    "desc": "天气条件好，血糖不易波动，可适时进行户外锻炼。"
                },
                {
                    "title": "穿衣指数",
                    "level": "较冷",
                    "desc": "建议着厚外套加毛衣等服装。年老体弱者宜着大衣、呢外套加羊毛衫。"
                },
                {
                    "title": "洗车指数",
                    "level": "较不宜",
                    "desc": "较不宜洗车，未来一天无雨，风力较大，如果执意擦洗汽车，要做好蒙上污垢的心理准备。"
                },
                {
                    "title": "空气污染扩散指数",
                    "level": "良",
                    "desc": "气象条件有利于空气污染物稀释、扩散和清除。"
                }
            ]
        },
        {
            "day": "22日（星期一）",
            "date": "2021-03-22",
            "week": "星期一",
            "wea": "晴",
            "wea_img": "qing",
            "wea_day": "晴",
            "wea_day_img": "qing",
            "wea_night": "晴",
            "wea_night_img": "qing",
            "tem": "17℃",
            "tem1": "17℃",
            "tem2": "6℃",
            "humidity": "",
            "visibility": "",
            "pressure": "",
            "win": [
                "南风",
                "南风"
            ],
            "win_speed": "3-4级",
            "win_meter": "",
            "sunrise": "06:12",
            "sunset": "18:24",
            "air": "56",
            "air_level": "良",
            "air_tips": "空气好，可以外出活动，除极少数对污染物特别敏感的人群以外，对公众没有危害！",
            "alarm": {
                "alarm_type": "",
                "alarm_level": "",
                "alarm_content": ""
            },
            "hours": [
                {
                    "hours": "08时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "5",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "09时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "7",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "10时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "10",
                    "win": "微风",
                    "win_speed": "8-9级"
                },
                {
                    "hours": "11时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "13",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "12时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "13时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "8-9级"
                },
                {
                    "hours": "14时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "8-9级"
                },
                {
                    "hours": "15时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "17",
                    "win": "微风",
                    "win_speed": "8-9级"
                },
                {
                    "hours": "16时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "17时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "18时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "15",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "19时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "20时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "21时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "22时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "23时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "6-7级"
                }
            ],
            "index": [
                {
                    "title": "紫外线指数",
                    "level": "很强",
                    "desc": "紫外线辐射极强，建议涂擦SPF20以上、PA  的防晒护肤品，尽量避免暴露于日光下。"
                },
                {
                    "title": "减肥指数",
                    "level": "一颗星",
                    "desc": "春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。"
                },
                {
                    "title": "血糖指数",
                    "level": "易波动",
                    "desc": "气温多变，血糖易波动，注意监测血糖变化。"
                },
                {
                    "title": "穿衣指数",
                    "level": "较冷",
                    "desc": "建议着厚外套加毛衣等服装。年老体弱者宜着大衣、呢外套加羊毛衫。"
                },
                {
                    "title": "洗车指数",
                    "level": "较不宜",
                    "desc": "较不宜洗车，未来一天无雨，风力较大，如果执意擦洗汽车，要做好蒙上污垢的心理准备。"
                },
                {
                    "title": "空气污染扩散指数",
                    "level": "良",
                    "desc": "气象条件有利于空气污染物稀释、扩散和清除。"
                }
            ]
        },
        {
            "day": "23日（星期二）",
            "date": "2021-03-23",
            "week": "星期二",
            "wea": "晴",
            "wea_img": "qing",
            "wea_day": "晴",
            "wea_day_img": "qing",
            "wea_night": "晴",
            "wea_night_img": "qing",
            "tem": "21℃",
            "tem1": "21℃",
            "tem2": "12℃",
            "humidity": "",
            "visibility": "",
            "pressure": "",
            "win": [
                "南风",
                "南风"
            ],
            "win_speed": "4-5级",
            "win_meter": "",
            "sunrise": "06:10",
            "sunset": "18:25",
            "air": "75",
            "air_level": "良",
            "air_tips": "空气好，可以外出活动，除极少数对污染物特别敏感的人群以外，对公众没有危害！",
            "alarm": {
                "alarm_type": "",
                "alarm_level": "",
                "alarm_content": ""
            },
            "hours": [
                {
                    "hours": "00时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "13",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "01时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "12",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "02时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "11",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "03时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "12",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "04时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "12",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "05时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "13",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "06时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "07时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "08时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "15",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "09时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "15",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "10时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "11时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "16",
                    "win": "东北风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "12时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "18",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "13时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "19",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "14时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "20",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "15时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "21",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "16时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "20",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "17时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "20",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "18时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "19",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "19时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "19",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "20时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "19",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "21时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "17",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "22时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "23时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "15",
                    "win": "东北风",
                    "win_speed": "6-7级"
                }
            ],
            "index": [
                {
                    "title": "紫外线指数",
                    "level": "很强",
                    "desc": "紫外线辐射极强，建议涂擦SPF20以上、PA  的防晒护肤品，尽量避免暴露于日光下。"
                },
                {
                    "title": "减肥指数",
                    "level": "一颗星",
                    "desc": "春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。"
                },
                {
                    "title": "血糖指数",
                    "level": "易波动",
                    "desc": "气温多变，血糖易波动，注意监测血糖变化。"
                },
                {
                    "title": "穿衣指数",
                    "level": "较舒适",
                    "desc": "建议着薄外套、开衫牛仔衫裤等服装。年老体弱者应适当添加衣物，宜着夹克衫、薄毛衣等。"
                },
                {
                    "title": "洗车指数",
                    "level": "较不宜",
                    "desc": "较不宜洗车，未来一天无雨，风力较大，如果执意擦洗汽车，要做好蒙上污垢的心理准备。"
                },
                {
                    "title": "空气污染扩散指数",
                    "level": "良",
                    "desc": "气象条件有利于空气污染物稀释、扩散和清除。"
                }
            ]
        },
        {
            "day": "24日（星期三）",
            "date": "2021-03-24",
            "week": "星期三",
            "wea": "晴",
            "wea_img": "qing",
            "wea_day": "晴",
            "wea_day_img": "qing",
            "wea_night": "晴",
            "wea_night_img": "qing",
            "tem": "21℃",
            "tem1": "21℃",
            "tem2": "9℃",
            "humidity": "",
            "visibility": "",
            "pressure": "",
            "win": [
                "北风",
                "南风"
            ],
            "win_speed": "3-4级",
            "win_meter": "",
            "sunrise": "06:09",
            "sunset": "18:26",
            "air": "70",
            "air_level": "良",
            "air_tips": "空气好，可以外出活动，除极少数对污染物特别敏感的人群以外，对公众没有危害！",
            "alarm": {
                "alarm_type": "",
                "alarm_level": "",
                "alarm_content": ""
            },
            "hours": [
                {
                    "hours": "00时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "01时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "14",
                    "win": "东北风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "02时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "13",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "03时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "13",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "04时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "12",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "05时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "12",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "06时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "12",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "07时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "12",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "08时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "09时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "10时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "17",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "11时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "17",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "12时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "18",
                    "win": "微风",
                    "win_speed": "4-5级"
                },
                {
                    "hours": "13时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "19",
                    "win": "微风",
                    "win_speed": "3-4级"
                },
                {
                    "hours": "14时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "20",
                    "win": "微风",
                    "win_speed": "10-11级"
                },
                {
                    "hours": "15时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "20",
                    "win": "微风",
                    "win_speed": "3-4级"
                },
                {
                    "hours": "16时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "20",
                    "win": "微风",
                    "win_speed": "3-4级"
                },
                {
                    "hours": "17时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "20",
                    "win": "微风",
                    "win_speed": "3-4级"
                },
                {
                    "hours": "18时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "18",
                    "win": "微风",
                    "win_speed": "3-4级"
                },
                {
                    "hours": "19时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "17",
                    "win": "微风",
                    "win_speed": "4-5级"
                },
                {
                    "hours": "20时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "3-4级"
                },
                {
                    "hours": "23时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "12",
                    "win": "微风",
                    "win_speed": "4-5级"
                }
            ],
            "index": [
                {
                    "title": "紫外线指数",
                    "level": "很强",
                    "desc": "紫外线辐射极强，建议涂擦SPF20以上、PA  的防晒护肤品，尽量避免暴露于日光下。"
                },
                {
                    "title": "减肥指数",
                    "level": "一颗星",
                    "desc": "春天不减肥，夏天徒伤悲。风虽有点大，室内可健身。"
                },
                {
                    "title": "血糖指数",
                    "level": "较易波动",
                    "desc": "血糖较易波动，注意监测。"
                },
                {
                    "title": "穿衣指数",
                    "level": "较舒适",
                    "desc": "建议着薄外套、开衫牛仔衫裤等服装。年老体弱者应适当添加衣物，宜着夹克衫、薄毛衣等。"
                },
                {
                    "title": "洗车指数",
                    "level": "较不宜",
                    "desc": "较不宜洗车，未来一天无雨，风力较大，如果执意擦洗汽车，要做好蒙上污垢的心理准备。"
                },
                {
                    "title": "空气污染扩散指数",
                    "level": "良",
                    "desc": "气象条件有利于空气污染物稀释、扩散和清除。"
                }
            ]
        },
        {
            "day": "25日（星期四）",
            "date": "2021-03-25",
            "week": "星期四",
            "wea": "晴转阴",
            "wea_img": "yin",
            "wea_day": "晴",
            "wea_day_img": "qing",
            "wea_night": "阴",
            "wea_night_img": "yin",
            "tem": "22℃",
            "tem1": "22℃",
            "tem2": "14℃",
            "humidity": "",
            "visibility": "",
            "pressure": "",
            "win": [
                "南风",
                "南风"
            ],
            "win_speed": "<3级",
            "win_meter": "",
            "sunrise": "06:07",
            "sunset": "18:27",
            "air": "24",
            "air_level": "优",
            "air_tips": "空气很好，可以外出活动，呼吸新鲜空气，拥抱大自然！",
            "alarm": {
                "alarm_type": "",
                "alarm_level": "",
                "alarm_content": ""
            },
            "hours": [
                {
                    "hours": "02时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "9",
                    "win": "微风",
                    "win_speed": "4-5级"
                },
                {
                    "hours": "05时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "11",
                    "win": "微风",
                    "win_speed": "5-6级"
                },
                {
                    "hours": "08时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "13",
                    "win": "微风",
                    "win_speed": "5-6级"
                },
                {
                    "hours": "11时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "17",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "14时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "21",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "17时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "19",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "20时",
                    "wea": "晴",
                    "wea_img": "qing",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "23时",
                    "wea": "多云",
                    "wea_img": "yun",
                    "tem": "15",
                    "win": "微风",
                    "win_speed": "6-7级"
                }
            ],
            "index": [
                {
                    "title": "紫外线指数",
                    "level": "很强",
                    "desc": "紫外线辐射极强，建议涂擦SPF20以上、PA  的防晒护肤品，尽量避免暴露于日光下。"
                },
                {
                    "title": "减肥指数",
                    "level": "五颗星",
                    "desc": "春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。"
                },
                {
                    "title": "血糖指数",
                    "level": "易波动",
                    "desc": "血糖易波动，注意监测。"
                },
                {
                    "title": "穿衣指数",
                    "level": "较舒适",
                    "desc": "建议着薄外套、开衫牛仔衫裤等服装。年老体弱者应适当添加衣物，宜着夹克衫、薄毛衣等。"
                },
                {
                    "title": "洗车指数",
                    "level": "较适宜",
                    "desc": "较适宜洗车，未来一天无雨，风力较小，擦洗一新的汽车至少能保持一天。"
                },
                {
                    "title": "空气污染扩散指数",
                    "level": "中",
                    "desc": "气象条件对空气污染物稀释、扩散和清除无明显影响。"
                }
            ]
        },
        {
            "day": "26日（星期五）",
            "date": "2021-03-26",
            "week": "星期五",
            "wea": "小雨",
            "wea_img": "yu",
            "wea_day": "小雨",
            "wea_day_img": "yu",
            "wea_night": "小雨",
            "wea_night_img": "yu",
            "tem": "19℃",
            "tem1": "19℃",
            "tem2": "11℃",
            "humidity": "",
            "visibility": "",
            "pressure": "",
            "win": [
                "南风",
                "北风"
            ],
            "win_speed": "<3级",
            "win_meter": "",
            "sunrise": "06:06",
            "sunset": "18:28",
            "air": "",
            "air_level": "优",
            "air_tips": "空气很好，可以外出活动，呼吸新鲜空气，拥抱大自然！",
            "alarm": {
                "alarm_type": "",
                "alarm_level": "",
                "alarm_content": ""
            },
            "hours": [
                {
                    "hours": "02时",
                    "wea": "阴",
                    "wea_img": "yin",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "05时",
                    "wea": "阴",
                    "wea_img": "yin",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "5-6级"
                },
                {
                    "hours": "08时",
                    "wea": "阴",
                    "wea_img": "yin",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "5-6级"
                },
                {
                    "hours": "11时",
                    "wea": "阴",
                    "wea_img": "yin",
                    "tem": "19",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "14时",
                    "wea": "阴",
                    "wea_img": "yin",
                    "tem": "18",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "17时",
                    "wea": "小雨",
                    "wea_img": "yu",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "5-6级"
                },
                {
                    "hours": "20时",
                    "wea": "小雨",
                    "wea_img": "yu",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "5-6级"
                },
                {
                    "hours": "23时",
                    "wea": "小雨",
                    "wea_img": "yu",
                    "tem": "13",
                    "win": "微风",
                    "win_speed": "6-7级"
                }
            ],
            "index": [
                {
                    "title": "紫外线指数",
                    "level": "最弱",
                    "desc": "属弱紫外线辐射天气，无需特别防护。若长期在户外，建议涂擦SPF在8-12之间的防晒护肤品。"
                },
                {
                    "title": "减肥指数",
                    "level": "一颗星",
                    "desc": "春天快来了，雨天坚持室内运动吧。"
                },
                {
                    "title": "血糖指数",
                    "level": "较易波动",
                    "desc": "血糖较易波动，注意监测。"
                },
                {
                    "title": "穿衣指数",
                    "level": "较舒适",
                    "desc": "建议着薄外套、开衫牛仔衫裤等服装。年老体弱者应适当添加衣物，宜着夹克衫、薄毛衣等。"
                },
                {
                    "title": "洗车指数",
                    "level": "不宜",
                    "desc": "不宜洗车，未来24小时内有雨，如果在此期间洗车，雨水和路上的泥水可能会再次弄脏您的爱车。"
                },
                {
                    "title": "空气污染扩散指数",
                    "level": "良",
                    "desc": "气象条件有利于空气污染物稀释、扩散和清除。"
                }
            ]
        },
        {
            "day": "27日（星期六）",
            "date": "2021-03-27",
            "week": "星期六",
            "wea": "阴转晴",
            "wea_img": "yin",
            "wea_day": "阴",
            "wea_day_img": "yin",
            "wea_night": "晴",
            "wea_night_img": "qing",
            "tem": "18℃",
            "tem1": "18℃",
            "tem2": "11℃",
            "humidity": "",
            "visibility": "",
            "pressure": "",
            "win": [
                "北风",
                "北风"
            ],
            "win_speed": "<3级",
            "win_meter": "",
            "sunrise": "06:04",
            "sunset": "18:29",
            "air": "",
            "air_level": "优",
            "air_tips": "空气很好，可以外出活动，呼吸新鲜空气，拥抱大自然！",
            "alarm": {
                "alarm_type": "",
                "alarm_level": "",
                "alarm_content": ""
            },
            "hours": [
                {
                    "hours": "02时",
                    "wea": "小雨",
                    "wea_img": "yu",
                    "tem": "11",
                    "win": "微风",
                    "win_speed": "9-10级"
                },
                {
                    "hours": "05时",
                    "wea": "小雨",
                    "wea_img": "yu",
                    "tem": "11",
                    "win": "微风",
                    "win_speed": "6-7级"
                },
                {
                    "hours": "08时",
                    "wea": "小雨",
                    "wea_img": "yu",
                    "tem": "12",
                    "win": "微风",
                    "win_speed": "8-9级"
                },
                {
                    "hours": "11时",
                    "wea": "阴",
                    "wea_img": "yin",
                    "tem": "15",
                    "win": "微风",
                    "win_speed": "9-10级"
                },
                {
                    "hours": "14时",
                    "wea": "多云",
                    "wea_img": "yun",
                    "tem": "17",
                    "win": "微风",
                    "win_speed": "8-9级"
                },
                {
                    "hours": "17时",
                    "wea": "阴",
                    "wea_img": "yin",
                    "tem": "18",
                    "win": "微风",
                    "win_speed": "7-8级"
                },
                {
                    "hours": "20时",
                    "wea": "阴",
                    "wea_img": "yin",
                    "tem": "16",
                    "win": "微风",
                    "win_speed": "5-6级"
                },
                {
                    "hours": "23时",
                    "wea": "多云",
                    "wea_img": "yun",
                    "tem": "14",
                    "win": "微风",
                    "win_speed": "6-7级"
                }
            ],
            "index": [
                {
                    "title": "紫外线指数",
                    "level": "最弱",
                    "desc": "属弱紫外线辐射天气，无需特别防护。若长期在户外，建议涂擦SPF在8-12之间的防晒护肤品。"
                },
                {
                    "title": "减肥指数",
                    "level": "五颗星",
                    "desc": "春天不减肥，夏天徒伤悲。天气较舒适，快去运动吧。"
                },
                {
                    "title": "血糖指数",
                    "level": "较易波动",
                    "desc": "血糖较易波动，注意监测。"
                },
                {
                    "title": "穿衣指数",
                    "level": "较冷",
                    "desc": "建议着厚外套加毛衣等服装。年老体弱者宜着大衣、呢外套加羊毛衫。"
                },
                {
                    "title": "洗车指数",
                    "level": "较不宜",
                    "desc": "较不宜洗车，路面少量积水，如果执意擦洗汽车，要做好溅上泥水的心理准备。"
                },
                {
                    "title": "空气污染扩散指数",
                    "level": "较差",
                    "desc": "气象条件较不利于空气污染物稀释、扩散和清除。"
                }
            ]
        }
    ]
}

# print(jsonpath.jsonpath(data,"$..city")[0])
# print(jsonpath.jsonpath(data,"$..win")[0])
# print(jsonpath.jsonpath(data,"$..wea"))
# print(data["data"][0]["win"][0])


class GetKeyword:
    @staticmethod
    def get_value_by_keyword(data,keyword):
        """
                        get_value_by_keyword:通过关键字获取对应值
                            :param data: 数据源 - 接口返回值
                            :param keyword: 关键字
                            :param return:
                """
        return jsonpath.jsonpath(data, f"$..{keyword}")[0]

if __name__ == '__main__':
    print(GetKeyword.get_value_by_keyword(data,"city"))
