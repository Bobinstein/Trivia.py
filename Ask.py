import time

def Ask(question):
    prompt = False

    while prompt not in ["A","B","C","D"]:
        print("\n\n",question["Question"])
        time.sleep(2)
        print(question["A1"])
        time.sleep(1)
        print(question["A2"])
        time.sleep(1)
        print(question["A3"])
        time.sleep(1)
        print(question["A4"])
        time.sleep(1)

        prompt = input("Answer (A/B/C/D): ").upper()
        if prompt not in ["A","B","C","D"]:
            print("please make a valid selection")
            time.sleep(2)
    answer = identifyAnswer(prompt)
    if answer == question["Correct"]:
        print("Correct!!")
        return True
    else:
        print("Sorry, the correct answer is: ", question[question["Correct"]])
        return False
def identifyAnswer( answer):

    if answer == "A":
        chosenAnswer = "A1"
    elif answer == "B":
        chosenAnswer = "A2"
    elif answer == "C":
        chosenAnswer = "A3"
    elif answer == "D":
        chosenAnswer = "A4"
    
    if chosenAnswer:
        return chosenAnswer
