candies = [2,3,5,1,3]
extraCandies = 3
answer = [True,True,True,False,True]

def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    return [candy + extraCandies >= max_candies for candy in candies]
print(kidsWithCandies(candies, extraCandies))