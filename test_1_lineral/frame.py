import pygame

class Frame:
    def __init__(self, start_pos, end_pos, goal_pos, frame_color = [255, 255, 0], goal_color = [255,0,20], width=5):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.goal_pos = goal_pos
        self.frame_color = frame_color
        self.goal_color = goal_color
        self.width = width


    def draw(self, display):
        pygame.draw.line(display, color=self.frame_color, start_pos=[self.start_pos[0], self.start_pos[1]], end_pos=[self.end_pos[0], self.start_pos[1]], width=self.width)
        pygame.draw.line(display, color=self.frame_color, start_pos=[self.end_pos[0], self.end_pos[1]], end_pos=[self.end_pos[0], self.start_pos[1]], width=self.width)
        pygame.draw.line(display, color=self.frame_color, start_pos=[self.start_pos[0], self.end_pos[1]], end_pos=[self.end_pos[0], self.end_pos[1]], width=self.width)
        pygame.draw.line(display, color=self.frame_color, start_pos=[self.start_pos[0], self.start_pos[1]], end_pos=[self.start_pos[0], self.end_pos[1]], width=self.width)

        pygame.draw.line(display, color=self.goal_color, start_pos=[self.goal_pos[0], self.start_pos[1]], end_pos=[self.goal_pos[0], self.end_pos[1]], width=self.width)
        pygame.draw.line(display, color=self.goal_color, start_pos=[self.start_pos[0], self.goal_pos[1]], end_pos=[self.end_pos[0], self.goal_pos[1]], width=self.width)
