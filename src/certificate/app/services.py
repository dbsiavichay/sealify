# from src.certificate.domain.repositories import CertificateRepository

from src.certificate.app.schemas import CertificateSchema
from src.core.domain.usecases import UseCase


class CertificateService:
    # def __init__(self, repository: CertificateRepository) -> None:
    #    self.repository = repository

    def __init__(self, process_certificate_usecase: UseCase) -> None:
        self.process_certificate_usecase = process_certificate_usecase

    def create(self, cert_bytes: bytes, password: str) -> CertificateSchema:
        certificate = self.process_certificate_usecase.execute(cert_bytes, password)

        # signature_exists = (
        #    self.signature_service.signature_repository.exists_serial_number(
        #        signature_entity.serial_number
        #    )
        # )

        # user_data = UserSchema(**user_create_data.model_dump())
        # user = User(**json.loads(user_data.model_dump_json()))
        # self.user_repository.create(user)
        return certificate
