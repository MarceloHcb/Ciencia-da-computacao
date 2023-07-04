notas_ana = [("matematica", 8.5), ("portugues", 10), ("historia", 9.5), ("geografia", 9)]

def media_notas(notas):
    soma = 0
    quantidade = len(notas)
    
    for nota in notas:
        soma += nota[1]
        
    media = soma / quantidade
    return int(media)

print(media_notas(notas_ana))

notas_ana = [("matematica", 8.5), ("portugues", 10), ("historia", 9.5), ("geografia", 9)]

def media_notas(notas):
    soma = sum(nota[1] for nota in notas) 
    
    quantidade = len(notas)
    media = soma / quantidade
    return int(media)

print(media_notas(notas_ana))

