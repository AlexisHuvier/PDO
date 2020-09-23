from pdo import PDO
import os

db = PDO("module=sqlite;db="+os.path.dirname(__file__)+"/sqlite_bdd.db")
db.execute("SELECT * FROM test WHERE id = 'A';")
print(db.fetchall())