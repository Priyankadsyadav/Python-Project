#Rock ,paper ,scissors:



import random 
choices=('r','p','s')
emojis ={'r':'🪨','p':'📜','s':'✂️'}

while True:

    user_choice = input("Rock,Paper,Scissors?(r/p/s) :").lower()
    if user_choice not in choices:
        print(f"{user_choice} is invalid")
        continue
    computer_choice=random.choice(choices)

    print(f'you chose {emojis[user_choice]}')
    print(f'computer chose {emojis[computer_choice]}')


    #determining the winner:

    if user_choice==computer_choice:
        print("Its a Tie")
    elif (user_choice=='r' and computer_choice=='s') or (user_choice=='s' and computer_choice=='p') or user_choice=='p' and computer_choice=='r' :
        print("you win")
    else:
        print("computer wins")


# ask the user if user wants to continue:

    should_continue = input('continue? y/n:')
    if should_continue=='n':
        break
print('Thanks for playing')


