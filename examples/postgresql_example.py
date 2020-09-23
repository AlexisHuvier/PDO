from pdo import PDO

db = PDO("module=postgresql;host=localhost;user=root;passwd=;db=nevinia")
db.execute("SELECT * FROM messages;")
print(db.fetchall())