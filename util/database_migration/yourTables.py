from sqlalchemy import Column, Integer, String, Text, Date, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    _umd5 = Column(String(255))
    username = Column(String(255))
    employeenum = Column(String(255))
    email = Column(String(255))
    phonenum = Column(String(255))
    password = Column(String(255), nullable=False)
    registered_on = Column(Date, nullable=False)
    admin = Column(Integer, nullable=False)
    last_modified = Column(Date)
    department = Column(String(255), nullable=False)
    uuid = Column(String(32))
    nickname = Column(String(255))
    openid = Column(String(127))
    unionid = Column(String(127))

class VersionUpdateLog(Base):
    __tablename__ = 'version_update_log'

    id = Column(Integer, primary_key=True)
    cuid = Column(String(255), nullable=False)
    version = Column(String(255), nullable=False)
    log_info = Column(Text)
    tag = Column(String(255))
    update_time = Column(Date)

AllClassName = [User, VersionUpdateLog]

oldEngine = 'mysql+pymysql://root:pd123456@106.15.60.110:10306/para_design'
newEngine = 'mysql+pymysql://root:123456@localhost:3306/para_design'