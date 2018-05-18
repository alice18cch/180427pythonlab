ages = {}
ages['bob'] = 9
ages['alice'] = 18


       
print(ages['bob'])       # 9
#print(ages.bob)           error: 'dict' object has no attribute 'bob'
print(ages.get('bob'))   # 9

#print(ages['john'])              KeyError: 'john'
print(ages.get('john'))         # None
print(ages.get('john', 'N/A'))  # 'N/A'
print(len(ages))                # 2
print(list(ages))               # ['bob', 'alice'], order may differ
print('bob' in ages)            # True
print('john' in ages)           # False


ages = { 'bob': 9, 'alice': 18 }
ages2 = dict({'bob': 9, 'alice': 18}) # same as ages
ages3 = dict(bob=9, alice=18)          # same as ages
ages4 = dict([('bob', 9), ('alice', 18)]) # same as ages