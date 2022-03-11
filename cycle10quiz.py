# author: LM (AMDG) 2/2/22
# naming functio with one parameter
from queue import Empty


def average(lst):
    # counter
    total = 0
    # using enumerate to iterate through list of prices
    for index, value in enumerate(lst):
        total = total + value
        new_average = total / 7
    return new_average


print(average([30, 40, 55, 25, 60, 80, 65]))


# function f0r reducing prices
def reduced_Prices(lst):
    # where the reduced values will go in
    empty = []
    # using enumerate to go through list of prices
    for index, value in enumerate(lst):
        # subtracting 5 from original value
        new_value = value - 5
        # appending value to empty list
        empty.append(new_value)
    return empty


print(reduced_Prices([30, 40, 25, 55, 60, 80, 65]))


# sales function
def sales(prices, sales):
    # counter
    total = 0
    # using enumerate to iterate through prices list, then multiplying the values by index 0 of sales list, then deleting it
    for index, value, in enumerate(prices):
        total = total + (value * sales[0])
        del sales[0]
    return total


print(sales([30, 40, 25, 55, 60, 80, 65], [1, 3, 2, 5, 2, 1, 2]))


# looks for values greater than 40and rediuces them by ten
def morethan(prices):
    # the new values will be stored here
    newlst = []
    # using enumerate to iterate through list
    for index, value in enumerate(prices):
        # using condtional to sub=tract 10 from any value greater than 40
        if value > 40:
            value = value - 10
            # value gets put into new list
            newlst.append(value)
    return newlst


print(morethan([30, 40, 25, 55, 60, 80, 65]))


def naming_pricing(prices, items):
    # since the items list is 2 lists in one we have to use two 'for loops'
    for group in items:
        for index, value in enumerate(group):
            print('{0} ${1}'.format(value, prices[0]))
            # deletes price number at index 0 so it can continuously loop
            del prices[0]


naming_pricing([30, 40, 25, 55, 60, 80, 65],[["tee-shirt", 'long-sleeve', 'tanktop'], ['quarter-zip', 'pullover', 'full-zip', 'half-zip']])
