import logging
from importlib_resources import files

from tomli import load
from datetime import datetime


class ConfigService:
    @property
    def config_dict(self):
        return self._config_dict

    @property
    def log_filename(self):
        return self._log_filename

    @property
    def log_level(self):
        return self._log_level

    @property
    def log_format(self):
        return self._log_format

    @property
    def log_dte_fmt(self):
        return self._log_dte_fmt

    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._set_log_filename()
        self._set_config()
        self._set_logging()

    def _set_config(self):
        config_file = files("py-dsa").joinpath("config.toml")
        with config_file.open("rb") as file:
            config_data = load(file)

        self._config_dict = config_data

    def _set_log_filename(self):
        date_start = datetime.now().strftime("%d_%m_%y_%T").replace(":", "_")
        filename = f"py_dsa_{date_start}.log"
        self._log_filename = filename

    def _set_logging(self):
        log_config = self._config_dict["logging"]
        logger = self._logger
        self._log_level = log_config["LOG_LEVEL"]
        self._log_format = log_config["LOG_FORMAT"]
        self._log_dte_fmt = log_config["LOG_DATE_FORMAT"]

        logger.info(f"Log level {self._log_level}")
        logger.info(f"Log format {self._log_format}")
        logger.info(f"Log date format {self._log_dte_fmt}")

        if self._log_level == "debug":
            log_level = logging.DEBUG
        elif self._log_level == "error":
            log_level = logging.ERROR
        elif self._log_level == "critical":
            log_level = logging.CRITICAL
        else:
            log_level = logging.INFO

        log_file = files("py-dsa").joinpath(self._log_filename).__str__()

        handlers = [
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]

        logging.basicConfig(level=log_level, format=self._log_format, datefmt=self._log_dte_fmt, handlers=handlers)

        logger.info("Logging configured")


