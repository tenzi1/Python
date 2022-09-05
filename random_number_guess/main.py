import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
   
    while random_number != guess:
        guess = int(input(f'Guess the number between 1 and {x}:  '))

    print('Congratulations , You guessed it correctly!!!!')
        
guess(10)       

