from fastapi import APIRouter
from db_service import use_mysql_service

router = APIRouter()

@router.post("/chatch_phrase")
def post_data(data:dict):
    """Inserts data into the MySQL database.

    Args:
        data (dict): A dictionary containing the data to be inserted.

    Returns:
        str: The inserted data value if successful.
        str: An error message if the insertion fails.
    """
    #return use_mysql_service.input_data(data)
    input_phrase = use_mysql_service.input_data(data)
    return input_phrase
        
@router.get("/chatch_phrase")
def latest_title():
    """Fetches the most recently registered data from the MySQL database.

    Returns:
        tuple: The most recently registered data.
        dict: An error message if the fetching fails.
    """
    latest_title = use_mysql_service.registered_data()
    return latest_title
    

# 6行　登録とゲットは同じURL名にすべき
