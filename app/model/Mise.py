from app import Base
from sqlalchemy import Column, Float, String, Integer


class Mise(Base):
    __tablename__ = 'mise'

    id = Column(Integer, primary_key=True)
    MSRDT_DE = Column(String(20))  # 측정 일시
    SO2 = Column(Float)  # 아황산가서ppm
    NO2 = Column(Float)  # 이산화질소농도(ppm)
    PM25 = Column(Float)  # 초미세먼지(㎍/㎥)
    MSRSTE_NM = Column(String(20))  # 측정소명
    CO = Column(Float)  # 일산화탄소농도(ppm)
    PM10 = Column(Float)  # 미세먼지(㎍/㎥)
    O3 = Column(Float)  # 오존농도(ppm)

    def __init__(self, MSRDT_DE, SO2, NO2, PM25, MSRSTE_NM, CO, PM10, O3):
        self.MSRDT_DE = MSRDT_DE
        self.SO2 = SO2
        self.NO2 = NO2
        self.PM25 = PM25
        self.MSRSTE_NM = MSRSTE_NM
        self.CO = CO
        self.PM10 = PM10
        self.O3 = O3

    def __repr__(self):
        return "<Mise('%s', '%s', '%s')>" % (self.MSRDT_DE, self.PM10, self.PM25)
