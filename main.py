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


def moeda_divisao_conquista(moedas, start, end):


    tamanho = len(moedas[start:end+1])
    print(tamanho)

    if(tamanho%2 == 0):

        somaPrimeiraParte = soma(moedas[start:tamanho//2])
        somaSegundaParte = soma(moedas[tamanho//2:end+1])

        print("soma primeira parte: ",somaPrimeiraParte)
        print("soma segunda parte: ", somaSegundaParte)

        if (somaPrimeiraParte > somaSegundaParte):
            print("Ta na primeira parte")
            return moeda_divisao_conquista(moedas, start, (tamanho//2) - 1)
        elif (somaPrimeiraParte < somaSegundaParte):
            print("Ta na segunda parte")
            return moeda_divisao_conquista(moedas,tamanho//2, end)

    elif(tamanho%2 == 1):
        if(tamanho != 1):
            somaPrimeiraParte = soma(moedas[start:tamanho // 2])
            somaSegundaParte = soma(moedas[(tamanho // 2)+1:end + 1])

            TermoMeio = moedas[tamanho//2]

            PosicaoTermoMeio = tamanho//2

            print("soma primeira parte: ", somaPrimeiraParte)
            print("soma segunda parte: ", somaSegundaParte)
            print("peso termo central: ",TermoMeio)
            print("posicao: ",PosicaoTermoMeio)

            if(somaPrimeiraParte == somaSegundaParte):
                print("É o elemento central")
                return PosicaoTermoMeio
            elif(somaPrimeiraParte > somaSegundaParte):
                print("Ta na primeira parte")
            elif (somaPrimeiraParte < somaSegundaParte):
                print("Ta na segunda parte")
        elif(tamanho == 1):
            return end

def main():

    moedas = [10,10,10,11,10]

    print("moeda falsa")


if __name__ == '__main__':
    main()