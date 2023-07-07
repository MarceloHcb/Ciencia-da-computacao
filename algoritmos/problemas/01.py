# Elemento aparece mais de 25% em um array ordenado

def more25(array):
    for number in array:
        count = 0
    porcent25 = len(array)//4
    for number2 in array:
        if number == number2:
            count +=1
    if count > porcent25:
        print(number)
        return number


def more252(array):
    porcent25 = len(array)//4
    porcent75 = len(array) - porcent25
    for index, elem in enumerate(array[:porcent75]):
        if elem == array[index + porcent25]:
            print(elem)
            return elem
    return -1         

more25([1,2,3,4,5,5,5,6])
more252([1,2,3,4,5,5,5,6])