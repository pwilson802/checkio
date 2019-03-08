import string
import re

def checkio(data):
    data = re.compile(r'\w').findall(data)
#    data = data.replace(' ', '')
    res = 0
    lettermap = {x:sum([int(i) for i in str(((ord(x)) - 48) * 2)]) for x in string.ascii_uppercase }
    nummap = {'0':0, '1':2, '2':4, '3': 6, '4':8, '5':1, '6':3, '7':5, '8':7, '9':9}
    all_mappings = {**lettermap, **nummap}
    print(all_mappings)
    for num, x in enumerate(list(reversed(data))):
        print(x)
        if num % 2 == 0:
            res += all_mappings[x]
            print(all_mappings[x])
        else:
            if x in string.ascii_uppercase:
                print(ord(x) - 48)
                res += (ord(x) - 48)
            else:
                print(x)
                res += int(x)
    print(res)
    if res % 10 == 0:
        check_num = '0'
    else:
        check_num = str(10 - (res % 10))
    print(check_num)

    return [check_num, res]
