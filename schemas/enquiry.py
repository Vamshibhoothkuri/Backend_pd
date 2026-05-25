from pydantic import BaseModel, EmailStr
from typing import Optional


class EnquiryCreate(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    phone: Optional[str] = None
    projectType: Optional[str] = None
    message: str


class EnquiryResponse(EnquiryCreate):
    id: str