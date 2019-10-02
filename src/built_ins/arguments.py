# def ex_one(*args):
#     print("My type is: {}".format(type(args)))
#     s = 0
#     for i in args:
#         s += i
#     return s
#
#
# print(ex_one(1, 2, 3))
# print(ex_one(2))
# print(ex_one())
# print(ex_one(*range(3)))


# def ex_two(**kwargs):
#     result = ""
#
#     for key, val in kwargs.items():
#         new_line = "{}__{}".format(key, val)
#         result += "\n" + new_line
#     return result
#
# print(ex_two(**dict(test="abc", new="gft")))
# print(ex_two(test="abc", new="gft"))


def ex_three(a, b, *args, **kwargs):
    formatted_text = "{} : {}".format(a, b)
    for arg in args:
        formatted_text += "     {}".format(arg)
    for k in kwargs:
        t = "\n{} - {}".format(k, kwargs[k])
        formatted_text += t
    return formatted_text

# print(ex_three())
# print(ex_three(4))
# print(ex_three(4, 5))
# print(ex_three(4, 5, "t", "n"))
# print(ex_three(4, 5, "t", "n", k=3))
# print(ex_three(4, 5, "t", "n", k=3, m=4))
# print(ex_three(a=4, b=5, k=3, m=4))
