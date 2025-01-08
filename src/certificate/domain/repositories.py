from abc import ABC, abstractmethod

from .models import Certificate


class CertificateRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: int) -> Certificate:
        pass

    @abstractmethod
    def find_by_serial_number(self, serial_number: int) -> Certificate:
        pass

    @abstractmethod
    def save(self, certificate: Certificate) -> Certificate:
        pass
