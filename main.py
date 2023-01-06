from Questions import Questions
from Ask import Ask
import time
from pprint import pprint


correctCount = 0
for question in Questions:
    count = Ask(question)
    if count:
        correctCount += 1
print(f"You got {correctCount}/{len(Questions)} correct!!")
