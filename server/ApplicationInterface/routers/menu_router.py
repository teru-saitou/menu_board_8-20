from fastapi import APIRouter
from smaregi_service import use_smaregi_service

router = APIRouter()

@router.get("/products")
def products():
    """Fetches product data from the Smaregi API.

    Returns:
        dict: A dictionary containing product data.
    """
    product_data = use_smaregi_service.product_data()
    return product_data

@router.get("/images")
def images():
    """Fetches image data from the Smaregi API.

    Returns:
        dict: A dictionary containing image data.
    """
    image_data = use_smaregi_service.image_data()
    print(image_data)
    return image_data