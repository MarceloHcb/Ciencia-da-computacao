def loop_print(my_list):
    result = ""
    for i in my_list:
        result += f"{i} "
        print(i, end=" ")
    my_list.pop()
    my_list.reverse()
    print(my_list[-1], end=" ")
    for i in my_list:
        result += f"{i} "
        print(i, end=" ")
    print()
    print(result.strip())


loop_print([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
