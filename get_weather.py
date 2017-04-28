import time
from time import strftime
from requests import get, post
import json
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy import Sequence, and_, or_

from config import *

import threading

engine = create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.format(id_db, ps_db, host_db, name_db))
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    baseDate = Column(Integer)
    baseTime = Column(Integer)
    category = Column(String(20))
    nx = Column(Integer)
    ny = Column(Integer)
    obsrValue = Column(Integer)

    def __init__(self, baseDate, baseTime, category, nx, ny, obsrValue):
        self.baseDate = baseDate
        self.baseTime = baseTime
        self.category = category
        self.nx = nx
        self.ny = ny
        self.obsrValue = obsrValue

    def __repr__(self):
        return "<Weather('%s', '%s', '%s')>" % (self.baseDate, self.baseTime, self.category)

Base.metadata.create_all(engine) # table 생성
session = Session()


print('app_run!!')
# print(time.gmtime())
print(strftime("%Y%m%d", time.localtime()))
print(strftime("%H%M", time.localtime()))

end = False


def exec(second=1000):
    print('exec')
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
    dict = json.loads(res.text)
    # print(type(dict))
    # print(dict)
    # print(type(dict['response']['body']['items']['item']))

    # for i in session.query(Weather).all():
    #     print('ho'+i.category)

    if not dict['response']['body']['items'] == '':
        # session.delete(i for i in session.query(Weather).all())
        session.query(Weather).delete()
        for i in dict['response']['body']['items']['item']:
            # print(i)
            w = Weather(i['baseDate'], i['baseTime'], i['category'], i['nx'], i['ny'], i['obsrValue'])

            session.add(w)
            session.commit()

            # if i['category'] == 'LGT':
            #     print(i)
    else:
        print('not yet')

    threading.Timer(second, exec, [second]).start()

exec(1200.0)