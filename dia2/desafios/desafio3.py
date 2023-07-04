# def data_to_bool(my_list):
#     result = list()
#     for i in my_list:
#         if i:
#             result.append(True)
#         else:
#             result.append(False)
#     return result
# print(data_to_bool([1, 0, 0, 1, 1, 0, 1, 0, 1, 1]))

def data_to_bool(my_list):
    result = list()
    for i in my_list:
        if isinstance(i, int):
            cond1 = i > 42
            result.append(cond1)
        if isinstance(i,str):    
            cond2 = 'a' in i
            result.append(cond2)
        if isinstance(i, float):
            cond3 = i > 3.14
            result.append(cond3)
            if isinstance(i, list):
                cond4 = len(i) != 2
                result.append(cond4)
    return result

print(data_to_bool(["bolo", "arara"]))
print(data_to_bool([3.16,3.0 ]))


