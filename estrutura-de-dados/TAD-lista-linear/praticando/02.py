def kids_with_candies(candies: list[int], extra_candies:  int) -> list[bool]:
    # max_candies = max(candies) #O(n)
    # result = []
    # for candy in candies: #O(n)
    #     if candy + extra_candies >= max_candies:
    #         result.append(True)
    #     else:
    #         result.append(False)
    # return result
    max_candies = max(candies) #O(n) 
    return [candy + extra_candies >= max_candies for candy in candies] #O(n)

def test_kids_with_candies():
    assert kids_with_candies([2,3,5,1,3], 3) == [True, True, True, False, True]