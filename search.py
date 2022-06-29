import random

def search(seq, item):
    begin = 0
    end = len(seq) - 1
    while begin <= end:
        midpoint = begin + (end - begin) // 2
        midpoint_value = seq[midpoint]

        if midpoint_value == item:
            return midpoint_value
        
        elif item < midpoint_value:
            end = midpoint - 1
        else:
            begin = midpoint + 1

    return "Item not found in list."


lists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
items = random.choice(lists)

print(search(lists, items))
print("The number was " + str(items))