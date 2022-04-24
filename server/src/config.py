import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
class Config:
  DEBUG = False
  DEVELOPMENT = False
  TESTING = False
  SECRET_KEY = os.getenv('SECRET_KEY')

class ProductionConfig(Config):
  pass
class DevelopmentConfig(Config):
  DEBUG = True
  DEVELOPMENT = True

class TestingConfig(Config):
  TESTING = True
