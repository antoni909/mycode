#!/usr/bin/python3

import random
import requests
from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request

APP= Flask(__name__)
URL= "https://opentdb.com/api.php?amount=20&type=multiple"
IMG= "static/OPENTRIVIA_LOGO.png"
TRIVIA= []
QUESTION_IDX= 0
TOTALS= {"correct": 0, "incorrect":0}

def getNextQuestion():
    global QUESTION_IDX, TOTAL_CORRECT
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

def updateTotals(flag):
    if(flag == "correct"): TOTALS["correct"] += 1
    else: TOTALS["incorrect"] += 1 

@APP.route("/") 
def index():
    print("ANSWER ",TRIVIA[QUESTION_IDX]["correct_answer"])
    answers_list = getAnswersList()

    return render_template(
        "index2.html", img= IMG, 
        current_trivia = TRIVIA[QUESTION_IDX], 
        answers = answers_list, 
        length = len(answers_list),
        number_of_questions = len(TRIVIA),
        question_number = TOTALS["correct"] + TOTALS["incorrect"]
    )

@APP.route("/handle_resp", methods = ["POST", "GET"])
def handle_response():
    if request.method == "POST":
        if request.form.get("trivia") in TRIVIA[QUESTION_IDX]["correct_answer"]:
            getNextQuestion()
            updateTotals("correct")
    return redirect(url_for('index'))

if __name__ == "__main__":
    resp = requests.get(URL).json()
    TRIVIA = resp["results"]
    APP.run(host="0.0.0.0", port=3000)

