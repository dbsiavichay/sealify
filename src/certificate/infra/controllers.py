from fastapi import HTTPException, UploadFile

from src.certificate.app.services import CertificateService


class CertificateController:
    def __init__(self, service: CertificateService) -> None:
        self.service = service

    async def create(self, certificate: UploadFile, password: str):
        try:
            certificate_bytes = await certificate.read()
            if not certificate.filename.endswith(".p12"):
                raise HTTPException(
                    status_code=400, detail="El archivo debe tener extensión .p12"
                )

            return self.service.create(certificate_bytes, password)
        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Error al procesar el archivo: {str(e)}"
            )
