from flask import Flask
from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'db-jjpb-test.cushakf5p0bn.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'mysql_admin'
app.config['MYSQL_PASSWORD'] = '1nsecure'
app.config['MYSQL_DB'] = 'db-jjpb-test'

    mysql = MySQL(app)

@app.route("/")
def main():
    return render_template('index.html')
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')



@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)