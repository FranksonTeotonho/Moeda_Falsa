def moeda_forca_bruta(moedas):

    n = len(moedas)

    for i in range(n):
        for j in range (n):
            if(j != i):
                print('Moeda atual: \n \tPosição: ',i,', Valor: ', moedas[i])
                print('Moeda sendo comparada: \n \tPosição: ', j, ', Valor: ', moedas[j] ,'\n')
                if(moedas[i] > moedas[j]):
                    return i

def soma(elementos):

    sum = 0

    for i in range(len(elementos)):
        sum = sum + elementos[i]

    return sum


def moeda_divisao_conquista(moedas, start,end):

    n = end - start + 1
    print("\nstart: ",start)
    print("end: ", end)
    print("n: ",n,"\n")

    if n == 1:
        print("---caso base---")
        return start
    else:
        if(n%2 == 0):
            print("\n -----par----- \n")
            meio = (n // 2) + start

            pesoEsquerdo = soma(moedas[start:meio])
            print(pesoEsquerdo)
            pesoDireito = soma(moedas[meio:end+1])
            print(pesoDireito)

            if(pesoEsquerdo > pesoDireito):
                return moeda_divisao_conquista(moedas,start,meio-1)
            if(pesoDireito > pesoEsquerdo):
                moeda_divisao_conquista(moedas,meio,end)

        else:
            print("\n -----impar----- \n")
            meio = (n//2) + start

            pesoEsquerdo = soma(moedas[start:meio])
            print(pesoEsquerdo)
            pesoDireito = soma(moedas[meio+1:end+1])
            print(pesoDireito)

            if (pesoEsquerdo == pesoDireito):
                return meio
            if(pesoEsquerdo > pesoDireito):
                return moeda_divisao_conquista(moedas, start, meio - 1)
            if(pesoDireito > pesoEsquerdo):
                return moeda_divisao_conquista(moedas, meio + 1, end)

def main():

    moedas = [10,10,10,10,11,10,10,10,10]

    print("A moeda falsa esta na posição: ",moeda_divisao_conquista(moedas,0,5))


if __name__ == '__main__':
    main()