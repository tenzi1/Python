#"pickle module offers algorithms which we can use to serialize and de-serialize Python object structures"
#"pickling" is process which converts a Python object into byte stream
#"unpickling" is proceess which converts byte steam into python object

#pickle.dump(obj, file) => writes a pickle representation of obj to the open file object file.
#pickle.load() => reads object  which have been dumped to a file with pickle.dump


# import pickle

# cities = ["Paris", "Dijon", "Lyon", "Strasbourg"]
# fh = open("data.pkl", "bw")
# pickle.dump(cities, fh)
# fh.close()

# #reading pickled data
# f = open("data.pkl", "rb")
# villes = pickle.load(f)
# print(villes)

# ______________________________________________________________
#PICKLING MULTIPLE OBJECCTS
import pickle
fh = open("data.pkl", "bw")
programming_lang = ["Python", "Perl","C++","C", "Java"]
python_dialects = ["Jython","ironPython", "CPython"]
pickle_object = (programming_lang, python_dialects)
pickle.dump(pickle_object, fh)
fh.close()

#UNPICKLING OBJECT INTO MULTIPLE OBJ
f = open("data.pkl", 'rb')
language, dialects = pickle.load(f)
print(programming_lang, python_dialects)

# __________________________________________________________________________________
#pickle is only capable of pickling one object at the time which has to be unpickled in one go.
#if data object is dictionary, we have save and load whole dictionary everytime so it is not desirable to save
#and load single value.
#so we use SHELVE MODULE

#A "shelf" as used in shelve module is a persistet, dictionary like object.