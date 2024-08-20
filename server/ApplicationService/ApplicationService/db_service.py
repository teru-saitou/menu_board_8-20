import os
import config
import sys
sys.path.append("/Users/saitouterataka/TrainingProjects/reMenuBoard/server/Repositories/ApplicationRepositories")

from connect_db import from_mysql 
parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent_dir)


host = config.HOST
user = config.USER
password = config.PASSWORD
db = config.DB

class MysqlService:
    """A class used to interact with a MySQL database through a service layer.

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
        
    def connection(self):
        """Establishes a connection to the MySQL database.

        Returns:
            MySQLdb.connections.Connection: A connection object to the MySQL database.
        """
        con = from_mysql.connect()
        return con
    
    def input_data(self,data):
        """Inserts data into the MySQL database.

        Args:
            data (dict): A dictionary containing the data to be inserted.

        Returns:
            str: The inserted data value if successful.
            str: An error message if the insertion fails.
        """
        input_data = from_mysql.post_input_data(data)
        return input_data
    
    def registered_data(self):
        """Fetches the most recently registered data from the MySQL database.

        Returns:
            tuple: The most recently registered data.
            dict: An error message if the fetching fails.
        """
        reg_data = from_mysql.get_registered_data()
        return reg_data

use_mysql_service = MysqlService(host,user,password,db)


# 名前はmysql_serviceよりrepositoryもっと言えば、環境ファイルに書い