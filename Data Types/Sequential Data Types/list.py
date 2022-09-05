#Accessing list:
person = [["Marc", "Mayer"],
["17, Oxford Str", "12345", "London"],
"07876-7876"]
name = person[0]
first_name = person[0][0]

#changing list item
languages = ["Python", "C", "C++", "Java", "Perl"]
languages[4] = 'Lisp'

#appending item in list
languages.append('Javascript')

#adding element at specific index
languages.insert(1, 'Golang')

#adding another list to current list
lst = [12,13,14]
lst2 = [21,22]
lst.append(lst2) # [12,13,14, [21,22]]
#so we use extend method, arguement can be any iterable
lst.extend(lst2)  # [12,13,14,21,22]

#removing element from list without knowing position
lst.remove(13)

#finding position of element in list
colours = ["red", "green", "blue", "green", "yellow"]
colours.index("green")# o/p: 1
colours.index('green',2) #o/p: 3
colours.index('green', 3,4) # 3



#applications
#  We go to a virtual supermarket. Fetch a cart and start shopping:
shopping_list = ['milk','yoghurt', 'egg', 'butter', 'bread', 'bananas']
cart = []
while shopping_list != []:
    #'pop' removes last element of list and returns it
    article = shopping_list.pop()
    cart.append(article)


#membership testing:
abc = ["a","b","c","d","e"]
"a" in abc #return True
"a" not in abc #return False

