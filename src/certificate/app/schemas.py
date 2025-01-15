import uuid
from datetime import datetime

from pydantic import BaseModel, Field


class CertificateResponseSchema(BaseModel):
    id: uuid.UUID
    subject_name: str = Field(serialization_alias="subjectName")
    serial_number: str = Field(serialization_alias="serialNumber")
    issue_date: datetime = Field(serialization_alias="issueDate")
    expiry_date: datetime = Field(serialization_alias="expiryDate")
