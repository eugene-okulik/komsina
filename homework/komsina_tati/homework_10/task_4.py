PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

tuples_from_price_list = [
    (x.split()[0], int(x.split()[1].replace('р', '')))
    for x in PRICE_LIST.split('\n')
]

dict_from_price_list = dict(tuples_from_price_list)
print(dict_from_price_list)
