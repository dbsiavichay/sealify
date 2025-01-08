from src.certificate.domain.models import Certificate
from src.certificate.domain.repositories import CertificateRepository
from src.core.domain.usecases import UseCase


class CertificateService:
    def __init__(
        self, repository: CertificateRepository, process_certificate_usecase: UseCase
    ) -> None:
        self.repository = repository
        self.process_certificate_usecase = process_certificate_usecase

    def create(self, cert_bytes: bytes, password: str) -> Certificate:
        certificate = self.process_certificate_usecase.execute(cert_bytes, password)
        db_certificate = self.repository.find_by_serial_number(
            certificate.serial_number
        )

        if db_certificate:
            return db_certificate

        self.repository.save(certificate)
        return certificate
