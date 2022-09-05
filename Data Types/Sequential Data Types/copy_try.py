# person1 = ['Ram', ["Chandol", "Kathmandu"]]
# person2 = person1.copy()
# person2[0] = 'Sita'
# print("Person1: ",person1)
# print("person 2", person2)
# print(id(person1))
# print(id(person2))
# person2[1][0] = "Dumbarahi"
# print("person 2", person2)
# print("Person1: ",person1)

#when we use copy(), we copy the references, this means both person variable is
#pointing to same nested list so when one changes the nested list it will be affected on
#other variable also

#deepcopy from module copy
from copy import deepcopy
person1 = ['Ram',["Chandol", "Kathmandu"]]
person2 = deepcopy(person1)
person2[0] = 'Sita'
person2[1][0] = "Sukedhara"
print("person 2", person2)
print("Person1: ",person1)

