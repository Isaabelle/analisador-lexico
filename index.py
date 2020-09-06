from Leitura import *

count = 0
vetor_palavras_reservadas = []
vetor_numeros = []
vetor_strings = []
vetor_sinais_operacao = []
vetor_identificadores = []
vetor_outros = []

for n in linhas:
    linha = linhas[count]
    qtd_palavras_reservadas = len(palavras_reservadas)
    for i in range(qtd_palavras_reservadas):
        aux = palavras_reservadas[i]
        palavra = linha.find(aux)
        if palavra is not  -1:
            vetor = ['Palavra reservada', aux, (palavra+1), (count+1)  ]
            if vetor in vetor_palavras_reservadas:
                break
            else:
                vetor_palavras_reservadas.append(vetor)


    qtd_numeros = len(numeros)
    for i in range(qtd_numeros):
        aux = numeros[i]
        palavra = linha.find(aux)
        if palavra is not -1:
            vetor = ['Numero', aux, (palavra + 2), (count + 1)]
            if vetor in vetor_numeros:
                break
            else:
                vetor_numeros.append(vetor)

    qtd_strings = len(strings)
    for i in range(qtd_strings):
        aux = strings[i]
        palavra = linha.find(aux)
        if palavra is not -1:
            vetor = ['String', aux, (palavra + 1), (count + 1)]
            if vetor in vetor_strings:
                break
            else:
                vetor_strings.append(vetor)

    qtd_sinais_operacao = len(sinais_operacao)
    for i in range(qtd_sinais_operacao):
        aux = sinais_operacao[i]
        palavra = linha.find(aux)
        if palavra is not -1:
            vetor = ['Sinais de operaçao', aux, (palavra + 1), (count + 1)]
            if vetor in vetor_sinais_operacao:
                break
            else:
                vetor_sinais_operacao.append(vetor)

    qtd_identificadores = len(identificadores)
    for i in range(qtd_identificadores):
        aux =identificadores[i]
        palavra = linha.find(aux)
        if palavra is not -1:
            vetor = ['Identificadores', aux, (palavra + 1), (count + 1)]
            verificacao_palavra_reservada = ['Palavra reservada', aux, (palavra + 1), (count + 1)]
            verificacao_strings = ['String', aux, (palavra + 1), (count + 1)]
            if vetor in vetor_identificadores:
                break
            elif verificacao_palavra_reservada in vetor_palavras_reservadas:
                break
            elif verificacao_strings in vetor_strings:
                break
            else:
                vetor_identificadores.append(vetor)

    qtd_outros = len(outros)
    for i in range(qtd_outros):
        aux = outros[i]
        palavra = linha.find(aux)
        if palavra is not -1:
            vetor = ['Outro', aux, (palavra + 1), (count + 1)]
            verificacao_sinais_operacao = ['Sinais de operaçao', aux, (palavra + 1), (count + 1)]
            if vetor in vetor_outros:
                break
            elif verificacao_sinais_operacao in vetor_sinais_operacao:
                break
            else:
                vetor_outros.append(vetor)


    count += 1



print(vetor_palavras_reservadas)
print('\n')

print(vetor_numeros)
print('\n')

print(vetor_strings)
print('\n')

print(vetor_sinais_operacao)
print('\n')

print(vetor_identificadores)
print('\n')

print(vetor_outros)


