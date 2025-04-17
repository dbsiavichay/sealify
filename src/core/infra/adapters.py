from typing import Optional

import structlog

from src.core.domain.ports import Logger


class StructLogger(Logger):
    _instance: Optional["StructLogger"] = None
    _logger = None

    def __new__(cls, level: str = "INFO", env: str = "local") -> "StructLogger":
        if cls._instance is None:
            cls._instance = super(StructLogger, cls).__new__(cls)
            # Configuración básica de structlog
            cls._logger = structlog.get_logger()
            # Configuración del procesador para formatear los logs
            structlog.configure(
                processors=[
                    structlog.processors.add_log_level,
                    structlog.processors.TimeStamper(fmt="iso"),
                    structlog.dev.ConsoleRenderer(colors=True)
                    if env == "local"
                    else structlog.processors.JSONRenderer(),
                ],
                wrapper_class=structlog.make_filtering_bound_logger(level),
                context_class=dict,
                logger_factory=structlog.PrintLoggerFactory(),
                cache_logger_on_first_use=True,
            )
        return cls._instance

    def debug(self, message: str) -> None:
        self._logger.debug(message)

    def info(self, message: str) -> None:
        self._logger.info(message)

    def warning(self, message: str) -> None:
        self._logger.warning(message)

    def error(self, message: str) -> None:
        self._logger.error(message)

    def critical(self, message: str) -> None:
        self._logger.critical(message)

    def exception(self, message: str) -> None:
        self._logger.exception(message)
