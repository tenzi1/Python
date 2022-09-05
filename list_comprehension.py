Celsius = [ 39.2, 36.5, 33.5, 35.9]
Fahrenheit = [ ((float(9)/5)*x +32) for x in Celsius]

#Pythagorean triple using list comprehension
[(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]

#________________________________________________________________________________________________
#Cartesian product (A x B)
colours = ["red", "green", "yellow", "blue"]
things  =["house", "car", "tree"]
coloured_things = [(x, y) for x in colours for y in things]
# print(coloured_things)

# _________________________________________________________________________________
#GENERATOR COMREHENSION
# uses () instead of [], same as list comprehension but returns generator instead of list

x = (x **2 for x in range(20))
#----------------------------------------------------------
#CALCULATION OF PRIME NUMBERS BETWEEN 1 AND 100 USING SIEVE OF ERATOSHENSE:

no_primes = [j for i in range(2, 9) for j in range( i*2, 100, i) ]

prmies = [x for x in range(2,100) if x not in no_primes]

#generalizing:
from math import sqrt
n = 100
sqrt_n = int(sqrt(n))
no_primes = [j for i in range(2, sqrt_n + 1) for j in range(i*2, n, i)]

#_____________________________________________________________________
#RECURSIVE FUNCTION TO CALCULATE THE PRIMES
def  primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
       
        no_p = {j for i in p for j in range(i*2, n+1, i)}
       
        p = {x for x in range(2, n+1) if x not in no_p}
     
       
    return p

for  i in range(1,50):
    print(i, primes(i))


