#Recursion is a method where the solution to a problem is based on solving
# smaller instances of the same problem.

# example1: Factorial

def factorial(n):
    print("factorial has been called with n = " + str(n))

    if n == 0:
        return 1
    else:
        res =  n * factorial(n-1)
        print("intermediate result for ", n, "* factorial(", n-1, "):", res)
        return res
print(factorial(5))


#______________________________
#iterative factorial
def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i

#_________________________________________
#FIBONACCI NUMBERS
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# iterative approach

def fibi(n):
    old, new  = 0,1
    if n == 0:
        return 0
    for i in range(n-1):
        old, new = new, old+new
    return new
