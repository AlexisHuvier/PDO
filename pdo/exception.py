class PDOException(Exception):
    pass

class PDOSQLException(PDOException):
    pass

class PDOConnectionException(PDOException):
    pass