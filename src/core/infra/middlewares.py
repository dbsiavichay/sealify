import logging

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware

from src.core.app.exceptions import BaseException

logger = logging.getLogger(__name__)


class ErrorHandlingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except StarletteHTTPException as exc:
            logger.exception(
                "STARLETTE_ERROR :: %s :: %s",
                exc.__class__.__name__,
                {"message": exc.message, "detail": exc.detail},
            )
            return JSONResponse(
                status_code=exc.status_code,
                content={"error": exc.detail},
            )
        except BaseException as exc:
            logger.exception(
                "REQUEST_ERROR :: %s :: %s",
                exc.__class__.__name__,
                {"message": exc.message, "detail": exc.detail},
            )
            return JSONResponse(
                status_code=exc.status_code,
                content={"error": exc.message},
            )
        except Exception as exc:
            logger.exception("UNHANDLED_EXCEPTION :: %s", exc)
            return JSONResponse(
                status_code=500,
                content={"error": "Internal Server Error"},
            )
