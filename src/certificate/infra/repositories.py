import uuid

from src.certificate.domain.models import Certificate
from src.certificate.domain.repositories import CertificateRepository
from src.core.infra.aws_clients import AWSDynamoDBClient


class CertificateRepositoryDynamoDB(CertificateRepository):
    def __init__(self, db_client: AWSDynamoDBClient):
        self.db_client = db_client

    def find_by_id(self, id: uuid.UUID) -> Certificate:
        item = self.db_client.get_item({"id": str(id)})
        return Certificate(**item)

    def find_by_serial_number(self, serial_number: int) -> Certificate:
        response = self.db_client.query(
            {"serial_number": serial_number}, index_name="SerialNumberIndex"
        )
        count = response.get("Count", 0)
        item = response.get("Items")[0] if count > 0 else None
        return Certificate(**item) if item else None

    def save(self, certificate: Certificate) -> None:
        self.db_client.put_item(certificate.dict())
