import random
import os
import json

# empty dictionaries to add the q's and a's in proposal.md
general = {}
pop_culture = {}
sports = {}
animals = {}
line_number = 1
question = None
answer = None

# writes the q's and a's to keys and values in the dictionary of their corresponding topic
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

# tracks which questions are answered right and wrong
questions_answered_right = []
questions_answered_wrong = []

# Check if the file exists.
if os.path.isfile("flashcards_data.json"):
    with open("flashcards_data.json","r") as f:
        quiz_data = json.load(f)
else:
    # If it doesn't, make an empty dictionary called quiz_data
    quiz_data = {}

# username = input("What is your username? ")

# general_questions= list(general.keys())
# pop_culture_questions= list(pop_culture.keys())
# sports_questions= list(sports.keys())
# animals_questions= list(animals.keys())

# directs you to trivia of the topick you choose

def main():
    choice = (input("Its time for ... TRRRRRIVIA!!! What category of trivia do you want? The options are General, Pop Culture, Sports, Animals \n"))
    print(choice)
    print("test1")
    if choice == "general":
        print("a")
        quiz("general", general)
    elif choice == "pop culture":
        print("b")
        quiz("pop culture", pop_culture)
    elif choice == "sports":
        print("c")
        quiz("sports", sports)
    elif choice == "animals":
        print("d")
        quiz("animals", animals)

# asks the questions in random order, and tells you if you answered correctly, then appends questions_answered_right and questions_answered_wrong
def quiz(category, choice):
    print("test2")
    global questions_answered_right
    global questions_answered_wrong
    global quiz_data
    global general
    global pop_culture
    global sports
    global animals
    random_questions = list(choice.keys())
    random.shuffle(random_questions)
    if category not in quiz_data:
        quiz_data[category]={}
    for random_question in random_questions:
        user_answer = input((random_question) + " ")
        if random_question not in quiz_data[category]:
            quiz_data[category][random_question]=[0,0,0,0]
        if user_answer == (choice[random_question]).lower():
            print("yay! you answered correctly!")
            questions_answered_right.append(random_question)
            quiz_data[category][random_question][0] += 1
            quiz_data[category][random_question][2] += 1
        elif user_answer != ((choice[random_question])).lower():
            print("oh no ... better luck next time")
            questions_answered_wrong.append(random_question)
            quiz_data[category][random_question][1] += 1
            quiz_data[category][random_question][3] += 1
    def sum_stats():
        global questions_answered_right
        global questions_answered_wrong
        global quiz_data
        global general
        global pop_culture
        global sports
        global animals
        with open("flashcards_data.json","w") as f:
            json.dump(quiz_data, f)
        with open("flashcards_data.json", "r") as f:
            json.load(f)
        single_right = 0
        single_wrong = 0
        total_right = 0
        total_wrong = 0
        for question in quiz_data[category]:
            single_right += int(quiz_data[category][question][0])
            single_wrong += int(quiz_data[category][question][1])
            total_right += int(quiz_data[category][question][2])
            total_wrong += int(quiz_data[category][question][3])
        
        print(f"Good job!!! This time you answered {single_right}/20 questions correctly in the category {category}")
        print(f"In total, you answered {total_right}/20 questions correctly in the category {category}")
    sum_stats()
    # Write the `data` variable to the file "flashcards_data.json"
    for random_question in random_questions:
        quiz_data[category][random_question][0] = 0
        quiz_data[category][random_question][1] = 0
    with open("flashcards_data.json","w") as f:
        json.dump(quiz_data, f)

# runs the code
main()

