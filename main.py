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

# Check if the file exists.
if os.path.isfile("flashcards_data.json"):
    with open("flashcards_data.json","r") as f:
        quiz_data = json.load(f)
else:
    # If it doesn't, make an empty dictionary called quiz_data
    quiz_data = {}

username = input("What is your username? ")

# general_questions= list(general.keys())
# pop_culture_questions= list(pop_culture.keys())
# sports_questions= list(sports.keys())
# animals_questions= list(animals.keys())

# directs you to trivia of the topick you choose

def main():
    global username
    choice = (input("Its time for ... TRRRRRIVIA!!! What category of trivia do you want? The options are General, Pop Culture, Sports, Animals \n"))
    if choice == "general":
        quiz("general", general, username)
    elif choice == "pop culture":
        quiz("pop culture", pop_culture, username)
    elif choice == "sports":
        quiz("sports", sports, username)
    elif choice == "animals":
        quiz("animals", animals, username)

# asks the questions in random order, and tells you if you answered correctly, then appends questions_answered_right and questions_answered_wrong
def quiz(category, choice, user):
    global quiz_data
    # with open ("flashcards_data.json","r") as f:
    #     #READ THE FILE TO KNOW WHAT BOX  EACH Q IS IN!!!

    random_questions = list(choice.keys())
    weights=[]
    questions_asked =[]

    def box_to_weight(box_num):
        global weight
        if box_num == 1:
            return 8
        if box_num == 2:
            return 4
        if box_num == 3:
            return 2
        if box_num == 4:
            return 1
        if box_num == 5:
            return 0
        
    # Ensure user exists in quiz_data
    if user not in quiz_data:
        quiz_data[user] = {}

    # Ensure category exists in quiz_data[user]
    if category not in quiz_data[user]:
        quiz_data[user][category] = {}

    # Initialize weights based on the box number
    for random_question in random_questions:
        # Ensure that quiz_data[user][category][random_question] exists
        if random_question not in quiz_data[user][category]:
            quiz_data[user][category][random_question] = [0, 0, 0, 0, 1]  # default [correct, wrong, total correct, total wrong, box number]
        
        box = quiz_data[user][category][random_question][4]  # Access the box number
        weight = box_to_weight(box)
        weights.append(weight)
    
    random.shuffle(random_questions)

    # Loop through the questions and ask them
    for random_question in range(len(random_questions)):
        selected_question = random.choices(random_questions, weights=weights, k=1)[0]
        questions_asked.append(selected_question)
        user_answer = input((selected_question) + " ")
        if user_answer.lower == (choice[selected_question]).lower():
            print("yay! you answered correctly!")
            quiz_data[user][category][selected_question][0] += 1
            quiz_data[user][category][selected_question][2] += 1
            if quiz_data[user][category][selected_question][4] <= 4:
                quiz_data[user][category][selected_question][4] += 1
        elif user_answer != ((choice[selected_question])).lower():
            print("oh no ... better luck next time")
            quiz_data[user][category][selected_question][1] += 1
            quiz_data[user][category][selected_question][3] += 1
            quiz_data[user][category][selected_question][4] = 1
    def sum_stats():
        global quiz_data
        with open("flashcards_data.json","w") as f:
            json.dump(quiz_data, f)
        with open("flashcards_data.json", "r") as f:
            json.load(f)
        category_single_right = 0
        category_single_wrong = 0
        category_total_right = 0
        category_total_wrong = 0
        total_right = 0
        total_wrong = 0
        for question in quiz_data[user][category]:
            category_single_right += int(quiz_data[user][category][question][0])
            category_single_wrong += int(quiz_data[user][category][question][1])
            category_total_right += int(quiz_data[user][category][question][2])
            category_total_wrong += int(quiz_data[user][category][question][3])
            if "general" in quiz_data[user]:
                    total_right += quiz_data[user]["general"][question][2]
            if "pop culture" in quiz_data[user]:
                    total_right += quiz_data[user]["pop culture"][question][2]
            if "sports" in quiz_data[user]:
                    total_right += quiz_data[user]["sports"][question][2]
            if "animals" in quiz_data[user]:
                    total_right += quiz_data[user]["animals"][question][2]
            if "general" in quiz_data[user]:
                    total_wrong += quiz_data[user]["general"][question][3]
            if "pop culture" in quiz_data[user]:
                    total_wrong += quiz_data[user]["pop culture"][question][3]
            if "sports" in quiz_data[user]:
                    total_wrong += quiz_data[user]["sports"][question][3]
            if "animals" in quiz_data[user]:
                    total_wrong += quiz_data[user]["animals"][question][3]
        print(f"Good job {username}!!! This time you answered {category_single_right}/20 questions correctly in the category {category}")
        print(f"In total, you have answered {category_total_right} questions correctly in the category {category}, and {total_right} questions correctly overall")
    sum_stats()
    
    # Write the `data` variable to the file "flashcards_data.json"
    for random_question in random_questions:
        quiz_data[user][category][random_question][0] = 0
        quiz_data[user][category][random_question][1] = 0
    with open("flashcards_data.json","w") as f:
        json.dump(quiz_data, f, indent = 2)

# runs the code
main()

