from typing import Annotated, List

from fastapi import APIRouter, File, Form, UploadFile

from src import certificate_controller
from src.certificate.app.schemas import CertificateResponseSchema
from src.core.app.schemas import ResourceDeletedSuccessfullyResponseSchema

router = APIRouter()


@router.post("", response_model=CertificateResponseSchema)
async def create_certificate(
    certificate: Annotated[UploadFile, File(...)], password: Annotated[str, Form(...)]
):
    return await certificate_controller.create(certificate, password)


@router.get("", response_model=List[CertificateResponseSchema])
async def list_certificates():
    return await certificate_controller.list()


@router.get("/{id}", response_model=CertificateResponseSchema)
async def retrieve_certificate(id: str):
    return await certificate_controller.retrieve(id)


@router.delete("/{id}", response_model=ResourceDeletedSuccessfullyResponseSchema)
async def delete_certificate(id: str):
    return await certificate_controller.delete(id)
