class Liquidificador:
    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco

class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.liquidificador = None

    def comprar_liquidificador(self, marca, preco):
        if preco <= self.saldo_na_conta:
            self.saldo_na_conta -= preco
            self.liquidificador = Liquidificador(marca, preco)
            print(f"{self.nome} comprou um liquidificador da marca {marca}!")
        else:
            print(f"{self.nome} não tem saldo suficiente para comprar o liquidificador da marca {marca}.")


# Exemplo de uso
pessoa1 = Pessoa("João", 100.0)

pessoa1.comprar_liquidificador("MarcaA", 50.0)  # João comprou um liquidificador da marca MarcaA!
pessoa1.comprar_liquidificador("MarcaB", 200.0)  # João não tem saldo suficiente para comprar o liquidificador da marca MarcaB.
