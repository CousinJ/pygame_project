import pygame
import os







#generic button class

class Button():
    width = 200
    height = 50
    def __init__(self, x, y,color) -> None:
        width = Button.width
        height = Button.height
        self.rect = (x, y, width, height)
        self.color = color
    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, self.rect)




#background class
  
class BackGround():
    def __init__(self, image):
        print(os.getcwd())
        self.image = pygame.image.load(image)

    def resize(self, sw, sh):
       self.image = pygame.transform.scale(self.image, (sw, sh))

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, (0,0))






#title UI element  note: center 500 and 100 control its x and y pos.

class Title:
    width = 600
    height = 150

    def __init__(self, color, font_path, font_size, text, x, y):
        self.color = color
        self.font_path = font_path
        self.font_size = font_size
        self.text = text
        font_obj = pygame.font.Font(self.font_path, self.font_size)
        text_color = (0, 0, 0)
        self.text_surface = font_obj.render(text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center=(x, y))
        
    def draw(self, screen, ):
        pygame.draw.rect(screen, (255, 255, 255), self.text_rect)
        screen.blit(self.text_surface, self.text_rect)
        
       
  