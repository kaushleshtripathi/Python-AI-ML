import random 

# -------- variables --------
user_input = input("Guess a number: ")
print("user_input",user_input)

print(type(user_input))

user_input_int = int(user_input)

print(type(user_input_int))

my_var = 2

print(id(user_input_int))
print(id(my_var))

# -------- loops and conditions ----------
# -------- data structures --------
round = 0
total_round = 5
users = {"user1","user2","user3"}
score_board = {"user1":0,"user2":0,"user3":0}

def generateRandomNumber():
     random_number = 0
     try:
       random_number = random.randint(1,9)
     except Exception as e:
          random_number = 7  
     finally:
          return random_number

def verifyNumber(user_input,random_number):
    if user_input == 0:
            print("Please add a number between 1 to 9")
    else:
            if user_input == random_number:
                current_score = score_board.get(user)   
                score_board[user] = current_score + 1
            else:
                print("No match!!")   

while(round < total_round):
    random_number = generateRandomNumber()
    print("random number:",random_number)
    for user in users:
        user_input = input(f"{user} Guess a number: ")
        user_input_int = int(user_input)
        verifyNumber(user_input_int, random_number)
         
    round = round + 1        

print("final score board:",score_board)    





