import pygame, time, sys
from core_classes import*
from spritesheet import*
from pygame.locals import *

pygame.init()


WINDOW_DIMENSION = (800,600)
LAYER_DIMENSION = (100,100)
SPEED = 5
LAYER_COUNT = 5
TILE_SIZE = 16

window = pygame.display.set_mode(WINDOW_DIMENSION)
layers = []
for i in range(LAYER_COUNT):
	layers.append(pygame.Surface(LAYER_DIMENSION))
spritesheet_section = pygame.Surface((250,600))
fps = pygame.time.Clock()
last_time = time.time()
scroll = [0,0]

up,down,left,right = False,False,False,False

current_layer = 0

grid = Game_map().Initialized_Grid(LAYER_DIMENSION,TILE_SIZE)

map = {}
for i in range(LAYER_COUNT):
	map[f'LAYER {i+1}'] = grid.copy()

while True:
# surface fill -----------------------------------------------------------#
	window.fill((45,45,45))
	for layer in layers:
		layer.fill((0,0,0))
	spritesheet_section.fill((25,25,25))

# framerate independence -------------------------------------------------#
	dt = time.time() - last_time
	dt *= 60
	last_time = time.time()

# coordinates ------------------------------------------------------------#
	mouse = pygame.mouse.get_pos()
	gridx = int((mouse[0] - scroll[0])/TILE_SIZE)
	gridy = int((mouse[1] - scroll[1])/TILE_SIZE)

# move surface -----------------------------------------------------------#
	move = [0,0]
	if up:
		move[1] -= SPEED * dt
	if down:
		move[1] += SPEED * dt
	if left:
		move[0] -= SPEED * dt
	if right:
		move[0] += SPEED * dt

	scroll[0] +=  move[0]
	scroll[1] +=  move[1]

# features ---------------------------------------------------------------#
	spritesheet.Folder_Selection(spritesheet_section)
	spritesheet.Folder_Component(spritesheet_section)

# event handler ----------------------------------------------------------#   

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == pygame.K_w:    
				up = True
			if event.key == pygame.K_s:
				down = True
			if event.key == pygame.K_a:
				left = True
			if event.key == pygame.K_d:
				right = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:    
				up = False
			if event.key == pygame.K_s:
				down = False
			if event.key == pygame.K_a:
				left = False
			if event.key == pygame.K_d:
				right = False

	for layer in layers:
		window.blit(layer, (scroll[0],scroll[1]))
		window.blit(spritesheet_section, (0,0))

	Game_map().Labels(window,current_layer)
	
	pygame.display.update()
	fps.tick(60)


