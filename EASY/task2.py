# Initialize score 
score = 0 

# Ask first question 
answer = input("""1. What is the capital of France?
A) Berlin
B) Madrid
C) Paris
D) Rome
Your answer: """).upper() 
if answer == "C": 
    print("Correct!") 
    score += 1 
else: 
    print("Wrong! The correct answer is C.") 

# Ask second question 
answer = input("""\n2. Which planet is known as the Red Planet?
A) Earth
B) Mars
C) Jupiter
D) Venus
Your answer: """).upper() 
if answer == "B": 
    print("Correct!") 
    score += 1 
else: 
    print("Wrong! The correct answer is B.") 

# Ask third question 
answer = input("""\n3. What is the largest ocean on Earth?
A) Atlantic Ocean
B) Indian Ocean
C) Arctic Ocean
D) Pacific Ocean
Your answer: """).upper() 
if answer == "D": 
    print("Correct!") 
    score += 1 
else: 
    print("Wrong! The correct answer is D.") 

# Ask fourth question 
answer = input("""\n4. Who wrote 'Romeo and Juliet'?
A) William Shakespeare
B) Mark Twain
C) Charles Dickens
D) Jane Austen
Your answer: """).upper() 
if answer == "A": 
    print("Correct!") 
    score += 1 
else: 
    print("Wrong! The correct answer is A.") 

# Ask fifth question 
answer = input("""\n5. What is 5 + 7?
A) 10
B) 11
C) 12
D) 13
Your answer: """).upper() 
if answer == "C": 
    print("Correct!") 
    score += 1 
else: 
    print("Wrong! The correct answer is C.") 

# Final score 
print("\nYour final score out of 5:", score)