my_age = int(input("Enter your age: "))

team_name = ["A", "B", "C", "D", "E"]

if my_age >=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

print("Team Name: ", team_name[my_age%5])