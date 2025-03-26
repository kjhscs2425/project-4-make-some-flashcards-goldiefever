# Write your code here
import random

general = {}
pop_culture = {}
sports = {}
animals = {}
line_number = 1
question = None
answer = None
with open ("proposal.md", "r") as f:
    for line in f:
        if line_number >= 3 and line_number <= 61:
            g = general
            if line[0]=="Q":
                question = line[2:-1]
            if line[0]=="A":
                answer = line[2:-1]
                g[question] = answer
        if line_number >=65 and line_number <= 123:
            p = pop_culture
            if line[0]=="Q":
                question = line[2:-1]
            if line[0]=="A":
                answer = line[2:-1]
                p[question] = answer
        if line_number >= 127 and line_number <=186 :
            s = sports
            if line[0]=="Q":
                question = line[2:-1]
            if line[0]=="A":
                answer = line[2:-1]
                s[question] = answer
        if line_number >=190 and line_number <=248 :
            a = animals
            if line[0]=="Q":
                question = line[2:-1]
            if line[0]=="A":
                answer = line[2:-1]
                a[question] = answer
        line_number +=1

questions_answered_right = []
questions_answered_wrong = []

general_questions= list(general.keys())
pop_culture_questions= list(pop_culture.keys())
sports_questions= list(sports.keys())
animals_questions= list(animals.keys())
random_general_questions = random.sample()
random_pop_culture_questions =
random_sports_questions =
random_animals_questions =
choice = input("Its time for ... TRRRRRIVIA!!! What category of trivia do you want? General(g), Pop Culture(p), Sports(s), Animals(a)")
if choice == "g":
    for quesion, answer in general:



