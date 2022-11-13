from flask import Flask, render_template, request, jsonify, make_response
from flask_mysqldb import MySQL
import sys
import base64
from PIL import Image
import io
import numpy as np
import face

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass123'
app.config['MYSQL_DB'] = 'voting'


@app.route("/")
def home2():
    return render_template("index.html")


@app.route("/signup")
def home():
    return render_template("signup.html")


mysql = MySQL(app)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/signup/create-entry", methods=['POST'])
def create_entry():
    req = request.get_json()
    aadharno = req['aadhar1']
    user = req['mobile1']
    email = req['email1']
    passwd = req['password']
    buffer = req['path5']
    cur = mysql.connection.cursor()
    cur.execute("insert into registration(adharno,username,email,password,image) values(%s,%s,%s,%s,%s)",
                (aadharno, user, email, passwd, buffer))
    mysql.connection.commit()
    cur.close()
    return make_response(jsonify({"message": "received"}), 200)


@app.route("/signin")
def signin():
    return render_template("signin.html")


@app.route("/signin/check", methods=['POST'])
def check():
    req = request.get_json()
    aadharno = req['aadhar2']
    username = req['mobile2']
    passwd = req['passwd2']
    flag = 0
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * from registration")
    if resultValue > 0:
        usersDetails = cur.fetchall()
        for user in usersDetails:
            if user[0] == aadharno and user[1] == username and user[3] == passwd:
                flag = 1
    if flag == 1:
        res = make_response(jsonify({"message": "True"}), 200)
        return res
    elif flag == 0:
        return make_response(jsonify({"message": "False"}), 200)


@app.route("/reg")
def reg():
    return render_template("reg.html")


@app.route("/parties")
def parties():
    return render_template("parties.html")


@app.route("/contactus")
def contact():
    return render_template('contactus.html')


@app.route("/votingpage")
def voting():
    return render_template('voting page.html')


@app.route("/election")
def election():
    return render_template('elections.html')


@app.route("/authenticate")
def authenticate():
    return render_template('authentication.html')


@app.route("/authenticate/check", methods=['POST'])
def check2():
    req = request.get_json();
    img1 = req['image']  #this is the fetched base64 which is done during authentication
    img2 = ''
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT image from registration");
    if resultValue > 0:
        usersDetails = cur.fetchall()
        for user in usersDetails:
            img2 = user[0]             #this is the fetched base64 which is done during registration
        analyze_user(img1, img2)
        return make_response(jsonify({"message": "received"}), 200)




if __name__ == "__main__":
    app.run(debug=True)
