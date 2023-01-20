#!/usr/bin/env python3

# create a script that includes the trivia dictionary below.

# Use the html library to render the question/answers in the proper format.
import html

# Slice and print out the trivia question and the four answers (one correct, three incorrect) from the dictionary.
trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

question = trivia["question"]
answer = trivia["correct_answer"]
incorrect_answers = trivia["incorrect_answers"]


print(question)
print(incorrect_answers)

# have the user answer A, B, C, or D and see if they guess the answer correctly

