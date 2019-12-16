from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, session, abort 
from flask_mysqldb import MySQL
import re
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'jjpb-test.cushakf5p0bn.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'mysql_admin'
app.config['MYSQL_PASSWORD'] = '1nsecure'
app.config['MYSQL_DB'] = 'testingjjpb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Intialize MySQL
mysql = MySQL(app)


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
            cur.execute("SELECT * FROM preferences WHERE name = %s", [var_name])
            account = cur.fetchone()
            print(account)
            if account:
                msg = 'User already exists!!'
                render_template('index.html', msg=msg)
            else:
                t  = (var_name, var_color, var_pet)
                cur.execute("INSERT INTO preferences VALUES(NULL,%s,%s,%s)", t)
                mysql.connection.commit()
                msg = 'User does not exists, Created'
                return render_template('index.html', msg=msg)
        except mysql.connection.ProgrammingError as err:
            print("Error", err)
            abort(500)
        cur.close()
    
    return render_template('index.html', msg=msg)

@app.route("/", methods=['GET','POST'])
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    #app.run()