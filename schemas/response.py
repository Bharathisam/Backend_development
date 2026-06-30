from typing import Any

from pydantic import BaseModel


class SuccessResponse(BaseModel):
    message: str
    data: Any


class ErrorDetail(BaseModel):
    code: int
    message: str


class ErrorResponse(BaseModel):
    error: ErrorDetail