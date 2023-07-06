def show_with_all(numbers_list):
    for x in numbers_list: # O(n)
      for y in numbers_list:# O(n)
          print(x,y)
# O(n²)
if __name__ == "__main__":
    my_list = [2, 5, 8]
    show_with_all(my_list)

# Descartar termos não dominantes

def max_and_pairs(array):
    max = array[0]
    for a in array:   
        if a > max:  #O(n)
            max = a
    print(max)                #O(n+n2) ---> O(n²)

    for a in array:
        for b in array:
            print(a, b) #O(n²)