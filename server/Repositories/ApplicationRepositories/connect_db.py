import MySQLdb 
import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent_dir)

import config


host = config.HOST
user = config.USER
password = config.PASSWORD
db = config.DB

class ConnectMysql:
    """A class used to represent a connection to a MySQL database.

    Attributes:
        host (str): The hostname of the MySQL server.
        user (str): The username to log in to the MySQL server.
        password (str): The password to log in to the MySQL server.
        db (str): The name of the database to connect to.
    """
    def __init__(self,host,user,password,db):
        """
        Args:
            host (str): The hostname of the MySQL server.
            user (str): The username to log in to the MySQL server.
            password (str): The password to log in to the MySQL server.
            db (str): The name of the database to connect to.
        """
        self.host = host
        self.user = user
        self.password = password
        self.db = db
    
    def connect(self):
        """Establishes a connection to the MySQL database.

        Returns:
            MySQLdb.connections.Connection: A connection object to the MySQL database.
        """
        return MySQLdb.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            db = self.db
        )
        
    def post_input_data(self,data:dict):
        """Inserts data into the database.
        
        Args:
            data (dict): A dictionary containing the data to be inserted.

        Returns:
            str: The inserted data value if successful.
            str: An error message if the insertion fails.
        """
        try:
            cnct = self.connect()
            cur = cnct.cursor() 
            data_value = data.get("data")
            sql = "INSERT INTO title(title)VALUES(%s)"
            cur.execute(sql,(data_value,)) 
            cnct.commit() 
            return  data_value
        except Exception as e:
            cnct.rollback()
            return f"Error inserting dada {str(e)}"
        finally:
            cnct.close()
            
    def get_registered_data(self):
        """Fetches the most recently registered data from the database.

        Returns:
            tuple: The most recently registered data.
            dict: An error message if the fetching fails.
        """
        try:
            cnct = self.connect()
            cur = cnct.cursor()
            sql =  "SELECT title FROM title ORDER BY title_id DESC LIMIT 1"
            cur.execute(sql)
            result = cur.fetchone()
            return result
        except Exception as e:
            return {"error": f"Error fetching data: {str(e)}"}
        finally:
            cnct.close()

from_mysql = ConnectMysql(host=host, user=user, password=password, db=db)









# 常に最新の一件を取得するSQLへ修正









