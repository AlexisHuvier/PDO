import sqlite3

from pdo import PDOSQLException

__all__ = ["SQLiteDatabase"]

class SQLiteDatabase:
    def __init__(self, args):
        self.connection = sqlite3.connect(args["db"])
        self.cursor = self.connection.cursor()
    
    def execute(self, query, tuples=None):
        error = None
        try:
            self.cursor = self.connection.cursor()
            if tuples is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, tuples)
        except sqlite3.Error as e:
            error = str(e)
        if error is not None:
            raise PDOSQLException(error)

    def fetchall(self):
        error = None
        try:
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            error = str(e)
        if error is not None:
            raise PDOSQLException(error)
    
    def fetchone(self):
        error = None
        try:
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            error = str(e)
        if error is not None:
            raise PDOSQLException(error)
    
    def close(self):
        error = None
        try:
            self.cursor.close()
            self.connection.close()
        except sqlite3.Error as e:
            error = str(e)
        if error is not None:
            raise PDOSQLException(error)