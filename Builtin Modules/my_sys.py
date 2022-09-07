#SYS module provides function and variables used to manipulate different parts 
#of the python runtime environment.

#sys.argv ==> returns list of command line arguements passed to python script.
#first value is always name of script

import sys
print("You entered: ", sys.argv[1], sys.argv[2], sys.argv[3] )
#_____________________________________________________________________________________________

#sys.exit -> causes script to exit back to either python console or the cmd prompt
#generally used to safely exit from the program in case of exception

# print("exception occured")
# sys.exit()
# print("back to cmd")
#______________________________________________________________________

#sys.maxsize -> returns largest integer a variable can take
print(sys.maxsize)
#______________________________________________________________

#sys.path -> env variable that is search path for all python  modules
sys.path
#__________________________________________________________________________

#sys.version -> attr displays a string containing the version number
#current python interpreter
print(sys.version)
