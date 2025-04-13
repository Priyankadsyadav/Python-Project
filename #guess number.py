#guess number 

import random 

choice = random.randint(1,100)
while True:
    try:
        guess=int(input("Guess the number between 1 and 100 :"))
        if guess < choice:
             print('Too Low!')
        elif guess>choice:
             print('Too high')
        else:
            print('Congragulations! you guessed the number ')
            break
    except ValueError:
        print('please send a valid number')
