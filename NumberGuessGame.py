import random

def game():
    guessed_no = random.randint(1, 100)
    attempts = 0
    
    for attempts in range(1, 30):
        guess = input("Enter the random no. in (0,100): ")
        
        try: #try guess is int. if true(if  guess is int then go to line 16,out of try except block. if guess is float then go to except.)
            guess = int(guess)    #try except block is to handle exceptions in code.
        except ValueError:        #try : is to handle exceptions and except is to handle errors in given error.
            print("Please enter an integer number.")
            break
        
        print("Number guessed by your system is:", guessed_no)
        attempts += 1
        
        if guess < guessed_no:
            print(f"Your guessed no {guess} is lower than {guessed_no}.\n")
        elif guess > guessed_no:
            print(f"Your guessed no {guess} is higher than {guessed_no}.\n")
        elif guess == guessed_no:
            print(f"Hurray! You have guessed the same no. {guess} in {attempts} attempts.\n")
            break
    else:
        print("Oops! You couldn't guess the number in 30 attempts.")

game()
