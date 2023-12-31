def pairs_in_list(n):
    list_numbers = []
    count = 0
    for number in range(1,n+1):
      print(number)
      if number % 2 == 0 and number != 0:
        list_numbers.append(number)
        count += 1
    return f'Os números são {list_numbers} somando total de {count} pares!'


#RECURSIVO
def recursive_pairs_in_list(n):  
    #condição de parada
    if n == 1:
        return 0
    #atendendo condição da função
    elif n % 2 == 0:      
      return 1 + recursive_pairs_in_list(n-1)
    #condição contraria da função
    else:
        return recursive_pairs_in_list(n-1)


if __name__ == "__main__":
    print(pairs_in_list(6))
    print(recursive_pairs_in_list(6))