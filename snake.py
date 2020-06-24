
# Importar pacotes
import pygame
from pygame.locals import *
import random

# Inicializar pygame
try:
	pygame.init()
except:
	("O módulo Pygame não foi inicializado")

# Definir tamanho da tela
altura = 450
largura = 450

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake")

# Limitar FPS
clock = pygame.time.Clock()

# funcao para gerar valores aleatorios sempre dentro do grid 10
def on_grid_random():
	x = random.randint(0,largura - 10)
	y = random.randint(0,altura - 10)

	return (x//10 * 10, y//10 * 10)

# funcao para definir colisao entre agentes
def collision(c1,c2):
	return (c1[0] == c2[0]) and (c1[1] == c2[1])

# Parametros
up = 0
right = 1
down = 2
left = 3

# tamanho da cobra
snake = [(200,200), (210, 200), (220,200)]
my_direction = left

# desenhar cobra
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255)) # branco

# desenhar maça
apple_skin = pygame.Surface((10,10))
apple_skin.fill((255,0,0)) # vermelho

# posicionar maça - valores aleatorios
apple_pos = on_grid_random()

# inserir pontuacao
font = pygame.font.Font('freesansbold.ttf', 20)
score = 0

game_over = False
# Loop infinito para rogar o jogo
while not game_over:
	clock.tick(10)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()

		# controlar cobra
		if event.type == KEYDOWN:
			if event.key == K_UP or event.key == K_w and my_direction != down:
				my_direction = up
			if event.key == K_DOWN or event.key == K_s and my_direction != up:
				my_direction = down
			if event.key == K_RIGHT or event.key == K_d and my_direction != left:
				my_direction = right
			if event.key == K_LEFT or event.key == K_a and my_direction != right:
				my_direction = left

	# verificar colisao com maça
	if collision(snake[0], apple_pos):
		apple_pos = on_grid_random()
		snake.append((0,0))
		score = score + 1

	# checar colisao com as bordas da tela
	if snake[0][0] == largura or snake[0][1] == altura or snake[0][0] < 0 or snake[0][1] < 0:
		game_over = True
		break

	# checar se a cobra nao colide com ela mesma
	for i in range(1, len(snake) - 1):
		if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
			game_over = True
			break

	# Game over
	if game_over:
		break

	# definir complemento do movimento - iniciando pelo "rabo"
	for i in range(len(snake) - 1, 0, -1):
		snake[i] = (snake[i - 1][0], snake[i - 1][1])

	# movimento
	if my_direction == up:
		snake[0] = (snake[0][0], snake[0][1] - 10)
	if my_direction == down:
		snake[0] = (snake[0][0], snake[0][1] + 10)
	if my_direction == right:
		snake[0] = (snake[0][0] + 10, snake[0][1])
	if my_direction == left:
		snake[0] = (snake[0][0] - 10, snake[0][1])

	

	# limpar a tela
	screen.fill((0,0,0))

	# posicioar maça
	screen.blit(apple_skin,apple_pos)

	# posicioar cobra
	for pos in snake:
		screen.blit(snake_skin,pos)

	# desenhar linhas da tela
	# horizontal
	pygame.draw.line(screen, (0, 0, 255), (0+5,0+5), (0+5, altura-5))
	pygame.draw.line(screen, (0, 0, 255), (largura-5, 0+5), (largura-5, altura-5))

	# vertical
	pygame.draw.line(screen, (0, 0, 255), (0+5,0+5), (largura-5, 0+5))
	pygame.draw.line(screen, (0, 0, 255), (0+5, altura-5), (largura-5, altura-5))

	

	# Inserir texto
	score_font = font.render('Pontuação: %s' %(score), True, (255,255,255))
	score_rect = score_font.get_rect()
	score_rect.topleft = ((largura/3), 10)
	screen.blit(score_font, score_rect)

	pygame.display.update()


while True:
	
	game_over_font = pygame.font.Font('freesansbold.ttf', 75)
	game_over_screen = game_over_font.render('Game Over', True, (255, 0, 0))
	game_over_rect = game_over_screen.get_rect()
	game_over_rect.midtop = (largura / 2, altura / 2)
	screen.blit(game_over_screen, game_over_rect)

	# desenhar linhas da tela
	# horizontal
	pygame.draw.line(screen, (255, 0, 0), (0+5,0+5), (0+5, altura-5))
	pygame.draw.line(screen, (255, 0, 0), (largura-5, 0+5), (largura-5, altura-5))

	# vertical
	pygame.draw.line(screen, (255, 0, 0), (0+5,0+5), (largura-5, 0+5))
	pygame.draw.line(screen, (255, 0, 0), (0+5, altura-5), (largura-5, altura-5))


	pygame.display.update()
	pygame.time.wait(500)
	while True:
	    for event in pygame.event.get():
	        if event.type == QUIT:
	            pygame.quit()
	            exit()


        
