import pygame,sys, os

pygame.init()

#Algoritmo força bruta
def moeda_forca_bruta(moedas):

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
    backgroundImage, backgroundImageSquare = load_png("dollar.png")
    background.blit(backgroundImage, backgroundImageSquare)

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
                    print("A moeda falsa esta na posição[B]: ", moeda_forca_bruta(moedas))
                if( event.key == pygame.K_d):
                    print("A moeda falsa esta na posição[D]: ", moeda_decremento_conquista(moedas, 0, 18))

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()