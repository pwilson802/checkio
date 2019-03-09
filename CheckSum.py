import string
import re

def checkio(data):
    data = re.compile(r'[A-Za-z0-9]').findall(data)
    res = 0
    lettermap = {x:sum([int(i) for i in str(((ord(x)) - 48) * 2)]) for x in string.ascii_uppercase }
    nummap = {'0':0, '1':2, '2':4, '3': 6, '4':8, '5':1, '6':3, '7':5, '8':7, '9':9}
    all_mappings = {**lettermap, **nummap}
    print(all_mappings)
    for num, x in enumerate(list(reversed(data))):
        print(x)
        if num % 2 == 0:
            res += all_mappings[x]
        else:
            if x in string.ascii_uppercase:
                res += (ord(x) - 48)
            else:
                res += int(x)
    if res % 10 == 0:
        check_num = '0'
    else:
        check_num = str(10 - (res % 10))
    return [check_num, res]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio("799 273 9871") == ["3", 67]), "First Test"
    assert (checkio("139-MT") == ["8", 52]), "Second Test"
    assert (checkio("123") == ["0", 10]), "Test for zero"
    assert (checkio("999_999") == ["6", 54]), "Third Test"
    assert (checkio("+61 820 9231 55") == ["3", 37]), "Fourth Test"
    assert (checkio("VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"

    print("OK, done!")
