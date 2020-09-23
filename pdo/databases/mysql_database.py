import mysql.connector

from pdo import PDOSQLException

__all__ = ["MySQLDatabase"]

class MySQLDatabase:
    def __init__(self, args):
        self.connection = mysql.connector.connect(host=args["host"], user=args["user"], password=args["passwd"], database=args["db"])
        self.cursor = self.connection.cursor()
    
    def execute(self, query, tuples=None):
        error = None
        try:
            self.cursor = self.connection.cursor()
            if tuples is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, tuples)
        except mysql.connector.Error as e:
            error = str(e)
        if error is not None:
            raise PDOSQLException(error)

    def fetchall(self):
        error = None
        try:
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            error = str(e)
        if error is not None:
            raise PDOSQLException(error)
    
    def fetchone(self):
        error = None
        try:
            return self.cursor.fetchone()
        except mysql.connector.Error as e:
            error = str(e)
        if error is not None:
            raise PDOSQLException(error)
    
    def close(self):
        error = None
        try:
            self.cursor.close()
            self.connection.close()
        except mysql.connector.Error as e:
            error = str(e)
        if error is not None:
            raise PDOSQLException(error)