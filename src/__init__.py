import boto3
from cryptography.fernet import Fernet

from .certificate.app.services import CertificateService
from .certificate.app.usecases import ProcessCertificateFileUseCase
from .certificate.infra.controllers import CertificateController
from .certificate.infra.repositories import CertificateRepositoryDynamoDB
from .config import config
from .core.app.utils import CipherUtil
from .core.infra.aws_clients import AWSDynamoDBClient
from .sealer.app.services import SealerService
from .sealer.app.usecases import SealerXMLUseCase
from .sealer.infra.controllers import SealerController

dynamodb = boto3.resource(
    "dynamodb",
    region_name=config.AWS_REGION_NAME,
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
    endpoint_url=config.AWS_ENDPOINT_URL,
)

# Cipher
fernet_cipher = Fernet(config.FERNET_KEY.encode("utf-8"))
cipher_util = CipherUtil(fernet_cipher)

# Tables
certificate_table = dynamodb.Table("certificates")

# AWS DynamoDB Clients
certificate_client = AWSDynamoDBClient(certificate_table)

# Repositories
certificate_repository = CertificateRepositoryDynamoDB(certificate_client, cipher_util)

# Usecases
process_certificate_file_usecase = ProcessCertificateFileUseCase()
seal_xml_usecase = SealerXMLUseCase()

# Services
certificate_service = CertificateService(
    certificate_repository, process_certificate_file_usecase
)
sealer_service = SealerService(certificate_repository, seal_xml_usecase)

# Controllers
certificate_controller = CertificateController(certificate_service)
sealer_controller = SealerController(sealer_service)
