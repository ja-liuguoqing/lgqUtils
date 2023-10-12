#数据库迁移工具：需要手动将类写完
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from yourTables.py import Base, AllClassName, oldEngine, newEngine

old_engine = create_engine(oldEngine)
old_Session = sessionmaker(bind=old_engine)
old_session = old_Session()

new_engine = create_engine(newEngine)
new_Session = sessionmaker(bind=new_engine)
new_session = new_Session()

Base.metadata.create_all(new_engine)#创表，若表存在则不创（包括不更新表结构）

for table in AllClassName:#数据迁移
    records = old_session.query(table).all()
    for record in records:
        new_session.merge(record)#使用 merge 会主动检测、更新

new_session.commit()

old_session.close()
new_session.close()