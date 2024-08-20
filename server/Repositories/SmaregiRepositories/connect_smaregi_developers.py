import urllib.parse
import urllib3
import urllib.request
import json
import base64
import interface
import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent_dir)

import config


client_id = config.CLIENT_ID
client_secret = config.CLIENT_SECRET
contract_id = config.CONTRACT_ID

class ConnectSmaregiDevelopers(interface.SmaregiData):
    """
    A class to connect and interact with the Smaregi Developers API.

    This class provides methods to authenticate and retrieve product and image data from the Smaregi Developers API.

    Attributes:
        client_id (str): The client ID for the application.
        client_secret (str): The client secret for the application.
        contract_id (str): The contract ID for the Smaregi Developers API.
        token_url (str): The URL to obtain the access token.
        product_url (str): The URL to retrieve product data.
        image_url (str): The URL to retrieve image data.
        http (urllib3.PoolManager): The HTTP manager for making requests.
        sort (str): The sorting parameter for product data.
    """
    def __init__(self, client_id, client_secret):
        """
        Initializes the ConnectSmaregiDevelopers class with the provided client ID and client secret.

        Args:
            client_id (str): The client ID for the application.
            client_secret (str): The client secret for the application.
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.contract_id = contract_id
        self.token_url = f"https://id.smaregi.dev/app/{self.contract_id}/token"
        self.product_url = f"https://api.smaregi.dev/{self.contract_id}/pos/products"
        self.image_url = f"https://api.smaregi.dev/{self.contract_id}/pos/products/images"
        self.http = urllib3.PoolManager()
        self.sort = "productId"
        
    def get_access_token(self):
        """
        Retrieves an access token using client credentials.

        This method encodes the client ID and client secret in base64, constructs the necessary headers and body for the
        token request, and sends a POST request to the token URL. If successful, it returns the access token. If an error
        occurs, it prints an error message and returns None.

        Returns:
            str: The access token if the request is successful, None otherwise.

        Raises:
            Exception: If there is an error in the token retrieval process.
        """
        credentials = f"{self.client_id}:{self.client_secret}"
        base64_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
        header = {
            "Authorization": f"Basic {base64_credentials}",
            "Content-Type":"application/x-www-form-urlencoded"
        }
        body ={
            "grant_type": "client_credentials",
            "scope": "pos.products:read" 
        }
        data = urllib.parse.urlencode(body).encode("utf-8")
        
        try:
            response_status = self.http.request(method="POST", url=self.token_url, body=data, headers=header).status
            request = self.http.request(method="POST", url=self.token_url, body=data, headers=header).data
            access_token = json.loads(request)["access_token"]
            if response_status == 200:
                print("status=200")
                return access_token
            elif response_status ==401:
                print("status=401")
                self.get_access_token_again(self)
                return access_token
            else:
                return None
        except Exception as e:
            print(f"アクセストークン取得エラー:{e}")
            return None
        
    def get_access_token_again(self):
        """
        Retrieves an access token using client credentials again.

        This method is called if the initial token retrieval fails with a 401 status. It re-encodes the client ID and
        client secret in base64, constructs the necessary headers and body for the token request, and sends another POST
        request to the token URL. If successful, it returns the access token.

        Returns:
            str: The access token if the request is successful, None otherwise.
        """
        credentials = f"{self.client_id}:{self.client_secret}"
        base64_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
        header = {
            "Authorization": f"Basic {base64_credentials}",
            "Content-Type":"application/x-www-form-urlencoded"
        }
        body ={
            "grant_type": "client_credentials",
            "scope": "pos.products:read"
        }
        data = urllib.parse.urlencode(body).encode("utf-8")
        request = self.http.request(method="POST", url=self.token_url, body=data, headers=header).data
        access_token = json.loads(request)["access_token"]
        return access_token

    def get_products(self,access_token):
        """
        Retrieves a list of products using the provided access token.

        This method constructs the URL for sorting products, sets the authorization header with the access token, and sends
        a GET request to retrieve the product list. If successful, it returns the product list. If an error occurs, it prints
        an error message and returns None.

        Args:
            access_token (str): The access token for authorization.

        Returns:
            list: The product list if the request is successful, None otherwise.

        Raises:
            Exception: If there is an error in the product retrieval process.
        """
        sort_product_url = f"{self.product_url}?sort={self.sort}"
        header = {
            "Authorization" : f"Bearer {access_token}"
        }
        try:
            product_request = self.http.request(method="GET", url=sort_product_url , headers=header).data
            product_list = json.loads(product_request)
            return product_list
        except Exception as e:
            print("商品リストの取得エラー:{e}")
            return None
    
    def get_images(self,access_token):
        """
        Retrieves a list of images using the provided access token.

        This method sets the authorization header with the access token and sends a GET request to retrieve the image list.
        If successful, it returns the image list. If an error occurs, it prints an error message.

        Args:
            access_token (str): The access token for authorization.

        Returns:
            list: The image list if the request is successful, None otherwise.

        Raises:
            Exception: If there is an error in the image retrieval process.
        """
        header = {
            "Authorization" : f"Bearer {access_token}"
        }
        try:
            image_request = self.http.request(method="GET", url=self.image_url , headers=header).data
            image_list = json.loads(image_request)
            return image_list
        except Exception as e:
            print("画像一覧の取得エラー:{e}")
    
    def smaregi_data(self):
        pass

smaregi_api = ConnectSmaregiDevelopers(client_id ,client_secret)
access_token = smaregi_api.get_access_token()



# 1??行,ロジックが一緒で圧縮できるものはまとめる