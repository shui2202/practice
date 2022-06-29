string = "hello$bye"
h = string[:string.index("$")]

b = string[string.index("$") + 1:]

print(h)
print(b)