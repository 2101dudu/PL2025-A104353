import sys
import re


def alphabetical_order():
    temp = []
    for linha in sys.stdin:
        m = re.search(r'\d\d\d\d;[^;]*;([^;]*);', linha)
        if m is not None:
            temp.append(m[1])

    temp.sort()
    print(temp)


def number_per_category():
    temp = {}
    for linha in sys.stdin:
        m = re.search(r'\d\d\d\d;([^;]*);[^;]*;', linha)
        if m is not None:
            category = m[1]
            if category not in temp:
                temp[category] = 1
            else:
                temp[category] += 1

    print(temp)


def title_per_category():
    temp = {}
    name = ""
    for linha in sys.stdin:
        m = re.search(r'(((\d\d\d\d;)([^;]*);.*$)|^([^;\n]*);[^ \w])', linha)
        if m is not None:
            if m[2] is None:
                name = m.group(1)
            else:
                category = m.group(4)
                if category not in temp:
                    temp[category] = []
                temp[category].append(name)

    for key, value in temp.items():
        value.sort()
        print(key, ":", len(value), ";", value)


# alphabetical_order()
# number_per_category()
# title_per_category()
