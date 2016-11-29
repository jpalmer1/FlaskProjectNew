from flask import Flask, render_template, jsonify, flash, request, url_for, redirect, session
import pymysql
pymysql.install_as_MySQLdb()
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
from MySQLdb import escape_string as thwart
import gc
from functools import wraps

def connection():
    conn = pymysql.connect(host='sql8.freemysqlhosting.net', port=3306, user='sql8146091', passwd='gLs1fMyhhT', db='sql8146091')
    c = conn.cursor()

    return c, conn 
 
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login_page'))

    return wrap

				 

# MySQL configurations
#app.config['MYSQL_DATABASE_USER'] = 'sql8146091'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'gLs1fMyhhT'
#app.config['MYSQL_DATABASE_DB'] = 'sql8146091'
#app.config['MYSQL_DATABASE_HOST'] = 'sql8.freemysqlhosting.net'
#mysql.init_app(app)

app = Flask(__name__)
app.secret_key = "super secret key"
conn = pymysql.connect(host='sql8.freemysqlhosting.net', port=3306, user='sql8146091', passwd='gLs1fMyhhT', db='sql8146091')

cur = conn.cursor()


#cur.execute("""INSERT INTO Users(ID, NAME, PASSWORD) VALUES ('2' ,'jack' , 'jack')""")

cur.execute("SELECT * FROM user")

print(cur.description)

print()

for row in cur:
    print(row)

cur.close()
conn.close()
@app.route("/logout/")

@login_required
def logout():
    session.clear()
    flash("You have been logged out!")
    gc.collect()
    return redirect(url_for('index'))

@app.route('/login.html/', methods=["GET","POST"])
def login_page():
    error = ''
    try:
        c, conn = connection()
        if request.method == "POST":

            data = c.execute("SELECT * FROM user WHERE username = (%s)",
                             thwart(request.form['username']))
            
            data = c.fetchone()[2]

            if sha256_crypt.verify(request.form['password'], data):
                session['logged_in'] = True
                session['username'] = request.form['username']

                flash("You are now logged in")
                return redirect(url_for("index"))

            else:
                error = "Invalid credentials, try again."

        gc.collect()

        return render_template("login.html", error=error)

    except Exception as e:
        flash(e)
        error = "Invalid credentials, try again."
        return render_template("login.html", error = error)
	
		
		
@app.route('/register.html/', methods=["GET","POST"])
def register_page():
    try:
        form = RegistrationForm(request.form)

        if request.method == "POST" and form.validate():
            username  = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))
            c, conn = connection()

            x = c.execute("SELECT * FROM user WHERE username = (%s)",
                          (thwart(username)))

            if int(x) > 0:
                flash("That username is already taken, please choose another")
                return render_template('register.html', form=form)

            else:
                c.execute("INSERT INTO user( username, password, email) VALUES ( %s,%s,%s)",
                          (thwart(username), thwart(password), thwart(email) ))
                
                conn.commit()
                flash("Thanks for registering!")
                c.close()
                conn.close()
                gc.collect()

                session['logged_in'] = True
                session['username'] = username

                return redirect(url_for('index'))

        return render_template("register.html", form=form)

    except Exception as e:
        return(str(e))
		
		
		
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
    return "John Palmer"
	
			
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
#aided with online tutorials from Python programming.net, and stackoverflow  