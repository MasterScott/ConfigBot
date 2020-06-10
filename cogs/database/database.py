from sqlalchemy import engine, create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, Configs

	# ----------------------- #
engine = create_engine('sqlite:///Configs.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

if not engine.dialect.has_table(engine, 'event'):
	Base.metadata.create_all(engine)