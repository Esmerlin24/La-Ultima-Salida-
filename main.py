# Nombre: Esmerlin Severino Paredes
# Matrícula: 24-EISN-2-033

# Importe la libreria para el hacer el juego y para que cierre bien.
import pygame
import sys 

# Inicie pygame para que mi juego corra 
pygame.init()

# Para que el juego se vea en pantalla completa
Pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("La Ultima Salida")

# Para controlar el tiempo 
Reloj = pygame.time.Clock()
Velocida = 60

# Para controlar si el juego sigue abierto y realizar lo que es pantalla completa.
jugando = True 
En_pantalla_completa = True

# Voy a declarar mi variable para el menu y los botones.
situacion = "Menu"
boton_iniciar = pygame.Rect(400, 250, 200, 60)
boton_reiniciar = pygame.Rect(400, 250, 200, 60)
boton_volver = pygame.Rect(400, 330, 200, 60)


while jugando:
    # Para el menu.
 if situacion == "Menu":

    
    for acontecimiento in pygame.event.get():

     if acontecimiento.type == pygame.QUIT:
        jugando = False
# Detectar el mouse 
        if acontecimiento.type == pygame.MOUSEBUTTONDOWN:

         if situacion == "menu":
          if boton_iniciar.collidepoint(acontecimiento.pos):
            situacion = "jugando"

     elif situacion == "game_over":
        if boton_reiniciar.collidepoint(acontecimiento.pos):
            situacion = "jugando"

        if boton_volver.collidepoint(acontecimiento.pos):
            situacion = "menu"


    if acontecimiento.type == pygame.KEYDOWN:
        if acontecimiento.key == pygame.K_ESCAPE:

            if En_pantalla_completa:
                Pantalla = pygame.display.set_mode((1500, 700))
                En_pantalla_completa = False
            else:
                
                Pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                En_pantalla_completa = True

# Para pintar pintar mi fondo y actualizar la pantalla 
Pantalla.fill((0, 0, 0))
pygame.display.flip()   
Reloj.tick(Velocida)  

jugando = False  

     

#Para cerrar la ventana 
pygame.quit()
sys.exit()


