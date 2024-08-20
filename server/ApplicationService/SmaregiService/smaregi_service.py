import sys
sys.path.append("/Users/saitouterataka/TrainingProjects/reMenuBoard/server/Repositories/SmaregiRepositories")
from connect_smaregi_developers import smaregi_api

access_token = smaregi_api.get_access_token()

class SmaregiService:
    """A class used to interact with the Smaregi API.

    Attributes:
        client_id (str): The client ID for the Smaregi API.
        client_secret (str): The client secret for the Smaregi API.
    """
    def product_data(self):
        """Fetches product data from the Smaregi API.

        Returns:
            dict: A dictionary containing product data.
        """
        product_data = smaregi_api.get_products(access_token) 
        return product_data
        
    def image_data(self):
        """Fetches image data from the Smaregi API.

        Returns:
            dict: A dictionary containing image data.
        """
        image_data = smaregi_api.get_images(access_token)
        return image_data

use_smaregi_service = SmaregiService()
