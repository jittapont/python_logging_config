import logging

logger = logging.getLogger(__name__)


def do_something():
    logger.debug("do_something Debug")
    logger.info("do_something Info")
    logger.error("do_something Error")
    logger.exception("do_something Exception")
