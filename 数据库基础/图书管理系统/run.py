import MySQLdb
import config
import MySQLdb.cursors  # 需要导入 cursors

def database(command_line, name=config.user_name, pswd=config.key, dataname=config.sql_name):
    db = MySQLdb.connect(
        host="localhost",
        user=name,
        password=pswd,
        database=dataname,
        charset="utf8mb4",
        cursorclass=MySQLdb.cursors.DictCursor  # 关键！指定游标类型
    )
    cur = db.cursor()
    cur.execute(command_line)
    row = cur.fetchall()  # 现在 row 是一个字典列表
    cur.close()
    db.close()
    return row
if __name__ == '__main__':
    result=  database('select * from users')
    print(result)