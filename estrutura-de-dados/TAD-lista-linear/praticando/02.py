def kids_with_candies(candies: list[int], extra_candies:  int) -> list[bool]:
    ...

def test_kids_with_candies():
    assert kids_with_candies([2,3,5,1,3], 3) == [True, True, True, False, True]