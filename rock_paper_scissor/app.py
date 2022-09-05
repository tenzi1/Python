'''
>random value for computer and input for user
> available values = {'r':'rock', 'p':'paper', 's':'scissor' }
> game logic = r > s , s > p and p > r

'''

import random

## raw way 
again = True
while again:
    again = False
    computer = random.choice(['r', 's', 'p'])
    
    user = input('Enter your choice ["r"="rock", "p"="paper", "s"="scissor"]    '  )

    if computer == user:
        print("It's draw... Again try")
        again = True

    elif computer == 'r' and user == 's' :
        print('Computer wins the game')
        

    elif computer == 's' and user == 'p':
        print('Computer wins the game')
        

    else:
        print('Congratulation User wins game....')
        


## Using Function 
def play():
    user = input("Enter your sign ('r'for 'rock', 's' for scissor and 'p' for paper):  ")
    computer = random.choice(['r','s','p'])

    if user == computer:
        return 'tie'

    return has_won(user, computer)

def has_won(player, host):
    if (player=='r' and host=='s') or (player=='s' and host =='p') or ( player=='p' and host=='r') :
        return 'User  won!!!'
    else:
        return "Host won !!!"


play()