st = "ab"
letters = list(st)
d = dict(zip(range(len(letters)), letters))
print(d)


def get_name(initial_dict):
    for x in initial_dict.keys():
        key_val = initial_dict[x]
        poss_values = sorted([m for m in initial_dict.values() if key_val!= m])
        if len(poss_values) == 0:
            continue
        else:
            lower_val = poss_values[0]
            changed_pos = sorted([ind for ind in initial_dict.keys() if initial_dict[ind] == lower_val])[0]
            initial_dict[x] = lower_val
            initial_dict[changed_pos] = key_val
        print(initial_dict)
    s = sorted(initial_dict.items(), key= lambda i: i[0])
    new_name = "".join([t[1] for t in s])
    return new_name


# def get_name2(initial_dict, curr_dict):
#     for x in initial_dict.keys():
#         key_val = initial_dict[x]
#         poss_values = sorted([m for m in curr_dict.values() if key_val!= m])
#         if len(poss_values) == 0:
#             continue
#         else:
#             lower_val = poss_values[0]
#             changed_pos = sorted([ind for ind in initial_dict.keys() if initial_dict[ind] == lower_val])[0]
#             initial_dict[x] = lower_val
#             initial_dict[changed_pos] = key_val
#         print(initial_dict)
#     s = sorted(initial_dict.items(), key= lambda i: i[0])
#     new_name = "".join([t[1] for t in s])
#     return new_name

st = "abac"
sorted_st = sorted(st)

list_len = len(st)
for i in range(list_len):
    letter_val = st[i]
    if letter_val == sorted_st[i]:
        first_index = [m for m in range(list_len) if sorted_st[m] != letter_val]
        if len(first_index) == 0:
            print(-1)
            break
        else:
            first_index = first_index[0]
        sorted_st[i], sorted_st[first_index] = sorted_st[first_index], sorted_st[i]
    print(sorted_st)

print("".join(sorted_st))