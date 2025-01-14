from src.sealer.app.schemas import SealedResponseSchema, SealInvoiceSchema
from src.sealer.app.services import SealerService


class SealerController:
    def __init__(self, service: SealerService) -> None:
        self.service = service

    async def seal(self, input: SealInvoiceSchema) -> SealedResponseSchema:
        data = self.service.seal(input)
        return SealedResponseSchema(sealed_data=data)
