#lambda arguement_list: expression

sum = lambda x,y : x + y
print(sum(3,5))

#map(func, seq)

def fahrenheit(T):
    return ((float (9) /5) * T + 32)

def celsius(T):
    return (float (5)/9) * (T - 32)

temperatures = (36.5, 37, 37.5, 38, 39)
F = map(fahrenheit, temperatures)
C = map(celsius, F)
temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))

# print(temperatures_in_Fahrenheit)
# print(temperatures_in_Celsius)

#____________________________________________________________________________________________
#using lambda with map
F = list(map(lambda x: (float (9) /5) *x + 32, temperatures))
C = list(map(lambda x: (float (5) /9) * (x - 32), F))
# _____________________________________________________________________
a = [1, 2, 3, 4,5]
b = [17, 12, 11]
c = [-1, 9]

result = list(map(lambda x,y,z: x + y + z, a,b,c))
# print(result)
# _________________________________________________________________________

from  math import sin, cos, tan, pi
def map_functions(x, functions):
    res = []
    for func in functions:
        res.append(func(x))
    return res
family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))
# ________________________________________________________________________
#EQUIVALENT LIST COMPREHENSION
def map_functions(x, functions):
    return [func(x) for func in functions]

# _______________________________________________________________________
#FILTERING FILTER(function, sequence)
#offers eleant way to filter out all the elements of "sequence", for which the function 'function' 
#returns True

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_number = list(filter(lambda x: x % 2 == 0, fibonacci))

even_numbers = list(filter(lambda x: x % 2 == 1, fibonacci))

# ________________________________________________________________________________
#REDUCING LIST reduce(func,seq)
#continully applies the function func() to the sequence seq. It requires a single value
from functools import reduce
sum = reduce(lambda x,y: x+y, [1,2,3,4,5])

