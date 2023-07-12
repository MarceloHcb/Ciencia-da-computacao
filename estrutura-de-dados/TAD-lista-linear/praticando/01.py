def contains_duplicate(nums: list[int]) -> bool:
    # found = [] 
    # for num in nums:
    #     if num in found:
    #         return True
    #     found.append(num)
    # return False
    nums.sort()
    for index in range(len(nums) -1):
        if nums[index] == nums[index + 1]:
            return True
    return False
# return len(nums) != len(set(nums)) 

def test_contains_duplicate():
    assert contains_duplicate([1,2,3,1])
    assert not contains_duplicate([1,2,3,4])
    assert contains_duplicate([1,1,1,3,3,4,3,2,4,2])
    assert not contains_duplicate([1,2,3,4,5,6,7,8,9,10])
    

