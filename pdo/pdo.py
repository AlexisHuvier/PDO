__all__ = ["PDO"]

from pdo.exception import PDOException, PDOConnectionException

class PDO:
    requirements = {
        "sqlite": ("db",),
        "mysql": ("host", "user", "passwd", "db"),
        "postgresql": ("host", "user", "passwd", "db")
    }

    def __init__(self, raw_connection):
        connection_infos = {i.split("=")[0]: i.split("=")[1] for i in raw_connection.split(";") if "=" in i}
        if "module" in connection_infos.keys():
            self.module = connection_infos["module"]
            del connection_infos["module"]
            if self.module in self.requirements.keys():
                for i in self.requirements[self.module]:
                    if i not in connection_infos.keys():
                        raise PDOConnectionException("Expect '"+i+"' argument in connection string")
                if self.module == "sqlite":
                    from pdo.databases.sqlite_database import SQLiteDatabase

                    self.db = SQLiteDatabase(connection_infos)
                elif self.module == "mysql":
                    from pdo.databases.mysql_database import MySQLDatabase

                    self.db = MySQLDatabase(connection_infos)
                elif self.module == "postgresql":
                    from pdo.databases.postgresql_database import PostgreSQLDatabase

                    self.db = PostgreSQLDatabase(connection_infos)
            else:
                raise PDOConnectionException("Unknown 'module' argument in connection string")
        else:
            raise PDOConnectionException("Expect 'module' argument in connection string")
    
    def execute(self, query, tuples=None):
        self.db.execute(query, tuples)

    def fetchall(self):
        return self.db.fetchall()
    
    def fetchone(self):
        return self.db.fetchone()
    
    def close(self):
        self.db.close()

    @classmethod
    def modules(cls):
        return tuple(cls.requirements.keys())
    
    @classmethod
    def module_requirements(cls, module):
        if module in cls.requirements.keys():
            return cls.requirements[module]
        raise PDOException("Unknown module")