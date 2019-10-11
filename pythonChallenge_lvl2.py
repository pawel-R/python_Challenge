
text = open("lvl2.txt", "r").read()
counted = {}

for i in text:
    counted[i] = counted.get(i, 0) + 1

print(counted)

# equality
