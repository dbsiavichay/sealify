from fastapi import UploadFile

from src.certificate.app.exceptions import CertificateInvalidExtensionException
from src.certificate.app.services import CertificateService


class CertificateController:
    def __init__(self, service: CertificateService) -> None:
        self.service = service

    async def create(self, certificate: UploadFile, password: str):
        if not certificate.filename.endswith(".p12"):
            raise CertificateInvalidExtensionException()

        certificate_bytes = await certificate.read()

        return self.service.create(certificate_bytes, password)

    async def list(self):
        return self.service.list()

    async def retrieve(self, id: str):
        return self.service.retrieve(id)

    async def delete(self, id: str):
        return self.service.delete(id)
