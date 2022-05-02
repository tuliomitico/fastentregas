import os

from dotenv import load_dotenv
from sqlalchemy import *
from sqlalchemy.orm import ( scoped_session, sessionmaker)
from sqlalchemy.ext.declarative import declarative_base

from config import BASE_DIR
from utils.validation import is_in_sentence

load_dotenv(BASE_DIR.parent / '.env')

DATABASE_PREFIX = os.getenv('DATABASE_PREFIX')
DATABASE_URL = os.getenv('DATABASE_URL')

url = DATABASE_PREFIX + DATABASE_URL
if not is_in_sentence(DATABASE_URL,':'):
  url = DATABASE_PREFIX + str(BASE_DIR) + "/" + DATABASE_URL

# TODO: Create a engine equal to Alembic
engine = create_engine(
  url,
  convert_unicode = True,
  connect_args = {'check_same_thread': False}
)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()
