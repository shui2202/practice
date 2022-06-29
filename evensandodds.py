#way1
for i in range(1, 101):
    if i % 2 == 0:
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")
#way 2
x = 1
while x < 101:
    if x % 2 == 1:
        print(str(x) + " is odd")
    else:
        print(str(x) + " is even")

    x+=1