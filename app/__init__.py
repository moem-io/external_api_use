from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import *

engine = create_engine('mysql+pymysql://{0}:{1}@{2}/{3}?charset=utf8'.format(id_db, ps_db, host_db, name_db))
Base = declarative_base()
Session = sessionmaker(bind=engine)

from app.model import *

Base.metadata.create_all(engine) # table 생성
session = Session()

