from pgzero.actor import Actor
import pygame as pg

class Enemy:
    def __init__(self, pos, images, move_type='horizontal'):
        self.images = images
        self.actor = Actor(self.images['walk'][0], midbottom=pos)
        self.move_type = move_type
        self.vx = 0
        self.vy = 0
        self.patrol_range = 50
        self.initial_pos = pos
        self.animation_frame = 0
        self.animation_speed = 0.1
        self.flip_x = False
        if self.move_type == 'horizontal':
            self.vx = -1
        elif self.move_type == 'vertical':
            self.vy = -1

    def update(self):
        if self.move_type == 'horizontal':
            self.actor.x += self.vx
            if self.actor.x < self.initial_pos[0] - self.patrol_range or \
               self.actor.x > self.initial_pos[0] + self.patrol_range:
                self.vx *= -1
                self.flip_x = not self.flip_x
        elif self.move_type == 'vertical':
            self.actor.y += self.vy
            if self.actor.y < self.initial_pos[1] - self.patrol_range or \
               self.actor.y > self.initial_pos[1] + self.patrol_range:
                self.vy *= -1
        self.animate()

    def animate(self):
        self.animation_frame += self.animation_speed
        animation_list = self.images['walk']
        if self.animation_frame >= len(animation_list):
            self.animation_frame = 0
        self.actor.image = animation_list[int(self.animation_frame)]
        if self.flip_x:
            self.actor._surf = pg.transform.flip(self.actor._surf, True, False)

    def draw(self, screen):
        self.actor.draw()