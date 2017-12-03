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

class Moeda_falsa():

    #Fontes
    font = pygame.font.Font(None, 60)
    result = pygame.font.Font(None, 100)
    # Loading Imagens

    backgroundImage, backgroundImageRect = load_png("dollar.png")

    # Balanças Left
    balanceLeft, balanceLeftRect = load_png("balance_left_heavy.png")
    balanceLeftPile, balanceLeftPileRect = load_png("balance_left_heavy_pile_coins.png")
    balanceLeftSingle, balanceLeftSingleRect = load_png("balance_left_heavy_single coin.png")

    # Balanças Right
    balanceRight, balanceRightRect = load_png("balance_right_heavy.png")
    balanceRightPile, balanceRightPileRect = load_png("balance_right_heavy_pile_coins.png")
    balanceRightSingle, balanceRightSingleRect = load_png("balance_right_heavy_singlecoin.png")

    # Balanças Equal
    balanceEqual, balanceEqualRect = load_png("balance_equal.png")
    balanceEqualPile, balanceEqualPileRect = load_png("balance_equal_pile_coins.png")
    balanceEqualSingle, balanceEqualSingleRect = load_png("balance_equal_single_coin.png")

    def __init__(self):
        # Initialise screen
        self.screen = pygame.display.set_mode((800, 600))
        # Title
        pygame.display.set_caption('Moeda falsa')

        # Fill background
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.cleanScreen()
        self.resetScreen()

        # Blit everything to the screen
        self.render()

    #Algoritmo força bruta
    def moeda_forca_bruta(self, moedas):

        n = len(moedas)

        for i in range(n):
            for j in range (n):
                if(j != i):
                    print('Moeda atual: \n \tPosição: ',i,', Valor: ', moedas[i])
                    print('Moeda sendo comparada: \n \tPosição: ', j, ', Valor: ', moedas[j] ,'\n')

                    time.sleep(1)
                    self.resetScreen()
                    self.cleanScreen()
                    self.background.blit(self.balanceEqual, (75, 100))
                    self.render()

                    if((moedas[i] > moedas[j]) or (moedas[i] < moedas[j])):
                        if(moedas[i] > moedas[j]):
                            time.sleep(1)
                            self.resetScreen()
                            self.cleanScreen()
                            self.label(indice=str(i), posicao=(120, 70))
                            self.label(indice=str(j), posicao=(520, 70))
                            self.background.blit(self.balanceLeftSingle, (75, 100))
                            self.render()

                            aux = i
                        elif(moedas[i] < moedas[j]):
                            time.sleep(1)
                            self.resetScreen()
                            self.cleanScreen()
                            self.label(indice=str(i), posicao=(120, 70))
                            self.label(indice=str(j), posicao=(520, 70))
                            self.background.blit(self.balanceRightSingle, (75, 100))
                            self.render()

                            aux = j



                    else:

                        time.sleep(1)
                        self.resetScreen()
                        self.cleanScreen()
                        self.label(indice=str(i), posicao=(120, 70))
                        self.label(indice=str(j), posicao=(520, 70))
                        self.background.blit(self.balanceEqualSingle, (75, 100))
                        self.render()

        print("A moeda falsa é: ",aux)
        time.sleep(1)
        self.resetScreen()
        self.cleanScreen()
        self.showResult(indice = str(aux))
        self.render()
        time.sleep(3)

        #Holder
        time.sleep(1)
        self.resetScreen()
        self.cleanScreen()
        self.showResult(indice=str(aux))
        self.render()
        time.sleep(5)

    #Função auxiliar que soma os pesos
    def soma(self, elementos):

        sum = 0

        for i in range(len(elementos)):
            sum = sum + elementos[i]

        return sum

    #Algoritmo por decremento e conquista
    def moeda_decremento_conquista(self, moedas, start,end):

        n = end - start + 1
        print("\nstart: ",start)
        print("end: ", end)
        print("n: ",n,"\n")

        if n == 1:
            print("---caso base---")
            print("A moeda falsa é: ", start)

            time.sleep(1)
            self.resetScreen()
            self.cleanScreen()
            self.showResult(indice=str(start))
            self.render()
            time.sleep(3)

            #Holder
            time.sleep(1)
            self.resetScreen()
            self.cleanScreen()
            self.showResult(indice=str(start))
            self.render()
            time.sleep(5)

            return start
        else:
            if(n%2 == 0):
                print("\n -----par----- \n")
                meio = (n // 2) + start

                pesoEsquerdo = self.soma(elementos = moedas[start:meio])
                print('O peso do lado esquerdo é: ', pesoEsquerdo)
                pesoDireito = self.soma(elementos = moedas[meio:end+1])
                print('O peso do lado direito é: ', pesoDireito)

                time.sleep(1)
                self.resetScreen()
                self.cleanScreen()
                self.background.blit(self.balanceEqual, (75, 100))
                self.render()

                if(pesoEsquerdo > pesoDireito):
                    time.sleep(1)
                    self.resetScreen()
                    self.cleanScreen()
                    self.label2(indice=str(pesoEsquerdo), posicao=(120, 70))
                    self.label2(indice=str(pesoDireito), posicao=(520, 70))
                    self.background.blit(self.balanceLeftPile, (75, 100))
                    self.render()

                    return self.moeda_decremento_conquista(moedas = moedas,start = start,end = meio-1)
                if(pesoDireito > pesoEsquerdo):
                    time.sleep(1)
                    self.resetScreen()
                    self.cleanScreen()
                    self.label2(indice=str(pesoEsquerdo), posicao=(120, 70))
                    self.label2(indice=str(pesoDireito), posicao=(520, 70))
                    self.background.blit(self.balanceRightPile, (75, 100))
                    self.render()

                    return self.moeda_decremento_conquista(moedas = moedas,start = meio,end = end)

            else:
                print("\n -----impar----- \n")
                meio = (n//2) + start

                pesoEsquerdo = self.soma(elementos = moedas[start:meio])
                print('O peso do lado esquerdo é: ' ,pesoEsquerdo)
                pesoDireito = self.soma(elementos = moedas[meio+1:end+1])
                print('O peso do lado direito é: ' ,pesoDireito)

                time.sleep(1)
                self.resetScreen()
                self.cleanScreen()
                self.background.blit(self.balanceEqual, (75, 100))
                self.render()

                if (pesoEsquerdo == pesoDireito):
                    time.sleep(1)
                    self.resetScreen()
                    self.cleanScreen()
                    self.label2(indice=str(pesoEsquerdo), posicao=(120, 70))
                    self.label2(indice=str(pesoDireito), posicao=(520, 70))
                    self.background.blit(self.balanceEqualPile, (75, 100))
                    self.render()

                    return meio
                if(pesoEsquerdo > pesoDireito):
                    time.sleep(1)
                    self.resetScreen()
                    self.cleanScreen()
                    self.label2(indice=str(pesoEsquerdo), posicao=(120, 70))
                    self.label2(indice=str(pesoDireito), posicao=(520, 70))
                    self.background.blit(self.balanceLeftPile, (75, 100))
                    self.render()

                    return self.moeda_decremento_conquista(moedas = moedas,start = start,end = meio - 1)
                if(pesoDireito > pesoEsquerdo):
                    time.sleep(1)
                    self.resetScreen()
                    self.cleanScreen()
                    self.label2(indice=str(pesoEsquerdo), posicao=(120, 70))
                    self.label2(indice=str(pesoDireito), posicao=(520, 70))
                    self.background.blit(self.balanceRightPile, (75, 100))
                    self.render()

                    return self.moeda_decremento_conquista(moedas = moedas,start = meio + 1, end = end)

    def render(self):
        pygame.display.flip()

    def resetScreen(self):
        self.screen.blit(self.background, (0, 0))

    def cleanScreen(self):
        self.background.blit(self.backgroundImage, self.backgroundImageRect)

    def label(self,indice, posicao):
        # Display some text
        text = self.font.render("Moeda: "+ indice , 1, (10,10,10))
        self.background.blit(text, posicao)

    def label2(self, indice, posicao):
        # Display some text
        text = self.font.render("Peso: " + indice, 1, (10, 10, 10))
        self.background.blit(text, posicao)

    def showResult(self, indice):

        text = self.result.render("A Moeda falsa é: " + indice, 1, (10, 10, 10))
        self.background.blit(text, (100,250))

#Funcao principal
def main():

    moedas = [10,10,10,11,10]

    mf = Moeda_falsa()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_b):
                    mf.moeda_forca_bruta(moedas)
                elif(event.key == pygame.K_d):
                    mf.moeda_decremento_conquista(moedas = moedas,start=0,end =4)

    mf.resetScreen()
    mf.render()

#Execução
if __name__ == '__main__':
    main()