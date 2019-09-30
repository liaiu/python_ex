import collections

"""
https://docs.python.org/3.7/library/collections.html
"""

d1 = dict(a=1, b=2, c=3)
d2 = {1: "a", 2: "b", 3: "c"}

# Default values
print(d1.get("a"))
print(d1.get(3))

c = d2.setdefault(1, "not here")
print(c, d2)
c2 = d2.setdefault(7, "not here")
print(c2, d2)

# defaultdict
print("\n ------ defaultdict --------")


def letter_frequency1(sentence):
    frequencies = {}
    for letter in sentence:
        frequencies.setdefault(letter, 0)
        frequencies[letter] += 1
    return frequencies


def letter_frequency2(sentence):
    frequencies = collections.defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies


print(letter_frequency1("A new era is born today").items())
print(letter_frequency2("A new era is born today").items())
