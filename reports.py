#!/usr/bin/env python

from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, Date
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Reports(Base):
    __tablename__ = 'reports'

    id = Column('id', Integer, primary_key=True)
    created_by = Column('created_by', String)
    report_name = Column('report_name', String)
    report_type = Column('report_type', String)
    frequency = Column('frequency', String)
    rolename = Column('rolename', String)
    hosts = Column('hosts', String)
    created_date = Column('created_date', Date)
    expiry_date = Column('expiry_date', Date)
    status = Column('status', String)

    def __init__(self, id, created_by, report_name, report_type, frequency, rolename, hosts, created_date, expiry_date, status):
        self.id = id
        self.created_by = created_by
        self.report_name = report_name
        self.report_type = report_type
        self.frequency = frequency
        self.rolename = rolename
        self.hosts = hosts
        self.created_date = created_date
        self.expiry_date = expiry_date
        self.status = status

engine = create_engine('sqlite:////home/nbkydek/utils/utils.db', echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

