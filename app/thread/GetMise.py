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
    while (True):
        global end
        if end:
            return

        # print(strftime("%Y%m%d%H%M", time.localtime()))
        res = get('http://openapi.seoul.go.kr:8088/' +
                  mise_servicekey + '/' +
                  'json' + '/' +
                  'TimeAverageAirQuality' + '/' +
                  '1/5' + '/' +
                  strftime("%Y%m%d", time.localtime()) + '/' +
                  '중구'
                  )
        # print('res', res)
        dicts = json.loads(res.text)
        # print('dicts', dicts)

        if 'TimeAverageAirQuality' in dicts:
            # session.delete(i for i in session.query(Weather).all())
            session.query(Mise).delete()

            for i in dicts['TimeAverageAirQuality']['row']:
                # print(i)
                w = Mise(
                    MSRDT_DE=i['MSRDT'],
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
            print('get mise')

        else:
            print('not yet mise')

        time.sleep(second)

            # threading.Timer(second, get_mise, [second]).start()
