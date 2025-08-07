from pgzero.actor import Actor

class Coin:
    def __init__(self, pos, images):
        self.images = images
        self.actor = Actor(self.images[0], pos=pos)
        self.animation_frame = 0
        self.animation_speed = 0.2

    def update(self):
        self.animation_frame += self.animation_speed
        if self.animation_frame >= len(self.images):
            self.animation_frame = 0
        self.actor.image = self.images[int(self.animation_frame)]

    def draw(self, screen):
        self.actor.draw()