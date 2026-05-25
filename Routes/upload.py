from fastapi import APIRouter, UploadFile, File, Depends
import cloudinary.uploader

from auth import verify_token

import cloudinary_config

router = APIRouter()


@router.post("/image")
async def upload_image(
    file: UploadFile = File(...),
    user=Depends(verify_token)
):

    result = cloudinary.uploader.upload(
        file.file,
        folder="pdinteriors/images"
    )

    return {
        "url": result["secure_url"]
    }


@router.post("/video")
async def upload_video(
    file: UploadFile = File(...),
    user=Depends(verify_token)
):

    result = cloudinary.uploader.upload(
        file.file,
        resource_type="video",
        folder="pdinteriors/videos"
    )

    return {
        "url": result["secure_url"]
    }