import MySQLdb
import config

def database(command_line,name=config.user_name ,pswd=config.key,dataname=config.sql_name):
    db=MySQLdb.connect(
        host="localhost",
        user=name,
        password=pswd,
        database=dataname,
        charset="utf8mb4"
    )
    cur = db.cursor()
    cur.execute(command_line)
    row = cur.fetchall()
    cur.close()
    db.close()
    return row

if __name__ == '__main__':
    result=len(database("SELECT name from users"))
    print(result)