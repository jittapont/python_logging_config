import json
import logging
from logging.config import dictConfig

from src.mod import do_something
from src.mod2 import do_something2

with open("logging.json", "r") as f:
    logging_config = json.load(f)

dictConfig(logging_config)

logger = logging.getLogger(__name__)

do_something()
do_something2()

logger.debug("Main Debug")
logger.info("Main Info")
logger.error("Main Error")
logger.exception("Main Exception")
