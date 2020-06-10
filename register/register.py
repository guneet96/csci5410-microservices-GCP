import os
import pymysql.cursors
from flask import Flask, render_template, url_for, request, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash

register = Flask(__name__)

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


@register.route('/', methods=['GET'])
def index():
	# sqlQuery = "show tables;"
	# cursorObject.execute(sqlQuery)
	# rows = cursorObject.fetchall()
	# print(rows)
	return render_template('register.html')

@register.route('/reg', methods=['POST'])
def reg():
	name = request.form.get("name")
	email = request.form.get("email")
	password = request.form.get("password")
	position = request.form.get("position")
	password_hash = generate_password_hash(password)
	query = "INSERT into users (`name`, `email`, `password`, `position`) VALUES (%s, %s, %s, %s)"
	cursorObject.execute(query, (name, email,password_hash,position))
	# sqlQuery = "select * from users;"
	# cursorObject.execute(sqlQuery)
	# rows = cursorObject.fetchall()
	# print(rows)
	connection.commit()
	return render_template('reg.html', reg = "Registered Successfully")



# def show_table(table):
# 	sqlQuery = "select * from " + str(table) + ";"
# 	cursorObject.execute(sqlQuery)
# 	rows = cursorObject.fetchall()
# 	print(rows)


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
	register.debug = True
	register.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))

