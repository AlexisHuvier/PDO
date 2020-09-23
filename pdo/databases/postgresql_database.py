import psycopg2

from pdo import PDOSQLException

__all__ = ["PostgreSQLDatabase"]

class PostgreSQLDatabase:
    def __init__(self, args):
        self.connection = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (args["host"], args["db"], args["user"], args["passwd"]))
        self.cursor = self.connection.cursor()
    
    def execute(self, query, tuples=None):
        error = None
        try:
            self.cursor = self.connection.cursor()
            if tuples is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, tuples)
        except psycopg2.Error as e:
            error = str(e)
        if error is not None:
            raise PDOSQLException(error)

    def fetchall(self):
        error = None
        try:
            return self.cursor.fetchall()
        except psycopg2.Error as e:
            error = str(e)
        if error is not None:
            raise PDOSQLException(error)
    
    def fetchone(self):
        error = None
        try:
            return self.cursor.fetchone()
        except psycopg2.Error as e:
            error = str(e)
        if error is not None:
            raise PDOSQLException(error)
    
    def close(self):
        error = None
        try:
            self.cursor.close()
            self.connection.close()
        except psycopg2.Error as e:
            error = str(e)
        if error is not None:
            raise PDOSQLException(error)