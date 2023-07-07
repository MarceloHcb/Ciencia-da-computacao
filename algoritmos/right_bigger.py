DESCRIPTION = "Dois loops com segundo range otimizado"
TIME_COMPLEXITY = "O(n^2)"
SPACE_COMPLEXITY = "O(1)"

def right_bigger(numbers: list[int]):
    for i in range(len(numbers)):
        original_element = numbers[i]
        right_max = original_element
        for j in range(i+1, len(numbers)):
            new_element = numbers[j]
            if new_element > right_max:
                right_max = new_element
        numbers[i] = right_max
    

def test_right_bigger():
    numbers_list = [2,1,2,3,0,5,1,2,3]
    right_bigger(numbers_list)
    assert numbers_list == [5,5,5,5,5,5,3,3,3]


DESCRIPTION2 = "Dois loops slicing no segundo"
TIME_COMPLEXITY2 = "O(n^2)"
SPACE_COMPLEXITY2 = "O(n)"

def right_bigger2(numbers: list[int]):
    for i in range(len(numbers)):        
        right_max = numbers[i]
        for new_element in numbers[i + 1:]: #slice 
            if new_element > right_max:
                right_max = new_element
        numbers[i] = right_max
    

def test_right_bigger2():
    numbers_list = [2,1,2,3,0,5,1,2,3]
    right_bigger2(numbers_list)
    assert numbers_list == [5,5,5,5,5,5,3,3,3]

DESCRIPTION3 = "Um loop reverso"
TIME_COMPLEXITY3 = "O(n)"
SPACE_COMPLEXITY3 = "O(1)"

def right_bigger3(numbers: list[int]):
    last_position = len(numbers) -1
    right_max = numbers[last_position]
    for i in range(last_position, -1, -1):
        if right_max >= numbers[i]:
            numbers[i] = right_max
        else:
            right_max = numbers[i]
    

def test_right_bigger3():
    numbers_list = [2,1,2,3,0,5,1,2,3]
    right_bigger3(numbers_list)
    assert numbers_list == [5,5,5,5,5,5,3,3,3]
