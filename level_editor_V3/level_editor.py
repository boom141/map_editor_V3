import pygame, time, sys
from core_classes import*
from spritesheet import*
from map_loader import*
from pygame.locals import *

pygame.init()


WINDOW_DIMENSION = (800,600)
LAYER_DIMENSION = (1000,800)
SPEED = 5
LAYER_COUNT = 5
TILE_SIZE = 16

window = pygame.display.set_mode(WINDOW_DIMENSION)
layers = []
for i in range(LAYER_COUNT):
	layers.append(pygame.Surface(LAYER_DIMENSION, pygame.SRCALPHA))
spritesheet_section = pygame.Surface((250,600))
fps = pygame.time.Clock()
last_time = time.time()
scroll = [0,0]

up,down,left,right = False,False,False,False
change_layer = False

current_layer = LAYER_COUNT
clicked_once = 0

map_data = game_map.Map_Data(LAYER_DIMENSION,TILE_SIZE,LAYER_COUNT)


while True:
# surface fill -----------------------------------------------------------#
	window.fill((0,0,0))
	for index, layer in enumerate(layers):
		layer.fill((0,0,0))
		layer.set_colorkey((0,0,0))
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

# load map ---------------------------------------------------------------#
	if pygame.key.get_pressed()[K_l]:
		map_data = map_loader.Load('save_map/map.json')

# features ---------------------------------------------------------------#
	spritesheet.Folder_Selection(spritesheet_section)
	spritesheet.Folder_Component(spritesheet_section)
	
	if change_layer and clicked_once == 0:
		current_layer -= 1
		if current_layer <= 0:
			current_layer = LAYER_COUNT
		clicked_once = 1
	

	if mouse[0] > spritesheet_section.get_width() and pygame.MOUSEMOTION:
		if pygame.mouse.get_pressed()[0]:
		# draw on to surface --------------------------------------------#
			if map_data[f'DATA {current_layer - 1}'][gridy][gridx] == [-1]:
				map_data[f'DATA {current_layer - 1}'][gridy][gridx] = [(current_layer - 1),spritesheet.current_folder,spritesheet.current_component,gridx*TILE_SIZE,gridy*TILE_SIZE]
		# erase image from the surface ----------------------------------#	
		if pygame.mouse.get_pressed()[2]:
			if map_data[f'DATA {current_layer - 1}'][gridy][gridx] != [-1]:
				map_data[f'DATA {current_layer - 1}'][gridy][gridx] = [-1]

	game_map.Render_Map(map_data,layers)
	
	if pygame.key.get_pressed()[K_SPACE]:
		game_map.Save_Map(map_data)

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
			if event.key == pygame.K_DOWN:
				change_layer = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:    
				up = False
			if event.key == pygame.K_s:
				down = False
			if event.key == pygame.K_a:
				left = False
			if event.key == pygame.K_d:
				right = False
			if event.key == pygame.K_DOWN:
				change_layer = False
				clicked_once = 0

	for layer in layers:
		window.blit(layer, (scroll[0],scroll[1]))
		window.blit(spritesheet_section, (0,0))

	game_map.Labels(window,current_layer)
	
	pygame.display.update()
	fps.tick(60)


