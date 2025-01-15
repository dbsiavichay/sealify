from pydantic import BaseModel


class ResourceDeletedSuccessfullyResponseSchema(BaseModel):
    message: str = "Resource deleted successfully"
