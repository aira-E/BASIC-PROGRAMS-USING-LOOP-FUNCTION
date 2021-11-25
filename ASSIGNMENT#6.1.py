# Addition Quiz
print ("Good day! This is our quiz for today!")
import random
question = {}
score = 0

for i in range (10):
    int_a = random.randint (0,99)
    int_b = random.randint (0,99)
    formula = int_a + int_b
    question = int (input (f" {int_a} + {int_b} = "))
    if question == formula:
        score += 1
        print ("Correct")
    else:
        print ("Incorrect")
print ("You got " + str (score) + " right answer/s, over 10 items")