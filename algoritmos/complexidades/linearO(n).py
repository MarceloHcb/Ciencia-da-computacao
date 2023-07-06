def list_sum(numbers_list):
    sum = 0
    for number in numbers_list:
        sum += number
    return sum

# Tempo e .. Espaço

def squared_list(numbers_list):
    new_list = []
    for number in numbers_list:
        new_list.append(number * number)
    return new_list
        # O(n)

# Descarta as constantes

def min_max_1(array):
    min = array[0]
    max = min
    for e in array:
        if e < min:  #O(n)
            min = e  
    for e in array:    # O("2"n) ----> O(n)
        if e > max:           
            max = e  #O(n)

    return min, max
