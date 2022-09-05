#creating dict
marks = {
    'Math': 88,
    "Science": 80,
    "Chemistry": 75
}

# marks['key'] use to access the value

#adding another item in dict
marks['Physics'] = 90

#only immutable data type can be key of dict
# dic = {[1,2]:"abc", } #gives error 'unhashable type'
# print(dic)

new_dic = {(1,2):"abc", 3.145:"pi"}
# print(new_dic)

#OPERATIONS IN DICTIONARIES
days = {'1':"Sunday",
        '2':"Monday",
        '3':"Tuesday",}

# len(days) returns the number of stored entries
# print(len(days))

#del d[k] deletes the key k with its value
# del days['2']
# print(days)

#membersip testing
# print('2' in days)
# print(2 in days)
# print('2 ' not in days)

#Methods 
#removing key value from dict
d = {1:'one', 2:'two', 3:'three'}
# one = d.pop(1)
# print(d,one)

#if key is not found keyerror is raised so use dict.pop(key, default)
# four = d.pop(4,'four')
# print(four)

#popitem() return (key, value) pair as 2-tuple
# two = d.popitem()
# print(two)

#when accessing key which doesn't exist we'll get error message
#1 so use "in" operator
# i = 6
# if i in d:
#     print(d[i])
# else:
#     print(str(i) +'is not in d')
#2 use .get() which doesn't raise error

# value = d.get(6)
# print(value)


#IMPORTANT METHODS:

#COPY() == shallow copy
words = {'house': 'Haus', 'cat': 'Katze'}
w = words.copy()
words["cat"] = "chat"
# print(w)
# print(words)

trainings = { "course1":{"title":"Python Training Course for Beginners",
"location":"Frankfurt",
"trainer":"Steve G. Snake"},
"course2":{"title":"Intermediate Python Training",
"location":"Berlin",
"trainer":"Ella M. Charming"},
"course3":{"title":"Python Text Processing Course",
"location":"München",
"trainer":"Monica A. Snowdon"}
}

trainings2 = trainings.copy()

trainings["course2"] = {"title": "Perl Seminar for Beginners",
"location": "Ulm",
"trainer": "James D. Morgan"}

# trainings["course2"]['title'] = "Advanced Python training"
# print(trainings['course2'])
# print(trainings2['course2'])

#CLEAR() == dictionary is not deleted, contents of dict is cleared
words = {'house': 'Haus', 'cat': 'Katze'}
words.clear()

#UPDATE(): merges the keys and values of one dictionary into another,
#overwriting value of same key:

knowledge = {'Frank': {'Perl','Javascript'}, "Monica":{'C','C++'}}
knowledge2 = {'Ram': {"Python"}, 'Frank':{'Perl', 'Python'}}
knowledge.update(knowledge2)
# print(knowledge)

#Iterating over dictionary
d = {'a':123, 'b':34, 'c':304}
# for key in d:
#     print(key)

# #or using keys()
# for key in d.keys():
#     print(key)
# #for iterating over values
# for value in d.values():
#     print(value)

# print(d.keys(), d.values())
# print(type(d.keys()))

# for k,v in d.items():
#     print(k,v)



# CONNECTING BETWEEN LISTS AND DICTIONARY
#LISTS FROM DICTIONARIES
#using keys(), values() and keys()

w = {"house": "Haus", "cat": "", "red": "rot"}
items_view = w.items()
items = list(items_view)

#or 
keys_view = w.keys()
keys = list(keys_view)
#or
values_view = w.values()
values = list(values_view)

#TURN LISTS INTO DICTIONARY
dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]
country_specialites_iterator = zip(countries,dishes)
country_specialities = list(country_specialites_iterator)
# print(country_specialities)
country_specialities_dict = dict(country_specialities)
# print(country_specialities_dict)

# for country, dish in zip(countries,dishes):
#     print(country, dish)


my_dict = dict(zip(countries, dishes))
# print(my_dict)

l1 = ["a","b","c"]
l2 = [1,2,3]
# c = zip(l1, l2)
# for i in c:
#     print(i)

#we have to keep in mind that iterators exhaust themselves
c = zip(l1,l2)
z1 = list(c)
z2 = list(c)
# print(z1) #[('a', 1), ('b', 2), ('c', 3)]
# print(z2) #[]



#Exercise:
def dict_merge_sum(d1, d2):

    
    for key, value in d2.items():
        if key in d1:
            d1[key] += value
        else:
            d1[key] = value
    merged_sum = d1.copy()
    return merged_sum
d1 = dict(a=4, b=5, d=8)
d2 = dict(a=1, d=10, e=9)
merge = dict_merge_sum(d1, d2)
# print(merge)
#or 
def dict_sum(d1,d2):
    return {k:d1.get(k,0) + d2.get(k, 0) for k in set(d1) | set(d2)}
d1 = dict(a=4, b=5, d=8)
d2 = dict(a=1, d=10, e=9)
# print(dict_merge_sum(d1, d2))


#----------------------------------------------
supermarket = { "milk": {"quantity": 20, "price": 1.19},
"biscuits": {"quantity": 32, "price": 1.45},
"butter": {"quantity": 20, "price": 2.29},
"cheese": {"quantity": 15, "price": 1.90},
"bread": {"quantity": 15, "price": 2.59},
"cookies": {"quantity": 20, "price": 4.99},
"yogurt": {"quantity": 18, "price": 3.65},
"apples": {"quantity": 35, "price": 3.15},
"oranges": {"quantity": 40, "price": 0.99},
"bananas": {"quantity": 23, "price": 1.29}}

def calc_cost():
    total_price = 0
    for article in supermarket:
        
        
        quatity = supermarket[article]['quantity']
        price = supermarket[article]['price']
        total_price += quatity * price 
    return total_price

cost = calc_cost()
print(cost)

# print(supermarket['milk']['quantity'] * supermarket['milk']['price'])