from fastapi import APIRouter

from src import sealer_controller
from src.sealer.app.schemas import SealedResponseSchema, SealInvoiceSchema

router = APIRouter()


@router.post("/{id}/seal-invoice", response_model=SealedResponseSchema)
async def seal_invoice(id: str, input: SealInvoiceSchema):
    return await sealer_controller.seal_invoice(id, input)
