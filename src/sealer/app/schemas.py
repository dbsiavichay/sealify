import uuid

from pydantic import BaseModel, Field


class SealInvoiceSchema(BaseModel):
    certificate_id: uuid.UUID = Field(alias="certificateID")
    invoice_xml: str = Field(alias="invoiceXML")


class SealedResponseSchema(BaseModel):
    sealed_data: str = Field(serialization_alias="sealedData")
