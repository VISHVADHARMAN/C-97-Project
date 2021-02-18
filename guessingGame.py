import random
chances = 0
number = random.randint(1,9)
print("Number Guessing Game")
while chances < 5:
    guess = int(input("Enter Your Guess Number: "))
    
    if (guess == number):
        print("Congratulation YOU Won!!!")
        break

    if (guess > number):
        print("Your Number Is Too High")
        
    if (guess < number):
        print("Your Number Is Too Low")


    chances = chances +1

if (not chances < 5 ):
    print("YOU LOSE!!! The number is ",number)