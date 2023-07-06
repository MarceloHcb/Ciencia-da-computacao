import pytest
from fizz_buzz import fizz_buzz

def test_fizzbuzz_deve_retornar_uma_lista_de_numeros():
    assert fizz_buzz(2) == [1,2]
  
def test_fizzbuzz_dividido_por_3_retorna_fizz():
    assert fizz_buzz(3)[-1] == 'Fizz'

def test_fizbuzz_dividido_por_5_retorna_buzz():
    assert fizz_buzz(5)[-1] == 'Buzz'
    
def test_fizzbuzz_dividivo_por_3_e_5_retorna_fizzbuzz():
    assert fizz_buzz(15)[-1] == 'FizzBuzz'
    