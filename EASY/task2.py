# Initialize score 
score = 0 
# Ask first question 
answer = input("1. What is the capital of France?\nA) 
Berlin\nB) Madrid\nC) Paris\nD) Rome\nYour answer: ").upper() 
if answer == "C": 
print("Correct!") 
score += 1 
else: 
print("Wrong! The correct answer is C.") 
# Ask second question 
answer = input("\n2. Which planet is known as the Red 
Planet?\nA) Earth\nB) Mars\nC) Jupiter\nD) Venus\nYour answer: 
").upper() 
if answer == "B": 
print("Correct!") 
score += 1 
else: 
print("Wrong! The correct answer is B.") 
# Ask third question 
answer = input("\n3. What is the largest ocean on Earth?\nA) 
Atlantic Ocean\nB) Indian Ocean\nC) Arctic Ocean\nD) Pacific 
Ocean\nYour answer: ").upper() 
if answer == "D": 
    print("Correct!") 
    score += 1 
else: 
    print("Wrong! The correct answer is D.") 
 
# Ask fourth question 
answer = input("\n4. Who wrote 'Romeo and Juliet'?\nA) William 
Shakespeare\nB) Mark Twain\nC) Charles Dickens\nD) Jane 
Austen\nYour answer: ").upper() 
if answer == "A": 
    print("Correct!") 
    score += 1 
else: 
    print("Wrong! The correct answer is A.") 
 
# Ask fifth question 
answer = input("\n5. What is 5 + 7?\nA) 10\nB) 11\nC) 12\nD) 
13\nYour answer: ").upper() 
if answer == "C": 
    print("Correct!") 
    score += 1 
else: 
    print("Wrong! The correct answer is C.") 
 
# Final score 
print("\nYour final score out of 5:",score)