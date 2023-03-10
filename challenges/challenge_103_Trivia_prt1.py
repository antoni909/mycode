#!/usr/bin/python3

import random
import requests
from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request

URL= "https://opentdb.com/api.php?amount=20&type=multiple"
IMG= "static/OPENTRIVIA_LOGO.png"
APP= Flask(__name__)
TRIVIA= []
QUESTION_IDX= 0

def getNextQuestion():
    global QUESTION_IDX
    global TRIVIA

    if( QUESTION_IDX in range(len(TRIVIA)) ):
        QUESTION_IDX += 1

def getAnswersList():
    random_idx = random.randint(0,len(TRIVIA[QUESTION_IDX]["correct_answer"]))
    correct_a = TRIVIA[QUESTION_IDX]["correct_answer"]
    answers_list = TRIVIA[QUESTION_IDX]["incorrect_answers"]
    if TRIVIA[QUESTION_IDX]["correct_answer"] not in TRIVIA[QUESTION_IDX]["incorrect_answers"]:
        answers_list.insert(random_idx,correct_a)
    return answers_list

@APP.route("/") 
def index():
    print(TRIVIA[QUESTION_IDX]["correct_answer"])
    answers_list = getAnswersList()
    return render_template("index.html", img= IMG, current_trivia = TRIVIA[QUESTION_IDX], answers = answers_list, length = len(answers_list))

@APP.route("/handle_resp", methods = ["POST", "GET"])
def handle_response():
    if request.method == "POST":
        if request.form.get("answer") == TRIVIA[QUESTION_IDX]["correct_answer"] :
            return redirect(url_for("correct")) # return a 302 redirect to /correct
    return redirect(url_for('index'))

@APP.route("/correct")
def correct():
    getNextQuestion()
    return redirect(url_for("index"))

if __name__ == "__main__":
    resp = requests.get(URL).json()
    TRIVIA = resp["results"]

    APP.run(host="0.0.0.0", port=3000)
