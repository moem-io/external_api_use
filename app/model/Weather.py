from app import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.mysql import TIMESTAMP
import datetime
from sqlalchemy.sql.expression import text


class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    baseDate = Column(Integer)
    baseTime = Column(Integer)
    category = Column(String(20))
    nx = Column(Integer)
    ny = Column(Integer)
    obsrValue = Column(Integer)
    created_date = Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow,
        server_default=text('CURRENT_TIMESTAMP')
    )

    def __init__(self, baseDate, baseTime, category, nx, ny, obsrValue):
        self.baseDate = baseDate
        self.baseTime = baseTime
        self.category = category
        self.nx = nx
        self.ny = ny
        self.obsrValue = obsrValue

    def __repr__(self):
        return "<Weather('%s', '%s', '%s')>" % (self.baseDate, self.baseTime, self.category)
