__all__ = ["PDO"]

from pdo.exception import PDOException, PDOConnectionException

class PDO:
    requirements = {
        "sqlite": ("db",)
    }

    def __init__(self, raw_connection):
        connection_infos = {i.split("=")[0]: i.split("=")[1] for i in raw_connection.split(";") if "=" in i}
        if "module" in connection_infos.keys():
            if connection_infos["module"] in self.requirements.keys():
                for i in self.requirements[connection_infos["module"]]:
                    if i not in connection_infos.keys():
                        raise PDOConnectionException("Expect '"+i+"' argument in connection string")
            else:
                raise PDOConnectionException("Unknown 'module' argument in connection string")
        else:
            raise PDOConnectionException("Expect 'module' argument in connection string")

    @classmethod
    def modules(cls):
        return tuple(cls.requirements.keys())
    
    @classmethod
    def module_requirements(cls, module):
        if module in cls.requirements.keys():
            return cls.requirements[module]
        raise PDOException("Unknown module")