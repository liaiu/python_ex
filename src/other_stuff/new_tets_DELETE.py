import os

d = 10
a = 5
b=8
c=20
e=43

f = [a,b,c,e]

def new(d, f_l):
    new_l = list(f_l)
    f_l.sort()
    if len(f_l) == 1:
        return "DA"
    else:
        s = abs(f_l[0] - f_l[1])
        if s <= d:
            new_member = f_l[0] + f_l[1]
            new_l.remove(f_l[0])
            new_l.remove(f_l[1])
            new_l.append(new_member)
            return new(d, new_l)
        else:
            return "NU"

# print(new(d,f))

with open("big.in", "r") as file:
    contents = file.read()

print(contents)
info = contents.split("\n")
with open("big.out", "w") as file:

    for x in range(int(contents[0])):
        line = info[x+1]
        line_items = list(map(int, line.split(" ")))
        no_items = line_items.pop(0)
        result = new(no_items, line_items)
        file.write(result+"\n")