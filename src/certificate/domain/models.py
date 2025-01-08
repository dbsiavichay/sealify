import uuid
from datetime import datetime


class Certificate:
    def __init__(
        self,
        id: uuid.UUID,
        subject_name: str,
        serial_number: int,
        issue_date: datetime,
        expiry_date: datetime,
        cert: str,
        key: str,
    ):
        self.id = id
        self.subject_name = subject_name
        self.serial_number = serial_number
        self.issue_date = issue_date
        self.expiry_date = expiry_date
        self.cert = cert
        self.key = key

    def __repr__(self):
        return f"Certificate(id={self.id})"

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.subject_name == other.subject_name
            and self.serial_number == other.serial_number
            and self.issue_date == other.issue_date
            and self.expiry_date == other.expiry_date
            and self.cert == other.cert
            and self.key == other.key
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(
            (
                self.id,
                self.subject_name,
                self.serial_number,
                self.issue_date,
                self.expiry_date,
                self.cert,
                self.key,
            )
        )
