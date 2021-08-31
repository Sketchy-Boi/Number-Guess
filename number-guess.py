import random
# Any feedback at all on how to better my code would be greatly appreciated, since most of this work is more effort than actual knowledge

#Number guess function
#note: inputting any other data type that is not an integer will throw an error at you lol
def number_guess(tries):
    print("(This is my sorry attempt at a decent minigame.)")
    print(f"You have {tries} attempts to guess a randomly generated integer correctly.")
    random_number = random.randint(1,100)
    if random_number < 10:
        print("Your number is less than ten, Lucky! ")
    elif random_number <= 30 and random_number >= 10:
        print("Your number is somewhere in between 10 and 30 inclusive.")
    elif random_number <=60 and random_number >= 31:
        print("Your number is in between 31 and 60 inclusive.")
    elif random_number <=90 and random_number >= 61:
        print("Your number is in between 61 and 90 inclusive.")
    else:
        print("Your number is between 91 and 100, Lucky!")

    while tries > 0:
        user_guess = int(input("Your guess : "))
        tries = tries - 1
        if user_guess == random_number:
            print(f"Nice! You guessed the number correctly in {tries} tries!")
            break
        elif user_guess != random_number:
            print("Not quite! Try again.")
    else:
        print("You ran out of tries! Better Luck Next Time!")    
# You can change the amount of tries you want below           
number_guess(20)
    
