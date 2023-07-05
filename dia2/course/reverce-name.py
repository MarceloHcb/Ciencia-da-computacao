def reverce_name(name):
    for n in range(len(name)):
        for index in range(len(name) - n):
            print(name[index], end='')
        print()

if __name__ == "__main__":
    name = input("Digite um nome: ")
    reverce_name(name)
