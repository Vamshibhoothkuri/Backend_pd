from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routes.enquiry import router as enquiry_router

from Routes.admin import router as admin_router
from Routes.gallery import router as gallery_router
from Routes.upload import router as upload_router

app = FastAPI()
app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "*",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)
app.include_router(
    enquiry_router,
    prefix="/enquiries",
    tags=["Enquiries"]
)

app.include_router(
    admin_router,
    prefix="/admin",
    tags=["Admin"]
)

app.include_router(
    gallery_router,
    prefix="/gallery",
    tags=["Gallery"]
)

app.include_router(
    upload_router,
    prefix="/upload",
    tags=["Upload"]
)


@app.get("/")
async def home():

    return {
        "message": "Backend Running"
    }