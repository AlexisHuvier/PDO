from pdo import PDO

PDO("module=sqlite;db=bdd.db")
print(PDO.modules())
print(PDO.module_requirements("sqlite"))