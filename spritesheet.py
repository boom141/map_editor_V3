import pygame, os

class Spritesheet():
	def __init__(self,root_folder):
		self.root_folder = root_folder
		self.sub_folder = os.listdir(root_folder)
		self.current_folder = None
		self.current_component = None
		self.buttons_color = 'white'
		self.current_button = -1
		self.highlight_color = (25,25,25)
		self.highlight_index = None

	def Folder_Selection(self,surface):
		buttons = []
		for i, folder in enumerate(self.sub_folder):
			if self.current_button == i:
				self.buttons_color = 'grey'
			else:
				self.buttons_color = 'white'

			Font = pygame.font.Font(os.path.join('font', 'Minecraft.ttf'), 15)
			folder_name = Font.render(folder, False, self.buttons_color)

			pygame.draw.line(surface, ((255,255,255)), (0,180),(250,180), 2)
			button = pygame.draw.rect(surface, ((25,25,25)), (30,(i+2)*20,150,20), 1)
			buttons.append(button)            
			surface.blit(folder_name,(30, (i+2)*20))

		self.Folder_Button_Selection(buttons)

	def Folder_Button_Selection(self,buttons):
		for button in buttons:
			if button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
				self.current_button = buttons.index(button)
				self.current_folder = self.sub_folder[buttons.index(button)]
				self.current_component = None
				self.highlight_index = None

	def Folder_Component(self,surface):
		buttons = []
		if self.current_folder != None:
			components = os.listdir(f'{self.root_folder}/{self.current_folder}/')
			if components:
				for i,component in enumerate(components):
					image = pygame.image.load(os.path.join(f'{self.root_folder}/{self.current_folder}/', component))
					image_copy = image.copy()
					image_copy = pygame.transform.scale(image, (35,35))
					image_copy.set_colorkey((0,0,0))
					if i == self.highlight_index:
						self.highlight_color = (0,255,0)
					else:
						self.highlight_color = (25,25,25)
					button = pygame.draw.rect(surface, self.highlight_color, (30,(i+5)*38,37,37),1)
					buttons.append(button)
					surface.blit(image_copy, (30, (i+5)*38))
		
			self.Component_Button_Selection(buttons,components)
	
	def Component_Button_Selection(self,buttons,components):
		for button in buttons:
			if button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
				self.current_component = components[buttons.index(button)]
				self.highlight_index = buttons.index(button)
				

spritesheet = Spritesheet('images/')