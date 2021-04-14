from pygame import time
import pygame
import os

class Monitor:
    def __init__(self) -> None:
        super().__init__()

        self.display_position = (50, 50)
        self.display_size = (3400, 1200)
        self.display_color = (48, 189, 221)
        self.fps_default = 480
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






    def draw(self, environment: list = [], enemies: list = [], character: list = []):
        self._draw_fill_display()
        self._draw_all(environment=environment, enemies=enemies, character=character)
        self._draw_flip()

    def _draw_fill_display(self): self.display.fill(self.display_color)

    def _draw_all(self, environment: list = [], enemies: list = [], character: list = []):
        for i in range(len(environment)): environment[i].draw(self.display)
        for i in range(len(enemies)): enemies[i].draw(self.display)
        for i in range(len(character)): character[i].draw(self.display)

    def _draw_flip(self):
        pygame.display.flip()





    def write_data_on_screen(self, text:str): pygame.display.set_caption(text)
