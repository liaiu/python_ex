import collections


Person = collections.namedtuple("Person", "name age gender")

b = Person("bobby", "55", "M")
print(b)
print(Person._fields)

c1 = collections.namedtuple("Test", "param1 class param3", rename=True)
c2 = collections.namedtuple("Test2", "a b c a", rename=True)
print(c1._fields)
print(c2._fields)

# c1 = collections.namedtuple("Test", "param1 class param3")
# c2 = collections.namedtuple("Test2", "a b c a")
#
# # b.age = "34"


