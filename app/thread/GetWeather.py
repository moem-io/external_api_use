import json
import threading
import time
from time import strftime

from requests import get

from app.model.Weather import Weather
from config import *
from app import session

end = False


def get_weather(second=1000):
    # print('exec')
    global end
    if end:
        return

    payload = {
        'ServiceKey': weather_servicekey,
        'base_date': strftime("%Y%m%d", time.localtime()),
        'base_time': strftime("%H%M", time.localtime()),
        # 'base_time': '1940',
        'nx': '60',
        'ny': '127',
        '_type': 'json'
    }
    res = get('http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastGrib', params=payload)
    # print('res', res)
    dicts = json.loads(res.text)
    # print(type(dict))
    # print(dicts)
    # print(type(dict['response']['body']['items']['item']))

    # for i in session.query(Weather).all():
    #     print('ho'+i.category)

    if not dicts['response']['body']['items'] == '':
        # session.delete(i for i in session.query(Weather).all())
        session.query(Weather).delete()
        for i in dicts['response']['body']['items']['item']:
            # print(i)
            w = Weather(i['baseDate'], i['baseTime'], i['category'], i['nx'], i['ny'], i['obsrValue'])

            session.add(w)
            session.commit()

            # if i['category'] == 'LGT':
            #     print(i)
    else:
        print('not yet')

    threading.Timer(second, get_weather, [second]).start()
