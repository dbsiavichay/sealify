from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def debug(self, message: str) -> None:
        pass

    @abstractmethod
    def info(self, message: str) -> None:
        pass

    @abstractmethod
    def warning(self, message: str) -> None:
        pass

    @abstractmethod
    def error(self, message: str) -> None:
        pass

    @abstractmethod
    def critical(self, message: str) -> None:
        pass

    @abstractmethod
    def exception(self, message: str) -> None:
        pass
