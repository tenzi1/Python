#_________MULTIPLE INHERITANCE_______________________________

from xmlrpc.client import FastMarshaller


class Clock:
    def __init__(self, hours, minutes, seconds):
        #the parameters must satisfy following conditions
        # 0 <= hours < 24
        # 0 <= minutes < 60
        # 0 <= seconds < 60

        self.set_Clock(hours, minutes, seconds)
    
    def set_Clock(self, hours, minutes, seconds):
        if type(hours) == int and 0 <= hours and hours < 24:
            self._hours = hours
        else:
            raise TypeError("Hours have to be integers between 0 and 23!")
        
        if type(minutes) == int and 0 <= minutes and minutes < 60:
            self.__minutes = minutes
        else:
            raise TypeError("Minutes have to be integers between 0 and 59!")
        
        if type(seconds) == int and 0 <= seconds and seconds < 60:
            self.__seconds = seconds
        else:
            raise TypeError("Seconds have to be integer between 0 and 59!")

    def __str__(self):
        # return  f"{self._hours}: {self.__minutes}:{self.__seconds}"
        return "{0:02d}:{1:02d}:{2:02d}".format(self._hours, self.__minutes, self.__seconds)

    def tick(self):
        """
        This method lets the clock "tick", this means that the internal time will be advanced by one second.
        
        """
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self._hours == 23:
                    self._hours = 0
                else:
                    self._hours += 1

            else:
                self.__minutes += 1
        else:
            self.__seconds += 1

# if __name__ == '__main__':
#     x = Clock(23,9,59)
#     print(x)
#     x.tick()
#     print(x)
#     y = str(x)
#     print(type(y))

# Calender implementation 

class Calender:
    months = (31,28,31,30,31,30,31,31,30,31,30,31)
    date_style = 'British'

    def __init__(self, d, m, y):
        """
        day, month and year has to be integer and year has to be 4 digit 
        """            
        self.set_Calender( d, m, y)

    def set_Calender(self,d,m,y):
        if type(d) == int and type(m) == int and type(y) == int:
            self.__days = d
            self.__months = m
            self.__year = y
        else:
            raise TypeError("d, m , y has to integers")


    @staticmethod
    def leapyear(year):
        """
        This method returns True if the parameter year is a leap year, False otherwise.
        """
        if not year % 4 == 0:
            return False
        elif not year % 100 == 0:
            return True
        elif not year % 400 == 0:
            return False
        else:
            return True

    def __str__(self):
        if Calender.date_style == "British":
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__days, self.__months,self.__year)
        else:
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__months, self.__days, self.__year)


    def advance(self):
        """
        This method advances to the next date.
        """

        max_days = Calender.months[self.__months-1]
        if self.months == 2 and Calender.leapyear(self.__year):
            max_days += 1
        if self.__days == max_days:
            self.__days = 1
            if self.__months == 12:
                self.__months = 1
                self.__year += 1
            else:
                self.months += 1
        else:
            self.__days += 1

# if __name__ == '__main__':
#     x = Calender(31,12,2022)
#     print(x,end=" ")
#     x.advance()
#     print("after applying advance: ", x)

class CalenderClock(Clock, Calender):
    """
    This class integrates Clock class with Calender class, it is the case of multiple inheritance.
    """
    def __init__(self,  day, month, year, hours, minutes, seconds):
        Clock.__init__(self,hours, minutes, seconds)
        Calender.__init__(self, day,month,year)

    def tick(self):
        """
        advance the clock by one second
        """
        previous_hour = self._hours
        Clock.tick(self)
        if (self._hours < previous_hour):
            self.advance()
        
    def __str__(self):
        return Calender.__str__(self) + ", " + Clock.__str__(self)

if __name__ == "__main__":
    x = CalenderClock(31,12,2013,23,59, 59)
    print("One tick from ", x, end = " ")
    x.tick()
    print("to ", x)        

