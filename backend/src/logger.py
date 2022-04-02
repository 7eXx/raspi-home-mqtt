import logging
from logging import StreamHandler, Formatter, Logger

class LoggerSingleton:

    logger = None

    @staticmethod
    def get_or_create_logger() -> Logger:
        if LoggerSingleton.__check_existence_logger():
            return LoggerSingleton.logger
        else:
            return LoggerSingleton.create_logger()

    @staticmethod
    def __check_existence_logger() -> bool:
        return LoggerSingleton.logger is not None

    @staticmethod
    def create_logger() -> Logger:
        LoggerSingleton.logger = logging.getLogger("allarme PI")
        LoggerSingleton.logger.setLevel(logging.DEBUG)

        ch = LoggerSingleton.__create_stream_handler('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        LoggerSingleton.logger.addHandler(ch)

        return LoggerSingleton.logger

    @staticmethod
    def __create_stream_handler(str_format) -> StreamHandler:
        # create console handler and set level to debug
        ch = StreamHandler()
        ch.setLevel(logging.DEBUG)

        ## formattazione del logger
        formatter = Formatter(str_format)
        ## associazione del formato
        ch.setFormatter(formatter)

        return ch

    @staticmethod
    def info(msg) -> None:
        LoggerSingleton.get_or_create_logger().info(msg)

    @staticmethod
    def warning(msg) -> None:
        LoggerSingleton.get_or_create_logger().warning(msg)

    @staticmethod
    def debug(msg) -> None:
        LoggerSingleton.get_or_create_logger().debug(msg)

    @staticmethod
    def exception(msg) -> None:
        LoggerSingleton.get_or_create_logger().exception(msg)
