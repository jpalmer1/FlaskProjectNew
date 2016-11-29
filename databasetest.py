from flask import Flask, render_template, jsonify, flash, request, url_for, redirect, session

import pymysql
pymysql.install_as_MySQLdb()
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
import gc
 
 
 
 
#def connection():
 #   conn = MySQLdb.connect(host="sql8.freemysqlhosting.net",
  #                         user = "sql8146091",
   #                        passwd = "gLs1fMyhhT",
    #                       db = "sql8146091")
    #c = conn.cursor()

    #return c, conn
#mysql = MySQL()



# MySQL configurations
#app.config['MYSQL_DATABASE_USER'] = 'sql8146091'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'gLs1fMyhhT'
#app.config['MYSQL_DATABASE_DB'] = 'sql8146091'
#app.config['MYSQL_DATABASE_HOST'] = 'sql8.freemysqlhosting.net'
#mysql.init_app(app)

app = Flask(__name__)

conn = pymysql.connect(host='sql8.freemysqlhosting.net', port=3306, user='sql8146091', passwd='gLs1fMyhhT', db='sql8146091')

cur = conn.cursor()

cur.execute("INSERT INTO user( username, password, email) VALUES ('password','password','pass@eircom.net')")


cur.execute("SELECT * FROM user")
conn.commit()
print(cur.description)

print()

for row in cur:
    print(row)

cur.close()
conn.close()


		
class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=20)])
    email = TextField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of Service and Privacy Notice (updated Jan 22, 2015)', [validators.Required()])
    

			

	
@app.route("/name")
def hello1():
    return "Pat Joyce"
	

	
#@app.route('/hello/')
#@app.route('/hello/<name>')
#def hello3(name=None):
 #   return render_template('index.html', name=name )
 
#@app.route('/')
#def index():
  #  return app.send_static_file('index.html')

			
@app.route('/index.html/')
@app.route('/')
def index():
	
    return render_template('index.html')
	 

					 


		

@app.route('/classes.html/')	
@app.route('/classes/')
def classes():
    return render_template("classes.html")
@app.route('/about.html/')
def about():
	return render_template("about.html")
@app.route('/FAQ.html/')
def FQA():
	return render_template("FAQ.html")

@app.route('/contact.html/')
def contact():
		return render_template("contact.html")
@app.route('/index2.html/')
def body():
		return render_template("index2.html")
@app.route('/main.html/')
def main():
		return render_template("main.html")	
if __name__ == "__main__":
    app.run()