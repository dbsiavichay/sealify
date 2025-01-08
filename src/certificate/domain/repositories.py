from abc import ABC, abstractmethod

from .models import Certificate


class CertificateRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: int) -> Certificate:
        pass

    @abstractmethod
    def exists_serial_number(self, serial_number: str) -> bool:
        pass
