import logging

from starlette.config import Config

log = logging.getLogger(__name__)


config = Config(".env")

LOG_LEVEL = config("LOG_LEVEL", default=logging.WARNING)
DEBUG = config("DEBUG", cast=bool, default=False)
SQLALCHEMY_DATABASE_URL = config("SQLALCHEMY_DATABASE_URL")
