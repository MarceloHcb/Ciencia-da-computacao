def my_sum(number1: int, number2: int) -> int:
    return number1 + number2

def test_sum_positive_num():
    assert my_sum(1, 2) == 3

def test_sum_negative_num():
    assert my_sum(-1, -2) == -3