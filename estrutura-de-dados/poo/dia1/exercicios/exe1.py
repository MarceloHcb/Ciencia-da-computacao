class Ventilador:
    def __init__(self, cor, marca, preco, voltagem):
      self.cor = cor
      self.marca = marca
      self.preco = preco
      self.voltagem = voltagem
    def cor(self):
        return self.__cor
    def __str__(self):
        return f"""
      *Ventilador*
    - cor: {self.cor}
    - marca: {self.marca}
    - preco: {self.preco}
    - voltagem: ({self.voltagem})
    """
    
ventiladorAzul = Ventilador('azul', 'Philco', 130.0, 220)
VentiladorPreto = Ventilador('preto', 'Arno', 150.0, 110)
print(ventiladorAzul)
print(VentiladorPreto)

class Pessoa:
    def __init__(self, nome, saldo_na_conta, ventiladorComprado=None):
        self.nome = nome
        self.ventiladorComprado = ventiladorComprado
        self.saldo_na_conta = saldo_na_conta               
    def __str__(self):
        return f"""
      *Pessoa*
    - Nome: {self.nome}
    - Saldo: {self.saldo_na_conta}
    - Ventilador comprado: {self.ventiladorComprado}    
    """

    def comprar_ventilador(self, ventilador):
        if ventilador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= ventilador.preco
            self.ventiladorComprado = self.ventiladorComprado

pessoa1 = Pessoa("Mariana", 5000, ventiladorAzul)
pessoa2 = Pessoa("Camila", 3000, VentiladorPreto)
pessoa3 = Pessoa("Junior", 4000)
pessoa1.comprar_ventilador(ventiladorAzul)
pessoa2.comprar_ventilador(VentiladorPreto)
print(pessoa1)
print(pessoa2)
print(pessoa3)