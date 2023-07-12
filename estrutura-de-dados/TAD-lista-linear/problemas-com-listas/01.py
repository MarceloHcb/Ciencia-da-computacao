def contains_duplicates(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

test1 = [1,2,3,1] #True
test2 = [1,2,3,4] #False
test3 = [1,2,3,4,5,6,7,8,9,10] #False
test4 = [1,2,3,4,5,6,7,8,4,3] # True

print(contains_duplicates(test1))
print(contains_duplicates(test2))
print(contains_duplicates(test3))
print(contains_duplicates(test4))
