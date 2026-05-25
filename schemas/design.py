from pydantic import BaseModel
from typing import List


class DesignCreate(BaseModel):

    title: str
    slug: str
    category: str
    section: str
    type: str
    description: str

    thumbnail: str

    images: List[str] = []
    videos: List[str] = []