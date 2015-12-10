import collections
try:
    collections.namedtuple('Person', 'name class age gender')
except ValueError as err:
    print(err)
    
try:
    collections.namedtuple('Person', 'name age gender age')
except ValueError as err:
    print(err)