from fastapi import APIRouter
from database import db

from schemas.admin import (
    AdminRegister,
    AdminLogin
)

from auth import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter()


@router.post("/register")
async def register(admin: AdminRegister):

    existing_admin = await db.admins.find_one({
        "username": admin.username
    })

    if existing_admin:

        return {
            "message": "Admin already exists"
        }

    hashed_password = hash_password(
        admin.password
    )

    await db.admins.insert_one({
        "username": admin.username,
        "password": hashed_password
    })

    return {
        "message": "Admin Registered Successfully"
    }


@router.post("/login")
async def login(admin: AdminLogin):

    existing_admin = await db.admins.find_one({
        "username": admin.username
    })

    if not existing_admin:

        return {
            "message": "Invalid Username"
        }

    is_valid = verify_password(
        admin.password,
        existing_admin["password"]
    )

    if not is_valid:

        return {
            "message": "Invalid Password"
        }

    token = create_access_token({
        "id": str(existing_admin["_id"]),
        "username": existing_admin["username"]
    })

    return {
        "token": token,
        "username": existing_admin["username"]
    }