numbers_list = input("Enter a list of numbers separated by space:  ")
numbers_list = numbers_list.split(" ")
n = 0
for number in  numbers_list: 
  if not number.isdigit():
      print(f"Invalid input , {number} is not a number")
  else:
        n += int(number)
        
print(f"The sum of the valid numbers is {n}")