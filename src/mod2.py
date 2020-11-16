import logging

logger = logging.getLogger(__name__)


def do_something2():
    logger.debug("do_something2 Debug")
    logger.info("do_something2 Info")
    logger.error("do_something2 Error")
    logger.exception("do_something2 Exception")
