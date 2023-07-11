class Tv:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.volume = 50
        self.canal = 1
        self.ligada = False

    def aumentar_volume(self):
        self.volume = min(self.volume + 1, 99)
    
    def diminuir_volume(self):
        self.volume = max(self.volume - 1, 0)

    def modificar_canal(self):
        if self.canal < 1 or self.canal > 99:
            raise ValueError("O canal está fora dos limites permitidos (1-99).") 
        return self.canal

    def ligar_desligar(self):
        self.ligada = not self.ligada  
    
    def __str__(self):
        return f"TV - Tamanho: {self.tamanho} polegadas, Volume: {self.volume}, Canal: {self.canal}, Ligada: {self.ligada}"

tv = Tv(32)
print(tv)
tv.ligada = True
tv.canal = 4
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
print(tv)
