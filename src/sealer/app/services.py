from typing import Tuple

from src.certificate.domain.repositories import CertificateRepository
from src.core.domain.usecases import UseCase
from src.sealer.app.schemas import SealInvoiceSchema


class SealerService:
    def __init__(
        self, certificate_repository: CertificateRepository, usecase_xml: UseCase
    ):
        self.certificate_repository = certificate_repository
        self.usecase_xml = usecase_xml

    def retrieve_certificate(self, certificate_id: str) -> Tuple[str, str]:
        certificate = self.certificate_repository.find_by_id(certificate_id)
        return certificate.cert, certificate.key

    def seal_invoice(self, certificate_id: str, input: SealInvoiceSchema) -> str:
        cert, key = self.retrieve_certificate(certificate_id)

        return self.usecase_xml.execute(cert, key, input.invoice_xml)
