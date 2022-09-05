#encapsulate the attribute with getter and setter
#but in simple case getter and setter doesn't do much
#so in case of change in implementation we use it


# in this case getter and setter has no special use
class P:
    def __init__(self, x):
        self.x = x 

    def get_x(self):
        return self.x 

    def set_x(self,x):
        self.x = x

# p = P(100)
# print(p.get_x())
# p.set_x(19)
# print(p.x)

#making attribute private and using getter and setter

class P1:
    def __init__(self, x):
        self.__x = x
    
    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        self.__x = x

# p1 = P1(42)
# print(p1.get_x())
# p1.set_x(50)
# print(p1.get_x())

#using public attribute there is no need to have getter and setter
#but there is no data encapsulation
class P2:
    def __init__(self, x):
        self.x = x
    
# p2 = P2(50)
# p2_new = P2(100)
# p2.x = p2.x + p2_new.x
# print(p2.x)


#when we need to change the implementation of x in above code

class P3:
    def __init__(self, x):
        self.set_x(x)
    
    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

# p3 = P3(1001)
# print(p3.get_x())

#if we use public attribute and remove all the methods interface would break 
#so we use @property to solve that

class P4:
    def __init__(self, x):
        self.x = x
    
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

#we can access the attribute by two ways in above class, but
# there should be only one way of accessing it

class P5:
    def __init__(self,x):
        self.__set_x(x)

    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        if x < 0:
            self.__x= 0
        elif x > 100:
            self.__x = 100
        else:
            self.__x = x
    x = property(__get_x, __set_x)

p5 = P5(40)
print(p5.x)
p5.x = 50
print(p5.x)
p5.__set_x(54)
print(p5.x)