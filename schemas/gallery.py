from pydantic import BaseModel


class GalleryCreate(BaseModel):

    name: str

    url: str

    type: str

    category: str

    section: str

    designType: str

    service: str | None = None