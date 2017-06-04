import threading
import json
import threading
import time
from time import strftime

from requests import get

from app.model.Weather import Weather
from config import *
from app import session
from app.model.Mise import Mise

end = False

def get_mise(second=1000):
    global end
    if end:
        return

    res = get('http://openapi.seoul.go.kr:8088/' +
              mise_servicekey + '/' +
              'json' + '/' +
              'DailyAverageAirQuality' + '/' +
              '1/5' + '/' +
              '20170604' + '/' +
              '중구'
              )
    # print('res', res)
    dicts = json.loads(res.text)
    print('dicts', dicts)

    if not dicts['DailyAverageAirQuality']['row'] == '':
        # session.delete(i for i in session.query(Weather).all())
        session.query(Weather).delete()

        for i in dicts['DailyAverageAirQuality']['row']:
            # print(i)
            w = Mise(
                MSRDT_DE=i['MSRDT_DE'],
                SO2=i['SO2'],
                NO2=i['NO2'],
                PM25=i['PM25'],
                CO=i['CO'],
                PM10=i['PM10'],
                O3=i['O3'],
                MSRSTE_NM=i['MSRSTE_NM'],
            )

            session.add(w)
            session.commit()

            # if i['category'] == 'LGT':
            #     print(i)
    else:
        print('not yet')

    threading.Timer(second, get_mise, [second]).start()
