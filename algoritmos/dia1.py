def number_substituition(numbers:list[int]):
    for i in range(len(numbers)):
        ...


def test_number_substituition():
    numbers_list = [2, 1, 2, 3, 0, 5, 1, 2, 3]
    number_substituition(numbers_list)
    assert numbers_list == [5,5,5,5,5,5,3,3,3]  