import pygame
import random
import time
from datetime import datetime



pygame.init()
pygame.mixer.init()

hojas = pygame.sprite.Group()


global xInicial, yInicial
xInicial, yInicial = 300, 100
anchura, altura  = 1200, 600

class framework_ventana():
    def __init__(self, anchura, altura):
        self.anchura, self.altura = anchura, altura
        self.ventana = pygame.display.set_mode((self.anchura, self.altura)) #es una tupla lleva 2 parentesis
        self.titulo = pygame.display.set_caption("Pato juego")


        self.reloj = pygame.time.Clock()


        
    def acabaFrame(self):
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                return True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return True



    def empiezaFrame(self):
        self.ventana.fill((184, 252, 250)) #color de la ventana 
        
    def actualizaFrame(self):
        fps = self.reloj.tick(60)
        pygame.display.flip() #actualiza la ventana

class framework_personaje():
    def __init__(self, ventana, anchura, altura):

        dir = "sprite/"
        self.personaje = [pygame.image.load(dir + "1.png"), pygame.image.load(dir + "1.png"), pygame.image.load(dir + "1.png"), 
        pygame.image.load(dir + "2.png"), pygame.image.load(dir + "2.png"), pygame.image.load(dir + "2.png"), 
        pygame.image.load(dir + "3.png"), pygame.image.load(dir + "3.png"), pygame.image.load(dir + "3.png"), 
        pygame.image.load(dir + "4.png"), pygame.image.load(dir + "4.png"), pygame.image.load(dir + "4.png"),
        pygame.image.load(dir + "5.png"), pygame.image.load(dir + "5.png"), pygame.image.load(dir + "5.png"),
        pygame.image.load(dir + "6.png"), pygame.image.load(dir + "6.png"), pygame.image.load(dir + "6.png"),
        pygame.image.load(dir + "7.png"), pygame.image.load(dir + "7.png"), pygame.image.load(dir + "7.png"),
        pygame.image.load(dir + "8.png"), pygame.image.load(dir + "8.png"), pygame.image.load(dir + "8.png")]

        self.personajeSprite = pygame.sprite.Sprite()
        self.personajeSprite.image = self.personaje
        self.personajeSprite.rect = self.personaje[0].get_rect()
        self.personajeSprite.rect.x = xInicial
        self.personajeSprite.rect.y = yInicial

        self.anchuraPersonaje = self.personaje[0].get_width()
        self.alturaPersonaje = self.personaje[0].get_height()
        self.ventana = ventana

        self.contador = 0

        self.anchura, self.altura = anchura, altura

        self.estatico = True
        self.enMovimiento = False


    def dibujar(self):
        global xInicial, yInicial

        if self.enMovimiento:
            self.ventana.blit(self.personaje[self.contador], (xInicial, yInicial))

            if self.contador == 23:
                self.contador = 0

            else:
                self.contador += 1

        if self.estatico:
            self.ventana.blit(self.personaje[0], (xInicial, yInicial))

    def movimiento(self):
        global xInicial, yInicial

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            xInicial += 4
            self.enMovimiento = True
            self.estatico = False

        elif keys[pygame.K_LEFT]:
            xInicial -= 4
            self.enMovimiento = True
            self.estatico = False

        else:
            self.enMovimiento = False
            self.estatico = True


        if keys[pygame.K_DOWN]:
            yInicial += 4
            self.enMovimiento = True
            self.estatico = False
        
        if keys[pygame.K_UP]:
            yInicial -= 4
            self.enMovimiento = True
            self.estatico = False

        #mientras el personaje este dentro de los limites no se mueve a la posición 1   
        if not(xInicial > 0 and xInicial < self.anchura):
            xInicial = 1
            


        if not(yInicial > 0 - (self.alturaPersonaje/2) / 2):
            yInicial = 1

        if not(yInicial < self.altura - self.alturaPersonaje):
            yInicial = self.altura - self.alturaPersonaje



    def colision(self, hojas):
        if (pygame.sprite.spritecollideany(self.personaje, hojas)):
            print("esta colisionando")


