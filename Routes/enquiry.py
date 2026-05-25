from fastapi import APIRouter, HTTPException
from bson import ObjectId
from database import db
from schemas.enquiry import EnquiryCreate

router = APIRouter()


@router.post("/")
async def create_enquiry(payload: EnquiryCreate):
    data = payload.dict()

    result = await db.enquiries.insert_one(data)

    return {
        "message": "Enquiry submitted successfully",
        "id": str(result.inserted_id)
    }
@router.get("/")
async def get_enquiries():
    enquiries = []

    async for item in db.enquiries.find().sort("_id", -1):
        enquiries.append({
            "id": str(item["_id"]),
            "firstName": item.get("firstName"),
            "lastName": item.get("lastName"),
            "email": item.get("email"),
            "phone": item.get("phone"),
            "projectType": item.get("projectType"),
            "message": item.get("message")
        })

    return enquiries


@router.delete("/{id}")
async def delete_enquiry(id: str):
    result = await db.enquiries.delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Enquiry not found")

    return {
        "message": "Enquiry deleted successfully"
    }