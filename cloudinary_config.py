
import cloudinary
import os

cloudinary.config(
    cloud_name=os.getenv(
        "cloud_name"
    ),
    api_key=os.getenv(
        "api_key"
    ),
    api_secret=os.getenv(
        "api_secret"
    )
)