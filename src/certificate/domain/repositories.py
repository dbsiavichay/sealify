from abc import ABC, abstractmethod
from typing import List

from .models import Certificate


class CertificateRepository(ABC):
    @abstractmethod
    def save(self, certificate: Certificate) -> Certificate:
        pass

    @abstractmethod
    def list(self) -> List[Certificate]:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Certificate:
        pass

    @abstractmethod
    def find_by_serial_number(self, serial_number: int) -> Certificate:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass
