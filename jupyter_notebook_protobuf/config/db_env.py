import os
import logging

logger = logging.Logger(__name__)


DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL is None:
    logger.warning(msg="Using default value for Database Url")
    DATABASE_URL = "sqlite:///foo.db"
