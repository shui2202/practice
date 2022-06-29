#duplicates
list = []
many = int(input("How many values do you want in your list? "))
for i in range(many):
    value = str(input("Enter a value that you want to add to your list: "))
    list.append(value)

list2 = []

for i in list:
    if i not in list2:
        list2.append(i)


print("The original list without duplicate values: " + str(list2) + ".")
if len(list) == len(str(many)):
    print("There were no duplicates in the list that was given.")
