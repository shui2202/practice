squares = [i ** 2 for i in range(1, 101) if i % 2 == 0] #odd would be 1
#some list comphrension
print("Even")
print(squares)
odds = []
for i in range(1, 101):
    i = i ** 2
    if i % 2 == 1:
        odds.append(i)
print("Odds")
print(odds)
#regular way of doing it