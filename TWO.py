import pygame
import time
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO, ALTO = 600, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Snake")

# Colores (RGB)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (213, 50, 80)
VERDE = (0, 255, 0)

# Configuraciones de la serpiente
TAMANIO_BLOQUE = 20
VELOCIDAD = 12

reloj = pygame.time.Clock()
fuente = pygame.font.SysFont("bahnschrift", 25)

def mostrar_puntuacion(puntuacion):
    valor = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
    pantalla.blit(valor, [10, 10])

def dibujar_serpiente(tamanio_bloque, lista_serpiente):
    for bloque in lista_serpiente:
        pygame.draw.rect(pantalla, VERDE, [bloque[0], bloque[1], tamanio_bloque, tamanio_bloque])

def juego():
    game_over = False
    game_close = False

    # Posición inicial de la serpiente
    x = ANCHO / 2
    y = ALTO / 2

    # Cambios de posición
    x_cambio = 0
    y_cambio = 0

    lista_serpiente = []
    largo_serpiente = 1

    # Posición inicial de la comida (alineada a la cuadrícula del bloque)
    comida_x = round(random.randrange(0, ANCHO - TAMANIO_BLOQUE) / 20.0) * 20.0
    comida_y = round(random.randrange(0, ALTO - TAMANIO_BLOQUE) / 20.0) * 20.0

    while not game_over:

        # Pantalla de Game Over
        while game_close:
            pantalla.fill(NEGRO)
            msg = fuente.render("Perdiste. C para jugar de nuevo o Q para salir", True, ROJO)
            pantalla.blit(msg, [ANCHO / 6, ALTO / 3])
            mostrar_puntuacion(largo_serpiente - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        juego()

        # Registro de controles de teclado
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and x_cambio == 0:
                    x_cambio = -TAMANIO_BLOQUE
                    y_cambio = 0
                elif evento.key == pygame.K_RIGHT and x_cambio == 0:
                    x_cambio = TAMANIO_BLOQUE
                    y_cambio = 0
                elif evento.key == pygame.K_UP and y_cambio == 0:
                    y_cambio = -TAMANIO_BLOQUE
                    x_cambio = 0
                elif evento.key == pygame.K_DOWN and y_cambio == 0:
                    y_cambio = TAMANIO_BLOQUE
                    x_cambio = 0

        # Validar colisión con los bordes de la pantalla
        if x >= ANCHO or x < 0 or y >= ALTO or y < 0:
            game_close = True

        x += x_cambio
        y += y_cambio
        pantalla.fill(NEGRO)

        # Dibujar la comida
        pygame.draw.rect(pantalla, ROJO, [comida_x, comida_y, TAMANIO_BLOQUE, TAMANIO_BLOQUE])
        
        # Actualizar el cuerpo de la serpiente
        cabeza_serpiente = [x, y]
        lista_serpiente.append(cabeza_serpiente)
        if len(lista_serpiente) > largo_serpiente:
            del lista_serpiente[0]

        # Validar colisión consigo misma
        for bloque in lista_serpiente[:-1]:
            if bloque == cabeza_serpiente:
                game_close = True

        dibujar_serpiente(TAMANIO_BLOQUE, lista_serpiente)
        mostrar_puntuacion(largo_serpiente - 1)

        pygame.display.update()

        # Validar si la serpiente come la fruta
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, ANCHO - TAMANIO_BLOQUE) / 20.0) * 20.0
            comida_y = round(random.randrange(0, ALTO - TAMANIO_BLOQUE) / 20.0) * 20.0
            largo_serpiente += 1

        reloj.tick(VELOCIDAD)

    pygame.quit()
    quit()

if __name__ == "__main__":
    juego()
