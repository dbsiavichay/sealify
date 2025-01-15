import uuid
from typing import List

from src.certificate.domain.models import Certificate
from src.certificate.domain.repositories import CertificateRepository
from src.core.app.exceptions import ResourceNotFoundException
from src.core.infra.aws_clients import AWSDynamoDBClient


class CertificateRepositoryDynamoDB(CertificateRepository):
    def __init__(self, db_client: AWSDynamoDBClient):
        self.db_client = db_client

    def save(self, certificate: Certificate) -> None:
        self.db_client.put_item(certificate.dict())

    def list(self) -> List[Certificate]:
        response = self.db_client.scan_items()
        count = response.get("Count", 0)

        if count == 0:
            return []

        return [Certificate(**item) for item in response.get("Items")]

    def find_by_id(self, id: uuid.UUID) -> Certificate:
        response = self.db_client.get_item({"id": str(id)})
        item = response.get("Item")

        if not item:
            raise ResourceNotFoundException(
                f"CERTIFICATE_REPOSITORY :: CERTIFICATE_NOT_FOUND :: ID {id}"
            )

        return Certificate(**item)

    def find_by_serial_number(self, serial_number: int) -> Certificate:
        response = self.db_client.query(
            {"serial_number": serial_number}, index_name="SerialNumberIndex"
        )
        count = response.get("Count", 0)
        item = response.get("Items")[0] if count > 0 else None
        return Certificate(**item) if item else None

    def delete(self, id: str) -> None:
        self.db_client.delete_item({"id": str(id)})
