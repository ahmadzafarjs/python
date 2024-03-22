import random
## Message for users to choose between 1 to 100
print("Choose a number between 1 to 100")
difficulty = input("Choose a difficulty: 'easy' or 'hard': ")
attempt = 10
if difficulty == "hard":
    attempt = 5
print(f"You have {attempt}")
    
random_number = round(random.random() * 100)

def guess():
    global attempt
    attempt -= 1
    user_input = int(input("Guess the number: "))
    if user_input == random_number:
        print("yes you get it")
        attempt = 0
    elif user_input > random_number:
        print("To High")
    elif user_input < random_number:
        print("to Low")
        
while attempt >= 1:
    print(f"your remaining attempts is: {attempt}")
    guess()