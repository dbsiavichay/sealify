from fastapi import APIRouter

from src import sealer_controller
from src.sealer.app.schemas import SealedResponseSchema, SealInvoiceSchema

router = APIRouter()


@router.post("/seal-invoice", response_model=SealedResponseSchema)
async def seal_invoice(input: SealInvoiceSchema):
    return await sealer_controller.seal(input)
