# db.py
import os
from contextlib import closing

import pymysql
from pymysql.cursors import DictCursor


class DatabaseConnector:
    """
    Connects to the MySQL database and returns the connection object.
    Modify the db_config dictionary with your actual database configuration.
    """

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state
        if not hasattr(self, "_connection"):
            self._connection = None
            self._config = {
                "host": os.environ.get("DB_HOST", "localhost"),
                "user": os.environ.get("DB_USER", ""),
                "password": os.environ.get("DB_PASSWORD", ""),
                "database": os.environ.get("DB_NAME", ""),
            }

    def connect(self):
        try:
            self._connection = pymysql.connect(**self._config)
        except pymysql.Error as e:
            print("Error connecting to database: {}".format(e))
            return None
        return self._connection

    def execute_query(self, sql, params=None):
        """
        Executes the provided SQL query and returns the result.
        """
        with closing(self._connection.cursor(DictCursor)) as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()

    def commit_query(self, sql, params=None):
        """
        Executes the provided SQL query and commits the transaction.
        """
        with closing(self._connection.cursor()) as cursor:
            cursor.execute(sql, params)
        self._connection.commit()  # commit transaction


def execute_query(sql, params=None):
    db_connector = DatabaseConnector()
    return db_connector.execute_query(sql, params)


def commit_query(sql, params=None):
    db_connector = DatabaseConnector()
    db_connector.commit_query(sql, params)
