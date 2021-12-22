from flask import Flask, render_template, request, render_template_string, redirect, session
import sqlite3
import os
from os import getenv
import hashlib

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

def connect_db():
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()
    return cursor

@app.route("/")
def homeView():
    cursor = connect_db()
    if session.get("username") is not None:
        username = session["username"]
        cursor.execute("SELECT user_id FROM Users WHERE username=?", (username,))
        user = cursor.fetchone()
        cursor.execute("SELECT * FROM Recipes WHERE user_id=?", (user[0], ))

        rows = cursor.fetchall()

        recipes = []
        for row in rows:
            recipes.append(row)
        return render_template('index.html', recipes=recipes)
    else:
        return render_template('login.html')

@app.route("/<id>", methods=['GET'])
def show_recipe(id):
    # if session.get("username") is not None:
        cursor = connect_db()
        cursor.execute("SELECT * FROM Recipes WHERE recipe_id='%s'" % (id))
        recipe = cursor.fetchone()
        # if recipe[3] != session["username"]:
        #     return render_template_string('<h2>Error 403: Access denied</<h2>')
        if recipe == None:
            return render_template_string('<h2>Error 404: The page you were looking for does not exist</h2>')
        return render_template_string("""
        <h2>{{recipe[1]}}</h2>
        <p>{{recipe[2]}}</p>
        """, recipe=recipe)
    # else:
    #     return render_template('login.html')


@app.route("/create")
def create_recipe():
    return render_template('create.html')

@app.route("/sign")
def create_account():
    return render_template('new_user.html')

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()

        recipe_name = request.form.get('recipe')
        recipe_url = request.form.get('url')
        if session.get("username") is not None:
            username = session['username']
            cursor.execute("SELECT user_id FROM Users WHERE username=?", (username,))
            user = cursor.fetchone()

            cursor.execute("INSERT INTO Recipes(name, url, user_id) VALUES (?,?,?)", (recipe_name, recipe_url, user[0]))
            conn.commit()
        else:
            return redirect('/')

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor = connect_db()
    cursor.execute("SELECT user_id, password FROM Users WHERE username=?", (username,))
    user = cursor.fetchone()
    if not user:
        session['message'] = 'Username not found'
    elif password != user[1]:
        session['message'] = 'Incorrect password'
    else:
        session["username"] = username
        session["message"] = None

    return redirect('/')

@app.route('/logout')
def logout():
    del session["username"]
    return redirect("/")

# def checkPassword(password):
#     if len(password) < 3:
#         return False
#
#     # initializing flag variable
#     letters = False
#     numbers = False
#
#     for i in password:
#
#         if i.isalpha():
#             letters = True
#
#         if i.isdigit():
#             numbers = True
#
#     return letters and numbers



@app.route('/sign-up', methods=['POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # b_password = bytes(password, 'utf-8')
        # password = hashlib.sha256(b_password).hexdigest()

        # if checkPassword(password) == False:
        #     session["message"] == "password must have at least three characters that include both letters and numbers"

        conn = sqlite3.connect('db.sqlite')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users(username, password) VALUES (?,?)", (username, password))
        conn.commit()

    return redirect('/')
