import pymysql.cursors
from flask import Flask, render_template, url_for, request, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash

login = Flask(__name__)

# Connect to the database
#url
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='hudacitycentre',
                             db='csci5410_2',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor,
                             autocommit=True)
								# charset='utf8mb4',
								# cursorclass=pymysql.cursors.DictCursor)
cursorObject = connection.cursor()


@login.route('/', methods=['GET'])
def index():
	return render_template('login.html')

@login.route('/log', methods=['POST'])
def log():
	email = request.form.get("email")
	password = request.form.get("password")
	sql = "SELECT `password` FROM `users` WHERE `email`=%s"
	cursorObject.execute(sql, (email))
	result = cursorObject.fetchone()
	sql = "SELECT `name` FROM `users` WHERE `email`=%s"
	cursorObject.execute(sql, (email))
	name = cursorObject.fetchone()
	print(password)
	print(name)
	if(result is not None and check_password_hash(result['password'], password)):
		# enter in status
		# url
		return redirect('http://0.0.0.0:5004/' + name['name'])
		# return render_template('logged.html', name=name['name'])
		# return render_template("log.html", name=name['name'], reg="Logged in Successfully")
	else:
		return render_template('login.html', err="Invalid credentials!")



# table = "users"
# create table users (
# 	id int not null,
# 	name varchar(255),
#     email varchar(255),
#     password varchar(255),
#     position varchar(255),
#     PRIMARY KEY (id)
# );


if __name__ == "__main__":
	login.debug = True
	login.run(host='127.0.0.1', port=5002)