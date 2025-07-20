# Programa para verificar a quantidade de números primos até o número desejado
# Números primos são aqueles que só possuem 2 divisores com resto 0, sendo eles o número 1 e ele mesmo
# Exemplo, até o número 30 há 10 primos, sendo eles 2, 3, 5, 7, 11, 13, 17, 19, 23 e 29, porque
#   todos eles só podem divididos por 1 e por eles mesmos restando 0 como resultado da divisão

numero = int(input('Digite até que número deseja verificar se é primo: '))
primos = []
comparacoes = 0

def resultados():
    print(f'Comparações: {comparacoes}')
    print(f'Quantidade de primos: {len(primos)}')
    print(f'Números primos: {primos}\n')

def metodo_normal():
    global comparacoes
    comparacoes = 0
    primos.clear()
    for i in range(2, numero + 1):
        eh_primo = True
        for j in range(2, i):
            comparacoes += 1
            if i % j == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(i)
    print('Método NORMAL')
    resultados()

def metodo_impar():    
    global comparacoes
    comparacoes = 0
    primos.clear()
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
    print('Método ÍMPAR')
    resultados()

def metodo_metade():
    global comparacoes
    comparacoes = 0
    primos.clear()
    primos.append(2)
    for i in range(3, numero + 1, 2):
        eh_primo = True
        for j in range(3, (i // 2) + 1, 2):
            comparacoes += 1
            if i % j == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(i)
    print('Método METADE')
    resultados()

def metodo_primos():
    global comparacoes
    comparacoes = 0
    primos.clear()
    primos.append(3)
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
    print('Método PRIMOS')
    resultados()

metodo_normal()     # Analisa todos os números (método mais lento)
metodo_impar()      # Analisa apenas números ímpares (afinal, nenhum número par é primo, com exceção do 2)
metodo_metade()     # Analisa apenas números ímpares até a metade da lista (afinal, nunca há divisor inteiro após a metade)
metodo_primos()     # Analisa apenas números ímpares primos até a metade da lista (afinal, multiplicando-se primos elimina-se os não primos)

input('Aperte ENTER para sair...')
