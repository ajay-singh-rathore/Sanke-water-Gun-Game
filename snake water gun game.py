import random
list=['s' ,'w','g']

chances=10
no_of_chances=0
computer_point=0
player_point=0

print("\t \t \t Snake - Water - Gun \t \t \t ")
print("s for snake \n"
      "w W for Water \n"
      "g G for Gun \n")

while no_of_chances<chances:
    player=input("Snake , Water , Gun : ")
    comp=random.choice(list)

    if player==comp:
        print("Match Tie Both have 0 Points ")

    # if user choose s
    elif player=='s' and comp=='g':
        computer_point=computer_point+1
        print(f"Your Guess is {player}  and computer Guess is {comp}")
        print("Computer won 1 Point You lost \n")
        print(f"Computer point {computer_point} and Your point {player_point}")

    elif player=='s' and comp=='w':
        player_point=player_point+1
        print(f"Your Guess is {player}  and computer Guess is {comp}")
        print("You won 1 point computer lost\n")
        print(f"Computer point {computer_point} and Your point {player_point}")


    # if user choose w
    elif player=='w' and comp=='g':
        player_point=player_point+1
        print(f"Your Guess is {player}  and computer Guess is {comp}")
        print("You won 1 point computer lost\n")
        print(f"Computer point {computer_point} and Your point {player_point}")
    
    elif player=='w' and comp=='s':
        computer_point=computer_point+1
        print(f"Your Guess is {player}  and computer Guess is {comp}")
        print("Computer won 1 point You lost\n")
        print(f"Computer point {computer_point} and Your point {player_point}")
        
    #if user choose g
    elif player=='g' and comp=='s':
        player_point=player_point+1
        print(f"Your Guess is {player}  and computer Guess is {comp}")
        print("You won 1 point computer lost\n")
        print(f"Computer point {computer_point} and Your point {player_point}")

    elif player == 'g' and comp == 'w':
        computer_point = computer_point + 1
        print(f"Your Guess is {player}  and computer Guess is {comp}")
        print("Computer won 1 point You lost\n")
        print(f"Computer point {computer_point} and Your point {player_point}")

    else:
        print("Wrong guess \n")
    no_of_chances = no_of_chances + 1
    print(f"{chances - no_of_chances} is left out of {chances} \n")

if computer_point>player_point:
    print(" 😞 Computer won the Match 😞")

elif computer_point<player_point:
    print("🥳 You won the Match 🥳 ")

else:
    print("Match tie")

print(f"THe point of Computer is {computer_point} and Your point is  {player_point}")



        
        




