import logging


logger = logging.getLogger("app_logger")

fileHandler = logging.FileHandler("app_log.log")
consoleHandler = logging.StreamHandler()

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        fileHandler,
        consoleHandler
    ]
)
