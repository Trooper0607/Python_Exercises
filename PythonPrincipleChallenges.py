#https://pythonprinciples.com/challenges/

def capital_indexes(word):
    list1 = list(word)
    list2 = []
    for x, y in enumerate(list1):
        if y == y.upper():
            list2.append(x)
    return list2

print(capital_indexes('HeLlO'))

def mid(word):
    middle = ""
    if (len(word) % 2) == 0:
        return middle
    else:
        newlist = list(word)
        middle_index = len(word) // 2
        for x, y in enumerate(newlist):
            if x == middle_index:
                middle = y
                return middle
print(mid('abc'))


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

def online_count(statuses):
    counter = 0
    for x, y in statuses.items():
        if y == 'online':
            counter += 1
    return counter
print(online_count(statuses))

import random

def random_number():
     number = random.randint(1, 100)
     return number


def only_ints(x, y):
    if type(x) == int and type(y) == int:
        return True
    else:
        return False
print(only_ints(1, 'a'))


def double_letters(word):
    counter = 0
    for x in range(0, len(word) - 1):
        if (word[x] == word[x + 1]):
            counter += 1
        else:
            counter
    if counter > 0:
        return True
    else:
        return False
print(double_letters('helo'))
def add_dots(word):
    word = list(word)
    with_dots = '.'.join(word)
    return with_dots
print(add_dots('test'))


def remove_dots(word):
    word = word.split('.')
    return ''.join(word)
print(remove_dots(add_dots('test')))


def count(word):
    counter = 1
    for x in range(len(word)-1):
        if (word[x] == '-'):
            counter += 1
        else:
            counter
    return counter

print(count('met-a-phor'))

def is_anagram(word1, word2):
    list1 = list(word1)
    list2 = list(word2)

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False
print(is_anagram('abc','cab'))



def flatten(list1):
    newlist = []
    for x in list1:
        for y in x:
            newlist.append(y)
    return newlist
print(flatten([[1, 2], [3, 4]]))


def larget_difference(list1):
    return max(list1) - min(list1)

print(larget_difference([1, 2, 3]))

def get_row_col(rc):
    col = rc[0]
    row = rc[1]

    dictionary = {
        'A': 0,
        'B': 1,
        'C': 2
    }

    xy = (int(row) - 1,dictionary.get(col))
    return xy

print(get_row_col("A3"))


def palindrome(word):
    word = list(word)
    if word == word[::-1]:
        return True
    else:
        return False
print(palindrome('mum'))

def up_down(n):
    return (n-1, n+1)
print(up_down(5))


def consecutive_zeros(n):
    list1 = n.split('1')
    newlist = []
    for x in list1:
        newlist.append(len(x))
        maxn = max(newlist)
    return maxn

print(consecutive_zeros("1001101000110"))



def all_equal(n):
    chk = True
    for x in n:
        if x != n[0]:
            chk = False
            break
    return chk
print(all_equal([1,1,2]))

def triple_and(a,b,c):
    return a and b and c


def convert(n):
    return [str(x) for x in n]
print(convert([1,2,3]))

def zap(a, b):
    result = []
    for i in range(len(a)):
         result.append((a[i],b[i]))
    return result
print(zap([0, 1, 2, 3], [5, 6, 7, 8]))

def validate(code):
    if "def" not in code:
        return "missing def"
    elif ":" not in code:
        return "missing :"
    elif "(" and ")" not in code:
        return "missing  paren"
    elif "( + )" not in code:
        return "missing para"
    elif "validate" not in code:
        return "wrong name"
    elif "return" not in code:
        return "missing return"

        return True

def list_xor(n, list1, list2):
    if n not in list1 and n not in list2:
        return False
    elif n in list2 and n in list1:
        return False
    elif n in list1 and n not in list2:
        return True
    elif n in list2 and n not in list1:
        return True
print(list_xor(1, [1, 2, 3], [4, 5, 6]))
print(list_xor(1, [0, 2, 3], [1, 5, 6]))
print(list_xor(1, [1, 2, 3], [1, 5, 6]))
print(list_xor(1, [0, 0, 0], [4, 5, 6]))

def param_count(*argv):
    counter = 0
    for arg in argv:
        counter += 1
    return counter

def format_number(n):
    res = str(n)
    res = res[::-1]

    ans = ""
    for i in range(len(res)):
        if i % 3 == 0 and i != 0:
            ans += ','
        ans += res[i]

    ans = ans[::-1]

    return ans
print(format_number(1000))
