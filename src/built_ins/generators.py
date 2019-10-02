import sys
import cProfile
import time

"""
A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

    Generator function contains one or more yield statement.
    When called, it returns an object (iterator) but does not start execution immediately.
    Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
    Once the function yields, the function is paused and the control is transferred to the caller.
    Local variables and their states are remembered between successive calls.
    Finally, when the function terminates, StopIteration is raised automatically on further calls.
! Generators are much more memory efficient than list comprehensions
"""

# Ex1
#
# def gen1():
#     x = 1
#     print("First")
#     yield x
#
#     x += 1
#     print("Second")
#     yield x
#
#     x += 1
#     print("Third")
#     yield x
#
# a = gen1()
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
#
# for item in a:
#     print(item)


# Ex2

# def rev(s):
#     for i in range(len(s) -1, -1, -1):
#         yield s[i]
#
# for c in rev("test_abss"):
#     print(c)


# # Test memory wise
# n = 100
# list_nums = [x**2 for x in range(n)]
# print(sys.getsizeof(list_nums))
#
# gen_nums = (x**2 for x in range(n))
# print(sys.getsizeof(gen_nums))
#
#
# cProfile.run('sum([i * 2 for i in range(10000)])')
# cProfile.run('sum((i * 2 for i in range(10000)))')


# Other uses -> coroutine = a generator function into which you can pass data

#
# def is_div_by_eleven(num):
#     if num % 11 == 0:
#         return True
#     return False
#
# def infinite_div():
#     num = 1
#     while True:
#         if is_div_by_eleven(num):
#             i = (yield num)
#             if i is not None:
#                 num = i
#         num += 1
#
# inf_div = infinite_div()
# for i in inf_div:
#     print(i)
#     dig = len(str(i))
#     inf_div.send(10**dig)
#     # if dig == 3:
#     #     inf_div.throw(ValueError("You should not try with larger than 3 digits"))
#     if dig == 20:
#         print("Only go to 20 digits max")
#         inf_div.close() # Raises a StopIteration so for loop will stop
#     time.sleep(0.2)
