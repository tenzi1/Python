import random, string
words = ['python', 'hello', 'java']

def get_valid_word(words):
    word = random.choice(words)
    while ('-' or '_' or ' ') in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))

        user_letter = input('Guess the letter:  ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            elif user_letter in used_letters:
                print('You have already used that character')
            else:
                print('Invalid character')

        print(len(word_letters))
    print('Correct word is :------', word)
            


hangman()
# def hangman():
#     word = get_valid_word(words)
#     word_letters = [*word]
#     used_letters = []
#     alphabet = [string.ascii_uppercase]
#     while len(word_letters) > 0:
#         word_list = [letter if letter in used_letters else '-' for letter in word]
#         print('Current word', ' '.join(word_list))
#         user_letter = input("Enter your letter").upper()
#         for letter in alphabet:
#             if letter not in used_letters:
#                 if letter == user_letter:
#                     if user_letter in word_letters:
#                         used_letters.append(user_letter)
#                         word_letters.remove(user_letter)
#             else:
#                 print('Try Again...')
#     print('The word is : ', word)

# hangman()



