def bigger_int(my_list: list): 
    my_list.sort()   
    return my_list[-1]

#RECURSIVO
def maiorinteiro_aux(lista, tamanho):
    if tamanho == 1:
        return lista[0]
    else:
        maior_do_resto_da_lista = maiorinteiro_aux(lista, tamanho-1)
        if maior_do_resto_da_lista > lista[tamanho-1]:
            return maior_do_resto_da_lista
        else:
            return lista[tamanho-1]

def maiorinteiro(lista):
    tamanho = len(lista)
    return maiorinteiro_aux(lista, tamanho)

def test_bigger_int():
    assert bigger_int([5, 2, 8, 1, 9, 3]) == 9   
    assert bigger_int([-5, -2, -8, -1, -9, -3]) == -1
    assert bigger_int([-5, 2, 0, -1, 9, -3]) == 9
    assert bigger_int([7]) == 7
    assert bigger_int([3, 3, 3, 3]) == 3

if __name__ == "__main__":
  my_list = [0,1,2,3,4,5,9,15,8,5]
  print(bigger_int(my_list))

print(maiorinteiro([1, 21, 300, 4, 57]))

