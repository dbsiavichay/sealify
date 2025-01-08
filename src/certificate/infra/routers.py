from typing import Annotated

from fastapi import APIRouter, File, Form, UploadFile

from src import certificate_controller
from src.certificate.app.schemas import CertificateSchema

router = APIRouter()


@router.post("", response_model=CertificateSchema)
async def create_certificate(
    certificate: Annotated[UploadFile, File(...)], password: Annotated[str, Form(...)]
):
    return await certificate_controller.create(certificate, password)
