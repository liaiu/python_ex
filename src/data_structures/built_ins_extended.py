from collections import KeysView, ItemsView, ValuesView


class DictSorted(dict):
    def __new__(*args, **kwargs):

        new_dict = dict.__new__(*args, **kwargs)
        new_dict.ordered_keys = []
        return new_dict

    def __setitem__(self, key, value):

        '''self[key] = value syntax'''
        if key not in self.ordered_keys:
            self.ordered_keys.append(key)
        super().__setitem__(key, value)

    def setdefault(self, key, value):

        if key not in self.ordered_keys:
            self.ordered_keys.append(key)
        return super().setdefault(key, value)

    # def keys(self):
    #
    #     return KeysView(self)
    #
    # def values(self):
    #
    #     return ValuesView(self)
    #
    # def items(self):
    #
    #     return ItemsView(self)

    def __iter__(self):

        '''for x in self syntax'''

        return self.ordered_keys.__iter__()

ds = DictSorted()
d = dict()
for x in range(10):
    ds[x] = str(x)
    d[x] = str(x)
# ds["a"] = 1
# ds["b"] = 2
# ds.setdefault("c", 3)
#
# d["a"] = 1
# d["b"] = 2
# d.setdefault("c", 3)


for k,v in ds.items():
    print(k,v)

print(ds.values())
print(d.values())
print("\n\n")

for k,v in d.items():
    print(k,v)