import random
print("Winning rules of the game ROCK PAPER SCISSORS are:\n Rock vs Paper -> Paper wins \n Rock vs Scissors -> Rock wins \n Paper vs Scissors -> Scissors wins")
while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    choice=int(input("Enter your choice: "))
    while choice>3 or choice<1:
        choice=int(input("enter a vailid choice: "))
    if choice==1:
        choice_name="rock"
    elif choice==2:
        choice_name="paper"
    elif choice==3:
        choice_name="scissor"
    print("user choice is: ", choice_name)
    print("now its computer turn")
    computer_choice=random.randint(1,3)
    if computer_choice==1:
        computer_choice_name="rock"
    elif computer_choice==2:
        computer_choice_name="paper"
    elif computer_choice==3:
        computer_choice_name="scissor"
    print("computer choice is: ", computer_choice_name)    
    print(choice_name, "vs", computer_choice_name)
    if choice==computer_choice:
        result="draw"
    elif (choice==1 and computer_choice==2) or (choice==2 and computer_choice==1): 
        result="paper"
    elif (choice==1 and computer_choice==3) or (choice==3 and computer_choice==1):    
        result="rock"
    elif (choice==2 and computer_choice==3) or (choice==3 and computer_choice==2):
        result="scissor"
    if result=="draw":
        print("....its a draw....")
    elif result=="choice_name":
        print("user wins")
    else:
        print("computer wins")
    print("Do you wanna play again(Y/N")
    ans=input().lower()
    if ans=="n":
        break
print("thanks for playing")            
    