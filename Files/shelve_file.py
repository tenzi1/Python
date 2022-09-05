#pickle is only capable of pickling one object at the time which has to be unpickled in one go.
#if data object is dictionary, we have save and load whole dictionary everytime so it is not desirable to save
#and load single value.
#so we use SHELVE MODULE

#A "shelf" as used in shelve module is a persistet, dictionary like object.

import shelve

s = shelve.open("MyShelve")
s['street'] = 'Fleet Str'
s['city'] = 'london'
for key in s:
    print(key)

s.close()