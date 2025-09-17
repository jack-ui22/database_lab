from flask import Flask, render_template, request, redirect, session, url_for, flash
from run import database

premission=0 #权限管理
app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
def home():
    if 'logged_in' in session and session['logged_in']:
        return "<h1>欢迎!</h1><a href='/logout'>退出</a>"
    # 显示登录页面
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    # 获取表单数据
    username = request.form.get('username')
    password = request.form.get('password')
    result=database(f'SELECT pswd FROM users WHERE name = "{username}" ')
    print(result[0]['pswd'])
    if result != None and result[0]['pswd']==password:
        session['logged_in'] = True
        session['username'] = username
        admin=database(f'SELECT is_admin FROM users WHERE name = "{username}" ')
        if admin[0]['is_admin']==1:
            return redirect(url_for('admin'))
        return redirect(url_for('user'))
    else:
        return "登录失败! <a href='/'>返回</a>"
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
@app.route('/admin')
def admin():
    if 'logged_in' in session and session['logged_in']:
        username = session['username']
        admin = database(f'SELECT is_admin FROM users WHERE name = "{username}" ')
        if admin[0]['is_admin'] == 1:
            book_num = len(database("SELECT name from book"))
            user_num = len(database("SELECT name from users"))
            books=database('select * from book')
            users=database('select * from users')
            record=database('select * from record')
            print(book_num,user_num,books,users,record)
            return render_template('admin.html',book_num=book_num ,user_num=user_num,books=books,users=users,records=record)
    return "无权限访问！ <a href='/'>返回</a>"
@app.route('/user')
def user():
    if 'logged_in' in session and session['logged_in']:
        username = session['username']
        user = database(f'SELECT is_admin FROM users WHERE name = "{username}" ')
        if user[0]['is_admin'] == 0:
            return render_template('user.html')
    return "无权限访问！ <a href='/'>返回</a>"

if __name__ == '__main__':
    app.run(debug=True)
# from flask import Flask, request, render_template
#
# app = Flask(__name__)
#
# @app.route('/', methods=['GET'])
# def index():
#     # 初始访问不显示结果
#     return render_template('index.html', result=None, a='', b='')
#
# @app.route('/add', methods=['POST'])
# def add():
#     a = request.form.get('a', '')
#     b = request.form.get('b', '')
#     try:
#         ra = float(a)
#         rb = float(b)
#         res = ra + rb
#         # 如果是整数就显示整数格式
#         if isinstance(res, float) and res.is_integer():
#             res = int(res)
#         result = res
#     except (ValueError, TypeError):
#         result = '输入无效，请输入数字'
#     return render_template('index.html', result=result, a=a, b=b)
#
# if __name__ == '__main__':
#     app.run(debug=True)