from pydantic import BaseModel, Field


class SealInvoiceSchema(BaseModel):
    invoice_xml: str = Field(alias="invoiceXML", description="Invoice as xml format")


class SealedResponseSchema(BaseModel):
    sealed_data: str = Field(serialization_alias="sealedData")
