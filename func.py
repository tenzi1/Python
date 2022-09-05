
#Encoding and decoding strings
import string
alphabet = string.ascii_uppercase

def caesar(txt, n, coded=False):
    """ returns coded or decoded text string"""
    result = ""
    for char in txt.upper():
        if char not in alphabet:
            result += char
        elif coded:
            result += alphabet[(alphabet.find(char) + n) % len(alphabet)]
        else:
            result += alphabet[(alphabet.find(char) - n) % len(alphabet)]
    return result

text = "abcd"
x = caesar(text,23, True)
# print(x)

#________________________________________
# import string
# shift = 3
# abc = string.ascii_uppercase + " .,-?!"
# abc_cipher = abc[-shift:] + abc[:-shift]

# def caesar (txt, shift):
#     """Encodes the text "txt" to caesar by shifting it 'shift' pos
#     itions """
#     new_txt=""
#     for char in txt.upper():
#         position = abc.find(char)
#         new_txt +=abc_cipher[position]
#     return new_txt
# n = 3
# x = caesar("Hello, here I am!", n)
# print(x)
# x = caesar("abcdefghijk", n)
# print(x)

#___________________________________________________________
import string
from random import sample

alphabet = string.ascii_letters
permutated_alphabet = sample(alphabet, len(alphabet))

encrypt_dict = dict(zip(alphabet, permutated_alphabet))
decrypt_dict = dict(zip(permutated_alphabet, alphabet))

def encrypt(text, edict):
    """Every chars of the text 'text' is mapped to the
    value of edict. Characters which are not keys of
    edict will not change"""
    res = ""
    for char in text:
        res = res + edict.get(char, char)
    return res

text = "Hello world"
ctext = encrypt(text, encrypt_dict)
# print(ctext + "\n")
# print(encrypt(ctext, decrypt_dict))

# list1 = [1, 2, 3, 4, 5, 6] 
# print('with list:', sample(list1, 3) )


#_______________________________________________________________________
#Text to Morse code conversion and reverse
latin2morse_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..',
'E':'.', 'F':'..-.', 'G':'--.','H':'....',
'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
'M':'--', 'N':'-.', 'O':'---', 'P':'.--.',
'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
'Y':'-.--', 'Z':'--..', '1':'.----',
'2':'...--',
'3':'...--', '4':'....-', '5':'.....', '6':'-....',
'7':'--...', '8':'---..', '9':'----.',
'0':'-----',
',':'--..--', '.':'.-.-.-', '?':'..--..',
';':'-.-.-',
':':'---...', '/':'-..-.', '-':'-....-',
'\'':'.----.',
'(':'-.--.-', ')':'-.--.-', '[':'-.--.-',
']':'-.--.-',
'{':'-.--.-', '}':'-.--.-', '_':'..--.-'}

#reversing the dictionary
morse2latin_dict = dict(zip(latin2morse_dict.values(), latin2morse_dict.keys()))

def txt2morse(txt, alphabet):
    morse_code = ""
    for char in txt.upper():
        if char == " ":
            morse_code += "  "
        else:
            morse_code += alphabet[char] + " "
    return morse_code

def morse2txt(txt, alphabet):
    res = ""
    mwords = txt.split("  ")
    for mword in mwords:
        for mchar in mword.split():
            res += alphabet[mchar]
        res += " "
    return res


# mstring = txt2morse("So what?", latin2morse_dict)
# print(mstring)
# print(morse2txt(mstring, morse2latin_dict))


# _______________________________________________
#program to calculate square root of number using Babylonian method

def calc_sqroot(num, eps=0.0000001):
    """Approximate the square root of num"""
    previous = 0
    new = 1
    while abs(new - previous) > eps:
        previous = new
        new = (previous + num/previous) / 2

    return new

print(calc_sqroot(4))