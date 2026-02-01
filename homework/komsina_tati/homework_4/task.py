my_dict = {'tuple': (11, 12, 13, 14, 15), 'list': [21, 22, 23, 24, 25],
           'dict': {'a': 31, 'b': 32, 'c': 33, 'd': 34, 'e': 35}, 'set': {41, 42, 43, 44, 45}}
print(my_dict['tuple'][-1])
my_dict['list'].append(26)
my_dict['list'].pop(1)
my_dict['dict'][('i am a tuple',)] = '36'
my_dict['dict'].pop('a')
my_dict['set'].add(46)
my_dict['set'].pop()
