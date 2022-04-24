from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
class Config:
  DEBUG = False
  TESTING = False

class DevelopmentConfig(Config):
  DEBUG = True
  DEVELOPMENT = True
