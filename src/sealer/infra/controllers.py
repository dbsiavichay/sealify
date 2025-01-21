from src.sealer.app.schemas import SealedResponseSchema, SealInvoiceSchema
from src.sealer.app.services import SealerService


class SealerController:
    def __init__(self, service: SealerService) -> None:
        self.service = service

    async def seal_invoice(
        self, certificate_id: str, input: SealInvoiceSchema
    ) -> SealedResponseSchema:
        data = self.service.seal_invoice(certificate_id, input)
        return SealedResponseSchema(sealed_data=data)
