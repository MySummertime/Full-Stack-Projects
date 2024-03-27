# db.py
import os

import pymysql


class DatabaseConnector:
    """
    Connects to the MySQL database and returns the connection object.
    Modify the db_config dictionary with your actual database configuration.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnector, cls).__new__(cls)
            cls._instance._connection = None
        return cls._instance

    def connect(self):
        if self._connection is None:
            db_config = {
                "host": os.environ.get("DB_HOST", "localhost"),
                "user": os.environ.get("DB_USER", "root"),
                "password": os.environ.get("DB_PASSWORD", ""),
                "database": os.environ.get("DB_NAME", ""),
            }
            try:
                self._connection = pymysql.connect(**db_config)
            except pymysql.Error as e:
                print("Error connecting to database: {}".format(e))
                return None
        return self._connection

    def close(self):
        if self._connection is not None:
            self._connection.close()


db_connector = DatabaseConnector()


def execute_query(sql, params=None):
    """
    Executes the provided SQL query and returns the result.
    """
    connection = db_connector.connect()
    if connection:
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(sql, params)
                result = cursor.fetchall()
                return result
        finally:
            connection.close()
    else:
        return None


def commit_query(sql, params=None):
    """
    Executes the provided SQL query and commits the transaction.
    """
    connection = db_connector.connect()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql, params)
            connection.commit()  # commit transaction
        finally:
            connection.close()
    else:
        return None
