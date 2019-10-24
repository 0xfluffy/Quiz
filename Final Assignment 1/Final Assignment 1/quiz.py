import json # Javascript Object Notation
import random

points = 0
print(" Welcome to Te Reo Māori Quiz")
print("You should answer questions in single māori word.")

# Gets the questions from a JSON file and returns the data in a Dictonary
def getQuiz():
    # Must use double slash or it wont work. For Windows must use utf-8
    # Opens the file data.json and loads the data into the dict data, after everthing is dumped then returns the dict
    #give the whole path where the file is stored so that program could collect the data from the file to run quiz
    with open('Path of the File', encoding='utf-8') as json_data:
        data = json.load(json_data)
    return data

def askQuestions(quiz):
    #Converts keys also known as questions to list so it can random without repeating, because a dictonary cannot be randomed with random.sample
    questionList = list(dict.fromkeys(quiz))
    # Calls random.sample on the list of questions, only randoms 5 questions uniqly
    uniqueQuestions = random.sample(questionList, 5)

    #Loops through the list of questions and checkAnswers is called for every questions asked. The function requires 3 necessary parameters
    #whole quiz dict, the user input and the questions asked
    for questionAsked in uniqueQuestions:
        userInput = input(questionAsked+" ")
        checkAnswers(quiz, userInput, questionAsked)

# THis function checks if the questios asked matched the any of the questions in the questions matches
def checkAnswers(quiz, userInput, questionAsked):
    #Loops through the entire quizz
    # First condtion: If the keys (questions in the entire quizz) match the random unique questionAsked AND the answer matches the userinput then correct and score points\
    global points
    for keys, value in quiz.items():
        if keys in questionAsked and value in userInput:
            print("Correct!")
            points +=1
            print("Your score is " + str(points))
        elif keys in questionAsked and value is not userInput:
            print("Incorrect, the correct answer is " + value)
            points -= 1
            print("Your score is " + str(points))

# This function calcuates the percentage, returns percentage.
def calculatePercentage():
    # Divided by 5 because that is how many questions there are/asked.
    # Multiply by 100 to get the percentage
    percentage = (points / 5) * 100
    if percentage <= 0:
        percentage = 0

    return percentage


def main():
    while(True):
        #calls the functions getQuizz to get the quizz questions from JSON file, returns dict
        quiz = getQuiz()
        #calls askQuestions to ask the questions and calculate them straight away
        askQuestions(quiz)
        #Calls the function to calculate percentage.
        p = calculatePercentage()
        #prints percentage
        print("Your final Percentage is: {}%".format(p))
        # Converts user input into an int so can compare with a number rather than string.
        userInput = int(input("Press 1 to play again press 2 to exit: "))
      # This global points starts to give score from the begining when you start quiz again
        global points
        points = 0

        # Breaks out of loop only if pressed 2 else forever loop used.
        if userInput == 2:
            break

if __name__ == '__main__':
    main()
