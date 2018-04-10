# Encoding: UTF-8
# Sebastian Morales martin
# Proyecto final

import pygame

# Dimensiones de la pantalla
ANCHO = 640
ALTO = 480
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

def dibujarMenu(fondo, boton1, boton2, ventana):
    ventana.blit(fondo, (0,0))
    ventana.blit(boton1.image, boton1.rect)
    ventana.blit(boton2.image, boton2.rect)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana de dibujo
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución

    #imagenes
    imgFondo = pygame.image.load('fondoMenu.jpg')
    imgJuego = pygame.image.load('fondoJuego.png')
    imgBtnSupreme = pygame.image.load('supreme.png')
    imgBtnEE = pygame.image.load('easterEgg.png')
    imgBtnPlay = pygame.image.load('play.png')
    
    #Sprites
    spriteBtnSupreme = pygame.sprite.Sprite()
    spriteBtnSupreme.image = imgBtnSupreme
    spriteBtnSupreme.rect = imgBtnSupreme.get_rect()
    spriteBtnSupreme.rect.left = ANCHO//2 - 128
    spriteBtnSupreme.rect.top = 100
    #-----------------------
    spriteBtnEE = pygame.sprite.Sprite()
    spriteBtnEE.image = imgBtnEE
    spriteBtnEE.rect = imgBtnEE.get_rect()
    spriteBtnEE.rect.left = ANCHO//2 - 128
    spriteBtnEE.rect.top = 200

    while not termina:  # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        pygame.draw.rect(ventana, VERDE_BANDERA, (30, 30, ANCHO - 60, ALTO - 60), 5)
        pygame.draw.circle(ventana, ROJO, (ANCHO // 2, ALTO // 2), 200, 2)
        pygame.draw.line(ventana, AZUL, (0,ALTO//2), (ANCHO,ALTO//2))
        dibujarMenu(imgFondo, spriteBtnSupreme, spriteBtnEE, ventana)

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    dibujar()


main()