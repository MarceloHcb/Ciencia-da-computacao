My_list = []

My_list.append('um')
My_list.append('dois')
My_list.append('tres')
quantidade = len(My_list)
len(My_list)
print(My_list)
print('Quantidade',quantidade)
index = 0
while index < quantidade:
    print(My_list[index])
    index = index + 1

for item in reversed(My_list):
    print(item)
