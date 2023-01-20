#!/usr/bin/python3

from flask import Flask
import requests
from flask import redirect
from flask import url_for
from flask import render_template

"""
Make the landing page ("/") return an HTML form.

2. The form should ask a trivia question of your choosing
3. Depending on the answer POSTed from the form, do the following:
    - If the answer is correct, redirect your user to the "/correct" route!
    - If the answer is wrong, return them to the form to try again.
"""

URL= "https://opentdb.com/api.php?amount=10&category=9"
IMG= "static/OPENTRIVIA_LOGO.png"
APP= Flask(__name__)
TRIVIA= []
CURRENT_QUESTION_INDEX= 0
# {  
# 'category': 'General Knowledge', 
# 'type': 'multiple', 
# 'difficulty': 'medium', 
# 'question': 'Which river flows through the Scottish city of Glasgow?', 
# 'correct_answer': 'Clyde', 
# 'incorrect_answers': ['Tay', 'Dee', 'Tweed']  
# }

def getTrivia(url,trivia_dict):
    resp = requests.get(url).json()
    trivia_dict = resp["results"]
    return trivia_dict



@APP.route("/") # default GET
def index():
    return render_template("index.html", img= IMG)


# CRUD ROUTES
@APP.route("/login", methods= ["POST","GET"])
def login():
# curl http://0.0.0.0:2224/login -L -d name=Conan%20the%20Librarian
# http://0.0.0.0:2224/login?name=Conan%20the%20Librarian

    # user info passed form 
    if requests.method == "POST" and requests.form.get("name"):
        user_data = requests.form.get("name")
        return redirect(url_for("hello_name", name=user_data))
    
    # user info passed from url params OR comm ln args *not best practice
    # login?name=someName
    if requests.method == "GET" and requests.args.get("name"):
        user_data = requests.args.get("name")
        return redirect(url_for("hello_name", name=user_data))

    user_data = "defaul_user"
    return redirect(url_for("hello_name", name=user_data))

# PLAYFUL ROUTES
@APP.route("/hello")
def hello_world():
    return "hello from flask"

@APP.route("/admin")
def hello_admin():
    return "hello admin"

@APP.route("/hello/<name>")
def hello_name(name):
    if name == "admin" :
        return redirect(url_for("hello_admin"))
    return redirect(url_for("hello_name",name= name))   

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=3000)# http://0.0.0.0:3000/hello

