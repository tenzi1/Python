from re import X


def city_generator():
    yield("Kathmandu")
    yield("Pokhara")
    yield("Dharan")
    yield("Butwal")
    yield("Janakpur")

#we create iterator by calling city_generator()
city = city_generator()
# print(city, type(city))
# print(next(city))
# print(next(city))

# _________________________________________________
def count(firstval=0, step=1):
    x = firstval
    while True:
        yield x
        print("yeild is encounterd")
        x += step
counter = count()
print(next(counter))
print(next(counter))
# for i in range(10):
#     print(next(counter), ", ")