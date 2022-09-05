# class Robot:
#     def __init__(self, name=None, build_year=None):
#         self.name = name
#         self.build_year = build_year

#     def say_hi(self):
#         if self.name:
#             print("Hi, I am " + self.name)
#         else:
#             print('Hi, I am robot without name')
        
#     def set_name(self, name):
#         self.name = name
    
#     def get_name(self):
#         return self.name

#     def set_build_year(self, build_year):
#         self.build_year = build_year

#     def get_build_year(self):
#         return self.build_year

# x = Robot()
# x.set_name('Henry')
# x.say_hi()
# y = Robot()
# y.set_name(x.get_name())
# print(y.get_name())
# x.set_build_year(1998)
# print(x.get_build_year())

# class A():
#     def __init__(self):
#         self.__priv = "I am private"
#         self._prot = "I am protected"
#         self.pub = "I am public"
# x = A()
# print(x.pub)
# print(x._prot)
# print(x.__priv)

# class Robot:

    
#     def __init__(self, name=None, build_year=None):
#         self.__name = name
#         self.__build_year = build_year

#     def say_hi(self):
#         if self.__name:
#             print("Hi, I am " + self.__name)
#         else:
#             print('Hi, I am robot without name')
        
#     def set_name(self, name):
#         self.__name = name
    
#     def get_name(self):
#         return self.__name

#     def set_build_year(self, build_year):
#         self.__build_year = build_year

#     def get_build_year(self):
#         return self.__build_year


# x = Robot()
# x.set_name('Henry')
# x.say_hi()
# y = Robot()
# y.set_name(x.get_name())
# print(y.get_name())
# x.set_build_year(1998)
# print(x.get_build_year())

# class Robot:
#     Three_Laws = (
# """A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
# """A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",
# """A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."""
# )
#     def __init__(self, name, build_year):
#         self.name = name
#         self.build_year = build_year

# for number, text in enumerate(Robot.Three_Laws):
#     print(str(number+1) + ":\n" + text)
    

# class C:
#     counter = 0

#     def __init__(self):
#         self.__class__.counter += 1

#     def __del__(self):
#         print('instance deleted')
#         type(self).counter -= 1
#         print(self.counter)


# print('Creating counter instance')
# c1 = C()
# print(c1.counter)
# print('Creating counter instance')
# c2 = C()
# print(c2.counter)
# print('Creating counter instance')
# c3 = C()
# print(c3.counter)

# del c1
# del c2
# del c3

# class Robot:
#     __counter = 0

#     def __init__(self):
#         type(self).__counter += 1
#     @staticmethod
#     def RobotInstances():
#         return Robot.__counter

# if __name__ == '__main__':
#     x = Robot()
#     print(x.RobotInstances())
#     y = Robot()
#     print(y.RobotInstances())

from multiprocessing.sharedctypes import Value


# class fraction:
#     def __init__(self, n, d):
#         self.numerator, self.denominator = fraction.reduce(n,d)
#     @staticmethod
#     def gcd(a,b):
#         while b != 0:
#             a, b = b, a%b
#             return a

    

    # @classmethod
    # def reduce(cls, n1, n2):
    #     g = cls.gcd(n1,n2)
    #     return (n1 // g, n2//g)


# class Pet:
#     _class_info = "pet animals"
#     @staticmethod
#     def about():
#         print("This class is about " + Pet._class_info + "!")   
# class Dog(Pet):
#     _class_info = "man's best friends"
# class Cat(Pet):
#     _class_info = "all kinds of cats"
# Pet.about()
# Dog.about()
# Cat.about()

class Pet:
    _class_info = "pet animals"
    @classmethod
    def about(cls):
        print("This class is about " + cls._class_info + "!")   
class Dog(Pet):
    _class_info = "man's best friends"
class Cat(Pet):
    _class_info = "all kinds of cats"
Pet.about()
Dog.about()
Cat.about()
