import pytest
from Tv import Tv

def test_tv_initial_state():
    tv = Tv(32)
    assert tv.volume == 50
    assert tv.canal == 1
    assert tv.ligada == False

def test_aumentar_volume():
    tv = Tv(32)
    tv.aumentar_volume()
    assert tv.volume == 51

def test_diminuir_volume():
    tv = Tv(32)
    tv.diminuir_volume()
    assert tv.volume == 49

def test_modificar_canal_dentro_dos_limites():
    tv = Tv(32)
    tv.modificar_canal(5)
    assert tv.canal == 5

def test_modificar_canal_fora_dos_limites():
    tv = Tv(32)
    with pytest.raises(ValueError):
        tv.modificar_canal(100)

def test_ligar_desligar():
    tv = Tv(32)
    tv.ligar_desligar()
    assert tv.ligada == True
    tv.ligar_desligar()
    assert tv.ligada == False

def test_show_details(capsys):
    tv = Tv(32)
    tv.show_details()
    captured = capsys.readouterr()
    assert captured.out.strip() == "TV - Tamanho: 32 polegadas, Volume: 50, Canal: 1, Ligada: False"

def test_str_representation():
    tv = Tv(32)
    assert str(tv) == "TV - Tamanho: 32 polegadas, Volume: 50, Canal: 1, Ligada: False"
