import os
import logging

logger = logging.Logger(__name__)


REDIS_HOST = os.environ.get("REDIS_HOST")
if REDIS_HOST is None:
    logger.warning(msg="Using default value for Redis Host")
    REDIS_HOST = "localhost"

REDIS_PORT = os.environ.get("REDIS_PORT")
if REDIS_PORT is None:
    logger.warning(msg="Using default value for Redis Port")
    REDIS_PORT = 6379
