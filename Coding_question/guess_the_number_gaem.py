import random
print(f"Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")
low=int(input("enter the starting number: "))
high=int(input("enter the ending number: "))   

print(f"you have 7 chances to guess from {low} to {high}\n lets begin")

num= random.randint(low,high)
total_chances=7
guessed=0

while guessed<total_chances:
    guessed+=1
    guess=int(input("guesss a random number: "))
    if guess == num:
        print(f"yes {num} is correct. you guessed it in {guessed} attempts ")
        break
    elif guessed == total_chances and guess != num:
        print(f"sorry the number was {num}\n better luck next time ")
    elif guess > num:
        print(f"too high! guess the lower num")
    elif guess < num:
        print(f"too low! guess the higher num")
