import re

# Leitura do arquivo geral

codigo_file = open('codigo.txt', 'r')
data = codigo_file.read()

palavras_reservadas = re.findall('(prog|programa\b|int|imprima|leia|se|entao|para\b|fimprog|algoritmo|aleatorio|arquivo|ate|caso|e\b|escreva|faca|falso|verdadeiro|inicio|nao|ou|pausa|repita|retorne|se nao|var|vetor)', data)
numeros = re.findall('[^a-zA-Z+0-9][0-9]+', data)
strings = re.findall('\"(.*?)\"', data)
sinais_operacao = re.findall("(=|\+|-|\*|/|<|>|<=|>=)", data)
identificadores = re.findall('[_a-zA-Z][_a-zA-Z0-9]*', data)
outros = re.findall('\W', data)

codigo_file.close()

# Leitura por linha

texto = open('codigo.txt', 'r')
linhas = texto.readlines()

codigo_file.close()