from fastapi import APIRouter, Depends
from bson import ObjectId

from database import db

from auth import verify_token

from schemas.gallery import GalleryCreate

router = APIRouter()


def serialize(item):

    return {

        "id": str(item["_id"]),

        "name": item["name"],

        "url": item["url"],

        "type": item["type"],

        "category": item["category"],

        "section": item.get("section"),

        "designType": item.get("designType"),

        "service": item.get("service")
    }


@router.get("")
async def get_gallery():

    items = await db.gallery.find().to_list(1000)

    return [serialize(item) for item in items]


@router.post("")
async def add_gallery_item(
    payload: GalleryCreate,
    user=Depends(verify_token)
):

    result = await db.gallery.insert_one({

    "name": payload.name,

    "url": payload.url,

    "type": payload.type,

    "category": payload.category,

    "section": payload.section,

    "designType": payload.designType,

    "service": payload.service
})

    return {
        "message": "Gallery Item Added",
        "id": str(result.inserted_id)
    }


@router.delete("/{item_id}")
async def delete_gallery_item(
    item_id: str,
    user=Depends(verify_token)
):

    await db.gallery.delete_one({
        "_id": ObjectId(item_id)
    })

    return {
        "message": "Deleted Successfully"
    }