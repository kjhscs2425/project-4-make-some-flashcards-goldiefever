import random
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

# general_questions= list(general.keys())
# pop_culture_questions= list(pop_culture.keys())
# sports_questions= list(sports.keys())
# animals_questions= list(animals.keys())

# directs you to trivia of the topick you choose
def main():
    choice = input("Its time for ... TRRRRRIVIA!!! What category of trivia do you want? General(g), Pop Culture(p), Sports(s), Animals(a)")
    if choice == "g":
        quiz(general)
    if choice == "p":
        quiz(pop_culture)
    if choice == "s":
        quiz(sports)
    if choice == "a":
        quiz(animals)

# asks the questions in random order, and tells you if you answered correctly, then appends questions_answered_right and questions_answered_wrong
def quiz(topic):
    random_questions = (random.sample(list(topic.keys()), 20))
    for random_question in random_questions:
        user_answer = input((random_question) + " ")
        if user_answer == ((topic[random_question])).lower():
            print("yay! you answered correctly!")
            questions_answered_right.append(random_question)
        elif user_answer != ((topic[random_question])).lower():
            print("oh no ... better luck next time")
            questions_answered_wrong.append(random_question)
    print(f"Good job!!! You answered {len(questions_answered_right)} out 20 questions correctly.")

# runs the code
main()

