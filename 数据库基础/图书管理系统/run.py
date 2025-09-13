import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="pswd",
    db="db_name"
)

cursor = db.cursor()
cursor.execute("show tables;")
results = cursor.fetchall()
print(results)