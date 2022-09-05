#__call__ method provides object of class to be callable
class A:
    def __init__(self):
        print("An instance of A was initialized")

    def __call__(self, *args, **kwargs):
        print("Arguements are: ", args, kwargs)

# x = A()
# print("now calling the instance")
# x(3,4,x=11,y=12)
# _____________________________________________________________________
#WRITING FIBONACCI FUNCTION USING __call__ METHOD:

class Fibonacci:
    def __init__(self):
        self.cache = {}
    
    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.cache[n]

# fib = Fibonacci()
# for i in range(15):
#     print(fib(i), end=", ")


#_________________________________________________________________________________________________
#USING CLASS AS A DECORATOR
def decorator1(f):
    def helper(x):
        print('Decorating', f.__name__)
        f(x)
    return helper

@decorator1
def foo(x):
    print("inside foo()")
# foo('hi')

#same implementation using class
class decorator2:
    def __init__(self, f):
        self.f = f
    
    def __call__(self):
        print("Decorating", self.f.__name__)
        self.f()
    
@decorator2
def foo():
    print("inside foo() ")
foo()