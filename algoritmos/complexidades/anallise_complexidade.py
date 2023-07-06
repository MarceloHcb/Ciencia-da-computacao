def calculations(n):
  number1 = 0
  for n1 in range(n):
      number1 += n1 #linear n

  number2 = 0
  for n1 in range(n): # (0,1) linear n
      for n2 in range(n): # (0,1) linear n  n*n  quadratica
        number2 += n1 + n2  

  number3 = 0
  for n1 in range(n): # linear
      for n2 in range(n): # linear
          for n3 in range(n): # linear  n*n*n cubica 
              number3 += n1 + n2 + n3

  return number1, number2, number3
# n + n² + n³ --> n³  'foca no maior'
n1, n2, n3 = calculations(100)
print(f'{n1}, {n2}, {n3}')