import re

codigo_file = open('codigo.txt', 'r')
data = codigo_file.read()

palavras_reservadas = re.findall('(prog|int|imprima|leia|se|entao|para|fimprog|algoritmo|aleatorio|arquivo|ate|caso|e|escreva|faca|falso |verdadeiro|inicio|nao|ou|pausa|repita|retorne|se nao|var|vetor)', data)
numeros = re.findall('[^a-zA-Z+0-9][0-9]+', data)
strings = re.findall('\"(.*?)\"', data)
sinais_operacao = re.findall("(=|\+|-|\*|/)", data)
identificadores = re.findall('[_a-zA-Z][_a-zA-Z0-9]*', data)


print (palavras_reservadas)
print (numeros)
print (strings)
print(sinais_operacao)
print(identificadores)

codigo_file.close()