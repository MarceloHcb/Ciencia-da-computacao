def fizz_buzz(n):
    fizz_buzz = []    
    for number in range(1, n+1):
        if number % 3 == 0 and number % 5 == 0:
            fizz_buzz.append('FizzBuzz')
        elif number % 3 == 0:
            fizz_buzz.append('Fizz')
        elif number % 5 == 0:
            fizz_buzz.append('Buzz')
        else:
            fizz_buzz.append(number)    
    return(fizz_buzz)

def fizz_buzz1(n):
    fizz_buzz = ['fizz'*(i%3==0) + 'buzz'*(i%5==0) or i for i in range(1, n+1)]
    return(fizz_buzz)

print(fizz_buzz(15))
# fizz_buzz1(5)

# fizz_buzz(2)
