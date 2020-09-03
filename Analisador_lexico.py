from Leitura import *

count = 0
vetor_palavras_reservadas = []
vetor_numeros = []
vetor_strings = []
vetor_sinais_operacao = []
vetor_identificadores = []

for n in linhas:
    linha = linhas[count]
    qtd_palavras_reservadas = len(palavras_reservadas)
    for i in range(qtd_palavras_reservadas):
        aux = palavras_reservadas[i]
        palavra = linha.find(aux)
        if palavra is not  -1:
            vetor = ['Palavra reservada', aux, (palavra+1), (count+1)  ]
            vetor_palavras_reservadas.append(vetor)

    qtd_numeros = len(numeros)
    for i in range(qtd_numeros):
        aux = numeros[i]
        palavra = linha.find(aux)
        if palavra is not -1:
            vetor = ['Numero', aux, (palavra + 1), (count + 1)]
            vetor_numeros.append(vetor)

    qtd_sinais_operacao = len(sinais_operacao)
    for i in range(qtd_sinais_operacao):
        aux = sinais_operacao[i]
        palavra = linha.find(aux)
        if palavra is not -1:
            vetor = ['Sinais de operaçao', aux, (palavra + 1), (count + 1)]
            vetor_sinais_operacao.append(vetor)

    qtd_identificadores = len(identificadores)
    for i in range(qtd_identificadores):
        aux =identificadores[i]
        palavra = linha.find(aux)
        if palavra is not -1:
            vetor = ['identificadores', aux, (palavra + 1), (count + 1)]
            vetor_identificadores.append(vetor)
    count += 1

print(vetor_palavras_reservadas)
print(palavras_reservadas)
print('\n')

print(vetor_numeros)
print(numeros)
print('\n')

print(vetor_strings)
print(strings)
print('\n')

print(vetor_sinais_operacao)
print(sinais_operacao)
print('\n')

print(vetor_identificadores)
print(identificadores)