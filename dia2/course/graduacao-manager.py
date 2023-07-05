import csv

with open('graduacao_unb.csv', encoding = "utf-8") as file:
    graduacao_reader = csv.reader(file, delimiter = ",", quotechar='"')

    # Usando o conceito de desempacotamento * restante
    header, *data = graduacao_reader

    print(data)