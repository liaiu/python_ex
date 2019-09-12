"""
Mutable objects: list, dict, set, byte array
Immutable objects: int, float, complex, string, tuple, frozen set [note: immutable version of set], bytes

"""

x = "abc"
y = "abc"

print(id(x))
print(id(y))

print("changing")
y = "abcd"
print(id(x))
print(id(y))

print("\ninteger - immutable\n")
a = 10

b = a

print(id(a) == id(b))
print(id(b) == id(10))

print("change a")

a = a + 1
print(id(a) == id(b))
print(id(b) == id(10))

print("\nlist - mutable\n")

m = list([1, 2, 3, 4])
n = m

print(id(m) == id(n))

m.pop()

print(id(m) == id(n))

print("\n small exercise\n")


def change_int(v):
    v += 2


def change_list(l):
    l += [2]


o = 7
change_int(o)
print(o)

l1 = [3, 3]
change_list(l1)
print(l1)

print("\n reference(binding) is actually immutable")

tup = (2, 3, l1)
print(tup)

change_list(l1)
print(tup)