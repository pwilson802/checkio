import string

def checkio(data):
    data = data.replace(' ', '')
    res = 0
    lettermap = {x:sum([int(i) for i in str(ord(x))]) for x in string.ascii_uppercase }
    nummap = {'0':0, '1':2, '2':4, '3': 6, '4':8, '5':1, '6':3, '7':5, '8':7, '9':9}
    all_mappings = {**lettermap, **nummap}
    print(all_mappings)
    for num, x in enumerate(list(reversed(data))):
        if num % 2 == 0:
            res += all_mappings[x]
        else:
            res += int(x)
    print(x)
    return [x % 10, x]
