from logging import getLogger
from logging import StreamHandler
from logging import Formatter
from logging import DEBUG, INFO
from icecream import ic

logger = getLogger("logging_sample")
handler = StreamHandler()
handler_format = Formatter(
    "%(asctime)s - %(name)s - %(funcName)s - %(lineno)s - %(levelname)s - %(message)s"
)
handler.setFormatter(handler_format)
logger.propagate = False
logger.addHandler(handler)


class ABC:
    def __init__(self):
        logger.debug("init")

    def func1(self):
        logger.debug("func1")
        ic()


if __name__ == "__main__":
    handler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    abc = ABC()
    abc.func1()
