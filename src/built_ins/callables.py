class ExtraInt(int):

    def __call__(self, *args, **kwargs):
        print("Args: {}".format(args))
        print("Kwargs: {}".format(kwargs))


class SumItUp:

    def __init__(self, a=4, b=10):
        self.a = ExtraInt(a)
        self.b = b

    def __call__(self, *args):
        sum_list = [self.a, self.b, *args]
        return sum(sum_list)

    def get_attr(self):
        all_attr = dir(self)
        callables = "CALLABLES:"
        non_callables = "NOT CALLABLES"
        for x in all_attr:
            if callable(getattr(self, x)):
                callables += "\n" + x
            else:
                non_callables += "\n" + x
        print(callables)
        print(non_callables)

obj_a = SumItUp()
print(obj_a())
print(obj_a(10))
obj_a.a()