class mapa_framework():
    def __init__(self, ventana, anchura, altura, xPersonaje, yPersonaje):
        self.ventana = ventana
        self.anchura = anchura
        self.altura = altura
        dirFondos = "Fondos/"
        self.niveles = [pygame.image.load(dirFondos + "1.jpg"), pygame.image.load(dirFondos + "2.jpg"), pygame.image.load(dirFondos + "3.jpg"),
                        pygame.image.load(dirFondos + "4.jpg"), pygame.image.load(dirFondos + "5.jpg"), pygame.image.load(dirFondos + "6.jpg"), 
                        pygame.image.load(dirFondos + "7.jpg")]
        #print(len(self.niveles))

        self.nuevoNivel = False
        self.contadorNiveles = -1

        self.dirMusica = "Musica/"

        #en el constructor solo se da el atributo 1 vez. luego no se actualiza.
    
    def siguiente_nivel(self):

        if self.contadorNiveles == len(self.niveles) -1:
            self.contadorNiveles = -1
        
        if xInicial > self.anchura - 5:
            self.contadorNiveles += 1
            self.nuevoNivel = True

        if self.nuevoNivel:
            self.ventana.blit(self.niveles[self.contadorNiveles], (0, 0))


        #print(xInicial, self.anchura, self.contadorNiveles)


    def activa_musica(self):
        pygame.mixer.music.load("AroundTheWorld.mp3")
        pygame.mixer.music.set_volume(20)
        pygame.mixer.music.play()

class menu_framework():
    def __init__(self, ventana):
        self.ventana = ventana
        transicion = 5 

        dirMenu = "Menu/"
        self.imagenMenu = [pygame.image.load(dirMenu + "1.jpg"), pygame.image.load(dirMenu + "2.jpg"), pygame.image.load(dirMenu + "3.jpg"),
                        pygame.image.load(dirMenu + "4.jpg"), pygame.image.load(dirMenu + "5.jpg")]

        self.empieza = False
        self.X, self.Y = 0, 0

    def acabaMenu(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.empieza = True




    def dibuja(self):

        self.ventana.blit(random.choice(self.imagenMenu), (self.X, self.Y)) 
        time.sleep(0.2)

        #start = datetime.now()
        #time.sleep(2)
        #end = datetime.now()

        #print(str(end - time))

class enemigo_framework():
    def __init__(self, ventana, anchura, altura):
        global xInicialE, yInicialE

        dirEnemigos = "enemigos/"
        self.hoja = pygame.image.load(dirEnemigos + "hoja.png")
        


        self.anchuraHoja = self.hoja.get_width()
        self.alturaHoja = self.hoja.get_height()

        self.anchura = anchura
        self.altura = altura

        self.ventana = ventana

        self.fuera = False


        xInicialE, yInicialE = self.anchura + self.anchuraHoja, random.randrange(self.alturaHoja, self.altura) #se suma la anchura de la hoja al borde de la ventana para que salga fuera

        self.hojaSprite = pygame.sprite.Sprite()
        self.hojaSprite.image = self.hoja
        self.hojaSprite.rect = self.hoja.get_rect()
        self.hojaSprite.rect.x = xInicialE
        self.hojaSprite.rect.y = yInicialE

        hojas.add(self.hojaSprite)

    def movimiento_hoja(self):
        global xInicialE, yInicialE

        xInicialE -= 10

        if xInicialE < 0:
            self.fuera = True
            xInicialE = self.anchura + self.anchuraHoja
        
    

    def dibuja(self):
        global xInicialE, yInicialE
        
        if self.fuera:
            xInicialE, yInicialE = self.anchura + self.anchuraHoja, random.randrange(0, self.altura - self.alturaHoja) #se suma la anchura de la hoja al borde de la ventana para que salga fuera
            self.fuera = False

        self.ventana.blit(self.hoja, (xInicialE, yInicialE))
        






ventana = framework_ventana(anchura, altura)
obtenVentana = ventana.ventana



personaje = framework_personaje(obtenVentana, anchura, altura)
mapa = mapa_framework(obtenVentana, anchura, altura, xInicial, yInicial)
menu = menu_framework(obtenVentana)
enemigo = enemigo_framework(obtenVentana, anchura, altura)


mapa.activa_musica()
while not ventana.acabaFrame():
    if menu.empieza:
        ventana.empiezaFrame()
        mapa.siguiente_nivel()
        personaje.dibujar()
        personaje.movimiento()
        personaje.colision(hojas)
        enemigo.movimiento_hoja()
        enemigo.dibuja()


    else:
        menu.dibuja()
        menu.acabaMenu()

    ventana.actualizaFrame()


    #print(menu.empieza)


