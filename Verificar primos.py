# Programa para verificar a quantidade de números primos até o número desejado
# Números primos são aqueles que só possuem 2 divisores com resto 0, sendo eles o número 1 e ele mesmo
# Exemplo, até o número 30 há 10 primos, sendo eles 2, 3, 5, 7, 11, 13, 17, 19, 23 e 29, porque
#   todos eles só podem divididos por 1 e por eles mesmos restando 0 como resultado da divisão

import time

numero = int(input('Digite até que número deseja verificar se é primo: '))
primos = []
comparacoes = 0
tempo_normal = float()
tempo_impar = float()
tempo_metade = float()
tempo_primo = float()
tempo_raiz = float()

def resultados(tempo):
    print(f'Tempo: {tempo:2f} segundos')
    print(f'Comparações: {comparacoes}')
    print(f'Quantidade de primos: {len(primos)}')
    # print(f'Números primos: {primos}')  # Caso deseje ver os números primos na tela
    print('')

def metodo_normal():
    global comparacoes, tempo_normal
    comparacoes = 0
    primos.clear()
    inicio = time.time()
    for i in range(2, numero + 1):
        eh_primo = True
        for j in range(2, i):
            comparacoes += 1
            if i % j == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(i)
    fim = time.time()
    print('Método NORMAL')
    tempo_normal = fim - inicio
    resultados(tempo_normal)

def metodo_impar():    
    global comparacoes, tempo_impar
    comparacoes = 0
    primos.clear()
    inicio = time.time()
    for i in range(3, numero + 1, 2):
        eh_primo = True
        for j in range(3, i, 2):
            comparacoes += 1
            if i % j == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(i)
    primos.insert(0, 2)
    fim = time.time()
    print('Método ÍMPAR')
    tempo_impar = fim - inicio
    resultados(tempo_impar)

def metodo_metade():
    global comparacoes, tempo_metade
    comparacoes = 0
    primos.clear()
    primos.append(2)
    inicio = time.time()
    for i in range(3, numero + 1, 2):
        eh_primo = True
        for j in range(3, (i // 2) + 1, 2):
            comparacoes += 1
            if i % j == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(i)
    fim = time.time()
    print('Método METADE')
    tempo_metade = fim - inicio
    resultados(tempo_metade)

def metodo_primos():
    global comparacoes, tempo_primo
    comparacoes = 0
    primos.clear()
    primos.append(3)
    inicio = time.time()
    for i in range(5, numero + 1, 2):
        eh_primo = True
        for j in primos:
            if j > (i // 2):
                break
            comparacoes += 1
            if i % j == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(i)
    primos.insert(0, 2)
    fim = time.time()
    print('Método PRIMOS')
    tempo_primo = fim - inicio
    resultados(tempo_primo)

def metodo_raiz():
    global comparacoes, tempo_raiz
    comparacoes = 0
    primos.clear()
    primos.append(3)
    inicio = time.time()
    for i in range(5, numero + 1, 2):
        eh_primo = True
        for j in primos:
            if j > (i ** 0.5):
                break
            comparacoes += 1
            if i % j == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(i)
    primos.insert(0, 2)
    fim = time.time()
    print('Método RAIZ')
    tempo_raiz = fim - inicio
    resultados(tempo_raiz)

def compara_tempos():
    global tempo_normal, tempo_impar, tempo_metade, tempo_primo, tempo_raiz
    if tempo_raiz == 0:
        print('Impossível dividir por 0')
    else:
        print(f'O método raiz foi {(tempo_normal / tempo_primo):.2f} vezes mais rápido que o normal')
        print(f'Ele também foi {(tempo_impar / tempo_primo):.2f} vezes mais rápido que o ímpar')
        print(f'{(tempo_metade / tempo_primo):.2f} vezes mais rápido que o metade')
        printf(f'E ainda foi {(tempo_metade / tempo_primo):.2f} vezes mais rápido que o primo')

metodo_normal()     # Analisa todos os números (método mais lento)
metodo_impar()      # Analisa apenas números ímpares (afinal, nenhum número par é primo, com exceção do 2)
metodo_metade()     # Analisa apenas números ímpares até a metade da lista (afinal, nunca há divisor inteiro após a metade)
metodo_primos()     # Analisa apenas números ímpares primos até a metade da lista (afinal, multiplicando-se primos elimina-se os não primos)
metodo_raiz()       # Analisa apenas números ímpares primos menores que a raiz do valor analisado
compara_tempos()    # Para comparar quantas vezes o método primo é mais rápido que os outros

input('Aperte ENTER para sair...')
