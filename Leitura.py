import re

# Leitura do arquivo geral

codigo_file = open('codigo.txt', 'r')
data = codigo_file.read()

palavras_reservadas = re.findall('(prog|int|imprima|leia|se|entao|para|fimprog|algoritmo|aleatorio|arquivo|ate|caso|e|escreva|faca|falso|verdadeiro|inicio|nao|ou|pausa|repita|retorne|se nao|var|vetor|\n)', data)
numeros = re.findall('[^a-zA-Z+0-9][0-9]+', data)
strings = re.findall('\"(.*?)\"', data)
sinais_operacao = re.findall("(=|\+|-|\*|/)", data)
identificadores = re.findall('[_a-zA-Z][_a-zA-Z0-9]*', data)
outros = 'null'

codigo_file.close()

# Leitura por linha

texto = open('codigo.txt', 'r')
linhas = texto.readlines()

codigo_file.close()