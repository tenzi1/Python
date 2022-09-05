def f():
    def g():
        print("hi this is 'g' ")
        print('thanks for calling me ')
    
    print("This is function 'f' ")
    print("I am calling 'g' now ")
    g()

# f()
# _____________________________________________
def temprature(t):
    def celsius2fahrenheit(x):
        return  9 * x / 5 + 32

    result = "It's " + str(celsius2fahrenheit(t)) + "degrees"

    return result
# print(temprature(20))
# ____________________________________________________

#we can pass 'reference to object' as parameter to function.
#and since function is also object, we can pass reference to that function
#as parameter to another function
def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")

def f(func):
    print("Hi, it's me 'f' ")
    print("I will call 'func' now ")
    func()
    print("func's real name is " + func.__name__)

# f(g)
# _______________________________________________________________________

import math

def foo(func):
    print("The function " + func.__name__ + "was passed to foo")
    res = 0
    for x in [1,2,2.5]:
        res  += func(x)
    return res

# print(foo(math.sin))
# print(foo(math.cos))

# _______________________________________________________________
#output of function is also reference to object, so function can return reference to objects
def f(x):
    def g(y):
        return y + x + 3
    return g 

nf1 = f(1)
nf2 = f(2)

# print(nf1(1))
# print(nf2(1))
# 

# ___________________________________________________________________________
def greeting_func_gen(lang):
    def costomized_greeting(name):
        if lang == "de":
            phrase = "Guten Morgen"
        elif lang == "fr":
            phrase = "Bonjour"
        elif lang == "it":
            phrase = "Buongiorno"
        elif lang == "nep":
            phrase = "Namaste"
        else:
            phrase = "Hi"
        return phrase + " " + name + "!"
    return costomized_greeting

# say_hi = greeting_func_gen("nep")
# print(say_hi("Tshering"))

# __________________________________________________________________________________________
#function to generate polynomial of degree two
# def polynomial_creator(a,b,c):
#     def polynomial(x):
#         return a * x**2 + b * x + c
#     return polynomial

# p1 = polynomial_creator(2,3,-1)
# p2 = polynomial_creator(-1,2,1)

# for x in range(-2,2,1):
#     print(x, p1(x), p2(x))

#generalizing above equation 

# def polynomial_creator(*coefficients):
#     """coefficients are in the form a_n, ..., a_1, a_0"""
#     def polynomial(x):
#         res = 0
#         for index, coeff in enumerate(coefficients[::-1]):
#             res += coeff * x** index
#         return res
#     return polynomial
    
# p1 = polynomial_creator(4)
# p2 = polynomial_creator(2, 4)
# p3 = polynomial_creator(1, 8, -1, 3, 2)
# p4 = polynomial_creator(-1, 2, 1)

# for x in range(-2,2,1):
#     print(x, p1(x), p2(x), p3(x), p4(x))

# _______________________________________________________________________________________
#SIMPLE DECORATOR
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("after calling " + func.__name__)
    return function_wrapper

def foo(x):
    print("Hi, foo has been called with " + str(x))

# print("We call foo before decoration:")
# foo("Hi")

# print("We now decorate foo with f:")
# foo = our_decorator(foo)

# print("We call foo after decoration")
# foo(42)

# -___________________________________________________________________
#PROPER DECORATION
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hello, foo has been called with " + str(x))

# foo("hi")

# _____________________________________________________________________________
#we can decorate third party function but we cannot use python @ syntax
from math import sin, cos

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

sin = our_decorator(sin)
cos = our_decorator(cos)

# for f in [sin, cos]:
    # f(3.1315)
# ____________________________________________________________________________

# GENERALIZZED VERSION :
from random import random, randint, choice

def our_decorator(func):
    def function_wrapper(*args, **kwargs):
        print("Before calling " + func.__name__)
        res = func(*args, **kwargs)
        print(res)
        print("After calling " + func.__name__)

    return function_wrapper

random = our_decorator(random)
randint = our_decorator(randint)
choice = our_decorator(choice)


# ________________________________________________________________
# CHECKING ARGUMENTS WITH A DECORATOR
def argument_test_natural_number(func):
    def helper(x):
        if type(x) == int and x > 0:
            return func(x)
        else:
            raise Exception("Argument is not an integer")

@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n -1)

# ________________________________________________________________________
#COUNTING FUNCTION CALLS WITH DECORATORS
def call_counter(func):
    def helper(x):
        helper.calls += 1
        return func(x)

    helper.calls = 0
    return helper

@call_counter
def succ(x):
    return x + 1

# print("Number of calls ",succ.calls)
# for i in range(10):
#     succ(i)

# print("Number of calls ",succ.calls)
# __________________________________________________________________________________________
#DECORATORS WITH PARAMETERS
#decorating for evening expresion
def evening_greeting(func):
    def function_wrapper(x):
        print("Good evening, " + func.__name__ + " returns:")
        return func(x)
    return function_wrapper

#decorating for morning expression:
def morning_greeting(func):
    def function_wrapper(x):
        print("Good Morning, " + func.__name__ + " returns:")
        return func(x)
    return function_wrapper

@evening_greeting
def foo(x):
    print(10)

# foo("hi") 

print("Its morning")
@morning_greeting
def foo(x):
    print(6)

# foo('hi')

#both of above decorators are similar.So we can add parameter to the 
# decorator to be capable of customizing the greeting, when we do the decoration.
# We have to wrap function around our previous decorator function to accomplish this.
def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return function_wrapper
    return greeting_decorator

# @greeting("Good Morning")
# def foo(x):
#     print(10)

# foo('hi') 
# @greeting("Good Evening")
# def foo(x):
#     print(10)

# foo('hi') 
#___________________________________________________________________________________________
# USING WRAPS FROM FUNCTOOLS
# After decoration fo function it looses '__name__', '__doc__' adn __module__ attributes
from greeting_decorator import greeting

@greeting
def f(x):
    """ just some silly function """
    return x + 4

# f(10)
print("function name: " + f.__name__) #function name: function_wrapper
print("docstring: " + f.__doc__) #     docstring: function wrapper of greeting
print("module name: " + f.__module__) # module name: greeting_decorator

#------------------------------------------------------------------------
from greeting_decorators_manually import greeting
@greeting
def f(x):
    """ just some silly function """
    return x + 4

# f(10)
print("function name: " + f.__name__) #function name: f
print("docstring: " + f.__doc__) #     docstring: just some silly function
print("module name: " + f.__module__) # module name: __main__
#_________________________________________________________
from functools import wraps
def greeting(func):
    @wraps(func)
    def function_wrapper(x):
        """function_wrapper of greeting"""
        print("Hi, " + func.__name__ + " returns:")
        return func(x)
    return function_wrapper
