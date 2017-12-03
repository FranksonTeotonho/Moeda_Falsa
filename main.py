import pygame,sys, os, time

#Inicializando pygame
pygame.init()


#Função responsavel por carregar imagens
def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join('resource', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print ('Cannot load image:', fullname)
        pass

    return image, image.get_rect()

#Algoritmo força bruta
def moeda_forca_bruta(moedas,backgroud):

    n = len(moedas)

    for i in range(n):
        for j in range (n):
            if(j != i):
                print('Moeda atual: \n \tPosição: ',i,', Valor: ', moedas[i])
                print('Moeda sendo comparada: \n \tPosição: ', j, ', Valor: ', moedas[j] ,'\n')
                if(moedas[i] > moedas[j]):
                    return i

#Função auxiliar que soma os pesos
def soma(elementos):

    sum = 0

    for i in range(len(elementos)):
        sum = sum + elementos[i]

    return sum

#Algoritmo por decremento e conquista
def moeda_decremento_conquista(moedas, start,end):

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
            print('O peso do lado esquerdo é: ', pesoEsquerdo)
            pesoDireito = soma(moedas[meio:end+1])
            print('O peso do lado direito é: ', pesoDireito)

            if(pesoEsquerdo > pesoDireito):
                return moeda_decremento_conquista(moedas,start,meio-1)
            if(pesoDireito > pesoEsquerdo):
                return moeda_decremento_conquista(moedas,meio,end)

        else:
            print("\n -----impar----- \n")
            meio = (n//2) + start

            pesoEsquerdo = soma(moedas[start:meio])
            print('O peso do lado esquerdo é: ' ,pesoEsquerdo)
            pesoDireito = soma(moedas[meio+1:end+1])
            print('O peso do lado direito é: ' ,pesoDireito)

            if (pesoEsquerdo == pesoDireito):
                return meio
            if(pesoEsquerdo > pesoDireito):
                return moeda_decremento_conquista(moedas, start, meio - 1)
            if(pesoDireito > pesoEsquerdo):
                return moeda_decremento_conquista(moedas, meio + 1, end)

#Funcao principal
def main():

    moedas = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,10,10,10]

    # Initialise screen
    screen = pygame.display.set_mode((800, 600))
    #Title
    pygame.display.set_caption('Moeda falsa')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    backgroundImage, backgroundImageRect = load_png("dollar.png")
    background.blit(backgroundImage, backgroundImageRect)

    #Loading Imagens

    #Balanças Left
    balanceLeft, balanceLeftRect = load_png("balance_left_heavy.png")
    balanceLeftPile, balanceLeftPileRect  = load_png("balance_left_heavy_pile_coins.png")
    balanceLeftSingle, balanceLeftSingle = load_png("balance_left_heavy_single coin.png")

    #Balanças Right
    balanceRight, balanceRightRect = load_png("balance_right_heavy.png")
    balanceRightPile, balanceRightPileRect = load_png("balance_right_heavy_pile_coins.png")
    balanceRightSingle, balanceRightSingle = load_png("balance_right_heavy_singlecoin.png")

    #Balanças Equal
    balanceEqual, balanceEqualRect = load_png("balance_equal.png")
    balanceEqualPile, balanceEqualPileRect = load_png("balance_equal_pile_coins.png")
    balanceEqualSingle, balanceEqualSingle = load_png("balance_equal_single_coin.png")

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_b):
                    time.sleep(2)
                    background.blit(backgroundImage, backgroundImageRect)
                    background.blit(balanceLeft, (75, 100))
                if( event.key == pygame.K_d):
                    time.sleep(2)
                    background.blit(backgroundImage, backgroundImageRect)
                    background.blit(balanceLeftPile, (75, 100))
                if (event.key == pygame.K_LEFT):
                    background.blit(backgroundImage, backgroundImageRect)
                    background.blit(balanceLeft, (75, 100))
                if (event.key == pygame.K_RIGHT):
                    background.blit(backgroundImage, backgroundImageRect)
                    background.blit(balanceRight, (75, 100))
                if (event.key == pygame.K_UP):
                    background.blit(backgroundImage, backgroundImageRect)
                    background.blit(balanceEqual, (75, 100))

        screen.blit(background, (0, 0))
        pygame.display.flip()

#Execução
if __name__ == '__main__':
    main()