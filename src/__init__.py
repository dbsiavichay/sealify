import boto3

from .certificate.app.services import CertificateService
from .certificate.app.usecases import ProcessCertificateFileUseCase
from .certificate.infra.controllers import CertificateController
from .config import config

dynamodb = boto3.resource(
    "dynamodb",
    region_name=config.AWS_REGION_NAME,
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
    endpoint_url=config.AWS_ENDPOINT_URL,
)

# Tables
user_table = dynamodb.Table("users")

# Usecases
process_certificate_file_usecase = ProcessCertificateFileUseCase()

# Services
certificate_service = CertificateService(process_certificate_file_usecase)

# Controllers
certificate_controller = CertificateController(certificate_service)
