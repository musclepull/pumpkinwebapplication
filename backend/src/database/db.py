from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DB_SERVER = 'fullstack-test-db'
DB_PORT = '3306'
DB_NAME = 'pumpkin'
DB_USER = 'pumpkin'
DB_PASS = 'pumpkin'

Engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_SERVER}:{DB_PORT}/{DB_NAME}'
                       f'?charset=utf8mb4&binary_prefix=true')

Session = scoped_session(sessionmaker(bind=Engine))
