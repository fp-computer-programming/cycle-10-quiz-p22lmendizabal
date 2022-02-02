# author: LM (AMDG) 2/2/22
# naming functio with one parameter
def average(lst):
    #using enumerate to iterate through list of prices
    for index, value in enumerate(lst):
        value = value + lst[index]
        #deletes the firstobject in list
        del lst[index]

        print(value)


print(average([30, 40, 25, 55, 60, 80, 65]))

def reduced_Prices(lst):
    empty= []
    #using enumerate to go through list of prices
    for index, value in enumerate(lst):
        #subtracting 5 from original value
        new_value = value - 5
        #appending value to empty list
        empty.append(new_value)
        print(empty)
    
reduced_Prices([30, 40, 25, 55, 60, 80, 65])

def sales(lst):
    #using enumerate to iterate through sales list
    for value in (lst):
        for index, innervalue in value:
            print(index, innervalue)
    



def morethan40(prices):
    #using enumerate to iterate through list
    for index, value in enumerate(prices):
        #using condtional to sub=tract 10 from any value greater than 40
        if value > 40:
            value = value - 10
            print(value)
