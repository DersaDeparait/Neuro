from pygame import time
import pygame
import os

class Monitor:
    def __init__(self) -> None:
        super().__init__()

        self.display_position = (50, 30)
        self.display_size = (1700, 1030)
        self.display_color = (48, 189, 221)
        self.fps_default = 240
        self.is_show_info: bool = True

        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % self.display_position
        pygame.init()

        self.display = pygame.display.set_mode(self.display_size)
        self.display.fill(self.display_color)

        self.clock = time.Clock()
        self.clock.tick(self.fps_default)


    def control_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # sys.exit() if sys is imported
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN: pass
                if event.key == pygame.K_UP: pass
                if event.key == pygame.K_LEFT: pass
                if event.key == pygame.K_RIGHT: pass
                if event.key == pygame.K_SPACE: pass
                if event.key == pygame.K_z: pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN: pass
                if event.key == pygame.K_UP: pass
                if event.key == pygame.K_LEFT: pass
                if event.key == pygame.K_RIGHT: pass
                if event.key == pygame.K_SPACE: pass
                if event.key == pygame.K_z: pass






    def draw(self, environment:list, enemies:list, character: list):
        self._draw_fill_display()
        self._draw_all(character)
        self._draw_flip()

    def _draw_fill_display(self): self.display.fill(self.display_color)

    def _draw_all(self, character: list): pass

    def _draw_flip(self):
        pygame.display.flip()





    def write_data_on_screen(self, text:str): pygame.display.set_caption(text)
