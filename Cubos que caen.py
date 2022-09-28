import pygame
import sys
import random

pygame.init()

anchura = 800
altura = 600

puntos = 0

rojo = (255,0,0)
negro = (0,0,0)
azul = (0,0,255)
blanco = (255,255,255)

tamaño_J = 50
posicion_J = [anchura/2, altura-2*tamaño_J]

tamaño_O = 50 #tamaño del oponente
posicion_O = [random.randint(0, anchura-tamaño_O),0]
lista_O = [posicion_O]
NdO = 10 #Número de oponentes

VdC = 7 #VdC significa Velocidad de Caída

screen = pygame.display.set_mode((anchura, altura))

game_over = False

clock = pygame.time.Clock()

fuente = pygame.font.SysFont("monospace", 35)

def bajar_O(lista_O):
	hack = random.random()
	if len(lista_O) < NdO and hack < 0.25:
		lista_O.append([random.randint(0, anchura - tamaño_O),0])

def dibujar_O(lista_O):
	for posicion_O in lista_O:
			pygame.draw.rect(screen, azul, (posicion_O[0], posicion_O[1], tamaño_O, tamaño_O))

def actualizar_posicion_O(lista_O, puntos):
	for idx, posicion_O in enumerate(lista_O):
		if posicion_O[1] >= 0 and posicion_O[1] < altura:
			posicion_O[1] += VdC
		else:
			lista_O.pop(idx)
			puntos += 1
	return puntos

#def my_game_my_colision_detection(posicion_J,posicion_O): #detector de colisiones usando valores absolutos porque el del video no me gustaba
#	if abs(posicion_J[1] - posicion_O[1]) < tamaño_J and  abs(posicion_J[0] - posicion_O[0]) < tamaño_J:
#		return True
#	return False
#
#def detectar_colision(posicion_J, posicion_O): #detector de colisiones usado en el video
#	if (posicion_O[1] >= posicion_J[1] and posicion_O[1] < (posicion_J[1] + tamaño_J)) or (posicion_J[1] >= posicion_O[1] and posicion_J[1] < (posicion_O[1] + tamaño_O)):
#		if (posicion_O[0] >= posicion_J[0] and posicion_O[0] < (posicion_J[0] + tamaño_J)) or (posicion_J[0] >= posicion_O[0] and posicion_J[0] < (posicion_O[0] + tamaño_O)):
#			return True
#
#def colision(lista_O, posicion_J):
#	for posicion_O in lista_O:
#		if abs(posicion_J[1] - posicion_O[1]) < tamaño_J and  abs(posicion_J[0] - posicion_O[0]) < tamaño_J:
#			return True
#		return False


while not game_over:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			x = posicion_J[0]
			y = posicion_J[1]
			if event.key == pygame.K_LEFT and posicion_J[0] >= 0 + tamaño_J:
				x -= tamaño_J
			elif event.key == pygame.K_RIGHT and posicion_J[0] < anchura - tamaño_J:
				x += tamaño_J
			posicion_J = [x,y]

	screen.fill(negro)

	bajar_O(lista_O)
	dibujar_O(lista_O)
	puntos = actualizar_posicion_O(lista_O, puntos)
	texto = "Puntos:" + str(puntos)
	label = fuente.render(texto, 1, blanco)
	screen.blit(label, (0, altura-40))
	pygame.draw.rect(screen, rojo, (posicion_J[0], posicion_J[1], tamaño_J, tamaño_J))
	for element in lista_O:
		if abs(posicion_J[1] - element[1]) < tamaño_J and  abs(posicion_J[0] - element[0]) < tamaño_J:
			game_over = True
			break

	VdC = (puntos/15)+5

	if puntos > 80:
		NdO = 12
	elif puntos >150:
		NdO = 15

	clock.tick(30)

	pygame.display.update()
print(puntos)