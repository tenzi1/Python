#used for working with underlying operating system.

import os

#GETTING CURRENT WORKING DIRECTORY
current = os.getcwd()
# print(current)
#_____________________________________

#CREATING A DIRECTORY
# os.mkdir(current + '\\' + "New")
#__________________________________________

#CHANGING CURRENT WORKING DIRECTORY
# os.chdir("New")
# print(os.getcwd())


#REMOVE DIRECTORY( EMPTY)
os.mkdir("New")
os.rmdir("New")


#LIST FILES AND SUB-DIRECTORY
print(os.getcwd())

print(os.listdir())
print(os.listdir("C:\\Users\\sherp\Desktop"))