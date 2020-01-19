import pygame
from time import sleep
from random import choice, randint

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)

pygame.init()

altura = 600
largura = 800

relogio = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
fonte = pygame.font.SysFont('impact', 30)
pygame.display.set_caption('Pong')

def texto(mensagem, cor, x, y):
    texto = fonte.render(mensagem, True, cor)
    tela.blit(texto, [x, y])

def pause(tempo):
    sleep(tempo)

def jogo():
    TelaInicio = True
    Jogador2 = False
    controles = False
    Jogador1 = False

    barra2X = 380
    barra2Y = 70

    barraX = 380
    barraY = 530

    bolaX = 380
    bolaY = 270

    scoreJogador1 = 0
    scoreJogador2 = 0

    aumentoVelocidadeBola = 0
    velocidade_bola_x = 0
    velocidade_bola_y = 0

    velocidadeX = 0
    velocidade2X = 0

    direção_velocidade_bola = [2.5, -2.5]

    # Tela do Inicio
    while TelaInicio:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x > 192 and y > 187 and x < 580 and y < 282:
                    Jogador1 = True
                if x > 191 and y > 318 and x < 580 and y < 410:
                    Jogador2 = True
                if x > 192 and y > 445 and x < 582 and y < 532:
                    controles = True

        tela.fill(branco)
        imagem = pygame.image.load('telaInicio.jpg')
        tela.blit(imagem, (0, 0))
        pygame.display.update()

        # Tela modo 2 jogadores
        while Jogador2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocidadeX -= 8 + ((velocidadeX ** 2)) ** (1/2)
                    if event.key == pygame.K_RIGHT:
                        velocidadeX += 8 + ((velocidadeX ** 2)) ** (1/2)
                    if event.key == pygame.K_UP:
                        velocidadeX = 0
                    if event.key == pygame.K_a:
                        velocidade2X -= 8 + ((velocidade2X ** 2)) ** (1/2)
                    if event.key == pygame.K_d:
                        velocidade2X += 8 + ((velocidade2X ** 2)) ** (1/2)
                    if event.key == pygame.K_w:
                        velocidade2X = 0
                    if event.key == pygame.K_p:
                        pause(5)
                    if event.key == pygame.K_c:
                        if velocidade_bola_x == 0 and velocidade_bola_y == 0:
                            velocidade_bola_y = choice(direção_velocidade_bola)
                            velocidade_bola_x = choice(direção_velocidade_bola)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]

                    if x >= 0 and y >= 0 and x <= 50 and y <= 50:
                        jogo()


            tela.fill(branco)
            # Objetos
            objetoJogador1 = pygame.draw.rect(tela, preto, [barraX, barraY, 100, 20])
            objetoBola = pygame.draw.rect(tela, preto, [bolaX, bolaY, 20, 20])
            objetoJogador2 = pygame.draw.rect(tela, preto, [barra2X, barra2Y, 100, 20])

            # Colisão da bola com o jogador 1
            if objetoJogador1.colliderect(objetoBola):
                forcaResultanteBola = 2.5 + aumentoVelocidadeBola
                velocidade_bola_y -= forcaResultanteBola + (aumentoVelocidadeBola + 2.5)
                velocidade_bola_x -= velocidadeX
                # força que a bola vem mais a força que eu quero que ela volte
                aumentoVelocidadeBola += 1

            # Colisão da bola com o jogador 2
            if objetoJogador2.colliderect(objetoBola):
                forcaResultanteBola = 2.5 + aumentoVelocidadeBola
                velocidade_bola_y += forcaResultanteBola + (aumentoVelocidadeBola + 2.5)
                velocidade_bola_x -= velocidade2X
                # força que a bola vem mais a força que eu quero que ela volte
                aumentoVelocidadeBola += 0.1

            barraX += velocidadeX
            bolaY += velocidade_bola_y
            bolaX += velocidade_bola_x
            barra2X += velocidade2X

            # SCORE
            imagem = pygame.image.load('divisão.png')
            tela.blit(imagem, (0, 292))
            texto('SCORE: {}'.format(scoreJogador1), preto, 10, 300)
            texto('SCORE: {}'.format(scoreJogador2), preto, 10, 250)

            # Botão de voltar
            imagem2 = pygame.image.load('botãoVoltar.jpg')
            tela.blit(imagem2, (0, 0))

            relogio.tick(60)
            # Jogador 2 faz gol
            if bolaY > 580:
                bolaY = 270
                bolaX = 380
                velocidade_bola_y = 0
                velocidade_bola_x = 0
                aumentoVelocidadeBola = 0
                scoreJogador2 += 1

            # Jogador 1 faz gol
            if bolaY < 20:
                bolaY = 270
                bolaX = 380
                velocidade_bola_y = 0
                velocidade_bola_x = 0
                aumentoVelocidadeBola = 0
                scoreJogador1 += 1

            # Bola ricocheteia na parede
            if bolaX > 780:
                velocidade_bola_x -= 8
            if bolaX < 20:
                velocidade_bola_x += 8

            # Barra do Jogador 1 bate na parede e para
            if barraX > 700:
                barraX = 700
                velocidadeX = 0
            if barraX < 0:
                barraX = 0
                velocidadeX = 0

            # Barra do Jogador 2 bate na parede e para
            if barra2X > 700:
                barra2X = 700
                velocidade2X = 0
            if barra2X < 0:
                barra2X = 0
                velocidade2X = 0

            # Impede que a velocidade da bola ultrapasse 10
            if velocidade_bola_y > 10:
                velocidade_bola_y = 10
            if velocidade_bola_y < -10:
                velocidade_bola_y = -10
            if velocidade_bola_x > 10:
                 velocidade_bola_x = 10
            if velocidade_bola_x < -10:
                velocidade_bola_x = -10

            # Imede que a velocidade da barra do jogador 1 ultrapasse 5
            if velocidadeX > 8:
                velocidadeX = 8
            if velocidadeX < -8:
                velocidadeX = -8

            # Impede que a barra do jogador 2 ultrapasse 5
            if velocidade2X > 8:
                velocidade2X = 8
            if velocidade2X < -8:
                velocidade2X = -8

            pygame.display.update()

        # Tela modo 1 Jogador
        while Jogador1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    # Movimento do jogador
                    if event.key == pygame.K_LEFT:
                        velocidadeX -= 8 + ((velocidadeX ** 2)) ** (1/2)
                    if event.key == pygame.K_RIGHT:
                        velocidadeX += 8 + ((velocidadeX ** 2)) ** (1/2)
                    if event.key == pygame.K_UP:
                        velocidadeX = 0
                    if event.key == pygame.K_p:
                        pause(5)

                    # Lança uma nova bola
                    if event.key == pygame.K_c:
                        if velocidade_bola_y == 0 and velocidade_bola_x == 0:
                            velocidade_bola_y = choice(direção_velocidade_bola)
                            velocidade_bola_x = choice(direção_velocidade_bola)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]

                    if x >= 0 and y >= 0 and x <= 50 and y <= 50:
                        jogo()


            tela.fill(branco)
            barraX += velocidadeX
            barra2X += velocidade2X
            bolaX += velocidade_bola_x
            bolaY += velocidade_bola_y

            # SCORE
            imagem = pygame.image.load('divisão.png')
            tela.blit(imagem, (0, 292))
            texto('SCORE: {}'.format(scoreJogador1), preto, 10, 300)
            texto('SCORE: {}'.format(scoreJogador2), preto, 10, 250)

            # Botão de voltar
            imagem2 = pygame.image.load('botãoVoltar.jpg')
            tela.blit(imagem2, (0, 0))

            # Objetos
            objetoJogador1 = pygame.draw.rect(tela, preto, [barraX, barraY, 100, 20])
            objetoBola = pygame.draw.rect(tela, preto, [bolaX, bolaY, 20, 20])
            objetoJogador2 = pygame.draw.rect(tela, preto, [barra2X, barra2Y, 100, 20])

            # Colisão da bola com o jogador 1
            if objetoJogador1.colliderect(objetoBola):
                forcaResultanteBola = 2.5 + aumentoVelocidadeBola
                velocidade_bola_y -= forcaResultanteBola + (aumentoVelocidadeBola + 2.5)
                velocidade_bola_x -= velocidadeX
                # força que a bola vem mais a força que eu quero que ela volte
                aumentoVelocidadeBola += 1

            # Colisão da bola com o bot
            if objetoJogador2.colliderect(objetoBola):
                forcaResultanteBola = 2.5 + aumentoVelocidadeBola
                velocidade_bola_y += forcaResultanteBola + (aumentoVelocidadeBola + 2.5)
                velocidade_bola_x -= velocidade2X
                # força que a bola vem mais a força que eu quero que ela volte
                aumentoVelocidadeBola += 0.1

            relogio.tick(60)

            # Jogador 2 faz gol
            if bolaY > 580:
                bolaY = 270
                bolaX = 380
                velocidade_bola_y = 0
                velocidade_bola_x = 0
                aumentoVelocidadeBola = 0
                scoreJogador2 += 1

            # Jogador 1 faz gol
            if bolaY < 20:
                bolaY = 270
                bolaX = 380
                velocidade_bola_y = 0
                velocidade_bola_x = 0
                aumentoVelocidadeBola = 0
                scoreJogador1 += 1

            # Bola ricocheteia na parede
            if bolaX > 780:
                velocidade_bola_x -= 8
            if bolaX < 20:
                velocidade_bola_x += 8

            # Barra do Jogador 1 bate na parede e para
            if barraX > 700:
                barraX = 700
                velocidadeX = 0
            if barraX < 0:
                barraX = 0
                velocidadeX = 0

            # Barra do bot bate na parede e para
            if barra2X > 700:
                barra2X = 700
                velocidade2X = 0
            if barra2X < 0:
                barra2X = 0
                velocidade2X = 0

            # Impede que a barra do Jogador 1 ultrapasse 8
            if velocidadeX > 8:
                velocidadeX = 8
            if velocidadeX < -8:
                velocidadeX = -8

            # Impede que a barra do bot ultrapasse 8
            if velocidade2X > 8:
                velocidade2X = 8
            if velocidade2X < -8:
                velocidade2X = -8

            # Impede que a velocidade da bola ultrapasse 10
            if velocidade_bola_y > 10:
                velocidade_bola_y = 10
            if velocidade_bola_y < -10:
                velocidade_bola_y = -10
            if velocidade_bola_x > 10:
                velocidade_bola_x = 10
            if velocidade_bola_x < -10:
                velocidade_bola_x = -10

            # Bot segue a bola
            if randint(1, 99) >= 20: # porcentagem de chance de atraso
                # Segue a bola
                if bolaX > barra2X:
                    velocidade2X += 8
                if bolaX < barra2X:
                    velocidade2X -= 8
            else:
                # Evita a bola
                if bolaX < barra2X:
                    velocidade2X += 8
                if bolaX > barra2X:
                    velocidade2X -= 8

            pygame.display.update()

        # Tela que exibe os controles
        while controles:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]

                    if x >= 0 and y >= 0 and x <= 50 and y <= 50:
                        jogo()

            tela.fill(branco)

            # Imagem da Tela
            imagem = pygame.image.load('controlesImagem.jpg')
            tela.blit(imagem, (0, 0))

            # Botão de voltar
            imagem2 = pygame.image.load('botãoVoltar.jpg')
            tela.blit(imagem2, (0, 0))


            pygame.display.update()

jogo()
