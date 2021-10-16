from icecream import ic
from test import ABC
from logging import getLogger, StreamHandler, Formatter, DEBUG, INFO

logger = getLogger("log_test")
handler = StreamHandler()
handler_format = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(handler_format)
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False


if __name__ == "__main__":
    ic()
    # ic.disable()
    abc = ABC()

    abc.func1()
    ic()
    logger.debug("debug")
    logger.info("Info")
