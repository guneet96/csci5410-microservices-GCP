import pymysql.cursors
from flask import Flask, render_template, url_for, request, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash


check = Flask(__name__)

# Connect to the database
# url
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

@check.route('/', methods=['GET', 'POST'])
def gg():
	return "asd"

@check.route('/<name>', methods=['GET', 'POST'])
def loggedin(name):
	print("gg")
	print(name)
	query = "INSERT into status (`name`, `stat`) VALUES (%s, %s)"
	cursorObject.execute(query, (name, "online"))

	sql = "SELECT * from status WHERE stat = 'online';"
	cursorObject.execute(sql)
	result = cursorObject.fetchall()

	# print(result.type)
	# cursorObject.execute(sqlQuery)
	# rows = cursorObject.fetchall()
	# print(rows)
	connection.commit()
	return render_template('log.html', result=result, name=name)


@check.route('/logout/<name>', methods=['POST'])
def logout(name):
	name = name
	sql = "UPDATE status SET stat='offline' WHERE `name`=(%s)"
	cursorObject.execute(sql, (name))
	# url
	return redirect("http://0.0.0.0:5002")


if __name__ == "__main__":
	check.debug = True
	check.run(host='0.0.0.0', port=5004)

