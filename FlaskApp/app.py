from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, session, abort 
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'jjpb-test.cushakf5p0bn.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'mysql_admin'
app.config['MYSQL_PASSWORD'] = '1nsecure'
app.config['MYSQL_DB'] = 'testingjjpb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Intialize MySQL
mysql = MySQL(app)


####name = 'ksg'
####age = 19
####sex = 'male'
####t  = (name, age, sex)
####cursor.execute("insert into table values(%s,%d,%s)", t)

#######@app.route('/', methods=['GET','POST'])
#######def main():
#######    # Output message if something goes wrong...
#######    msg = 'Wrong'
#######    # Check if "username" and "password" POST requests exist (user submitted form)
#######    if request.method == 'POST' and 'name' in request.form and 'color' in request.form:
#######        # Create variables for easy access
#######        var_name = request.form['name']
#######        var_color = request.form['color']
#######        var_pet = request.form['pet']
#######        # Check if account exists using MySQL
#######        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#######        cursor.execute('SELECT * FROM preferences WHERE name = %s', (var_name))
#######        # Fetch one record and return result
#######        account = cursor.fetchone()
#######        # If account exists in accounts table in out database
#######        if account:
#######            msg = 'User Already Exists!!'
#######            # Create session data, we can access this data in other routes
#######            #session['loggedin'] = True
#######            #session['id'] = account['id']
#######            #session['username'] = account['username']
#######            # Redirect to home page
#######            return 'User Exist!'
#######        else:
#######            # Account doesnt exist or username/password incorrect
#######            msg = 'User Does not exists'
#######    # Show the login form with message (if any)
#######    return render_template('index.html', msg=msg)

@app.route("/handle_data", methods=['GET','POST'])
def handle_data():
    msg = 'Wrong'
    var_name = request.form['inputName']
    var_color = request.form['favoriteColor']
    var_pet = request.form['comboPet']
    if request.method == 'POST' and 'inputName' in request.form:
        # Create variables for easy access
        var_name = request.form['inputName']
        var_color = request.form['favoriteColor']
        var_pet = request.form['comboPet']
        print("Name: %s"%(var_name))
        print("Color: %s"%(var_color))
        print("Pet: %s"%(var_pet))
        # Check if account exists using MySQL
        try:
            cur = mysql.connection.cursor()
            #cur.execute('''SELECT * FROM testingjjpb.preferences''')
            cur.execute("SELECT * FROM preferences WHERE name = %s", [var_name])
            account = cur.fetchone()
            print(account)
            if account:
                msg = 'User Already Exists!!'
                return 'User Already Exist!'
            else:
                t  = (var_name, var_color, var_pet)
                cur.execute("INSERT INTO preferences VALUES(NULL,%s,%s,%s)", t)
                mysql.connection.commit()
                msg = 'User Does not exists'
                return 'User Does not Exist!'
        except mysql.connection.ProgrammingError as err:
            print("Error", err)
            abort(500)
    # Show the login form with message (if any)
        cur.close()
    
    return render_template('index.html', msg=msg)

@app.route("/", methods=['GET','POST'])
def main():
    return render_template('index.html')


##@app.route('/', methods=['GET', 'POST'])
##def main():
##    if request.method == "POST":
##        details = request.form
##        firstName = details['fname']
##        lastName = details['lname']
##        cur = mysql.connection.cursor()
##        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
##        mysql.connection.commit()
##        cur.close()
##        return 'success'
##    return render_template('index.html')
##



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    #app.run()