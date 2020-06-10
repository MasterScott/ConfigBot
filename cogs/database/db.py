from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.sqlite import TEXT,INTEGER, TEXT

Base = declarative_base()

class Configs(Base):
	__tablename__ = 'configs'
	__table_args__={'sqlite_autoincrement':True}
	count = Column(INTEGER, primary_key=True, nullable=False)
	name = Column(TEXT)
	captcha = Column(TEXT)
	capture = Column(TEXT)
	proxies = Column(TEXT)
	author = Column(TEXT)
	uploaded_by = Column(TEXT)
	wordlist1 = Column(TEXT)
	wordlist2 = Column(TEXT)
	Location = Column(TEXT)