import pygame, os

class Game_map():
    def __init__(self):
        pass

    def Labels(self,surface,layer):
        Font = pygame.font.Font(os.path.join('font', 'Minecraft.ttf'), 20)
        coordinates = Font.render(f"X:{pygame.mouse.get_pos()[0]} | Y:{pygame.mouse.get_pos()[1]}",False,'white')
        layer = Font.render(f'Layer: {layer + 1}', False,'white')
        Font1 = pygame.font.Font(os.path.join('font', 'Minecraft.ttf'), 20)
        selection = Font1.render('Image Selection',False,'white')

        surface.blit(selection, (50, 10))
        surface.blit(layer, (260, 10))
        surface.blit(coordinates, (260, 30))
    
    def Initialized_Grid(self,dimensions,tile_size):
        layer = []
        for y in range(0,dimensions[1],tile_size):
            row = []
            for x in range(0,dimensions[0],tile_size):
                row.append(-1)
            layer.append(row)
        return layer

    def Render_Map(self,map):
        pass