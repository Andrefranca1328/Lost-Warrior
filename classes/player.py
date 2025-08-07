from pgzero.actor import Actor
import pygame as pg

class Player:
    def __init__(self, pos, images, screen_width, screen_height):
        self.images = images
        self.actor = Actor(self.images['idle'][0], pos=pos)
        self.vx = 0
        self.vy = 0
        self.gravity = 0.7
        self.jump_force = -13
        self.on_ground = False
        self.current_animation = 'idle'
        self.animation_frame = 0
        self.animation_speed = 0.2
        self.flip_x = False
        self.is_dead = False
        self.health = 3
        self.max_health = 3
        self.coins_collected = 0
        self.is_hit = False
        self.is_invincible = False
        self.invincibility_timer = 0
        self.invincibility_duration = 1.5
        self.screen_width = screen_width
        self.screen_height = screen_height

    def take_damage(self, amount, enemy_actor=None):
        if not self.is_dead and not self.is_invincible:
            self.health -= amount
            self.animation_frame = 0
            self.is_hit = True
            self.is_invincible = True
            self.invincibility_timer = self.invincibility_duration
            if enemy_actor:
                repulsion_force = 4
                if self.actor.centerx < enemy_actor.centerx:
                    self.vx = -repulsion_force
                else:
                    self.vx = repulsion_force
                self.vy = -3
            if self.health <= 0:
                self.is_dead = True
                self.animation_frame = 0

    def update(self, keyboard, solid_tiles, dt):
        if self.is_invincible:
            self.invincibility_timer -= dt
            if self.invincibility_timer <= 0:
                self.is_invincible = False
        if self.is_dead:
            self.animate()
            return
        if self.is_hit and not self.is_invincible:
            self.is_hit = False
        if not self.is_hit:
            self.vx = 0
            if keyboard.left:
                self.vx = -4
                self.flip_x = True
            if keyboard.right:
                self.vx = 4
                self.flip_x = False
        self.actor.x += self.vx
        for tile in solid_tiles:
            if self.actor.colliderect(tile):
                if self.vx > 0:
                    self.actor.right = tile.left
                elif self.vx < 0:
                    self.actor.left = tile.right
        if not self.on_ground:
            self.vy += self.gravity
            if self.vy > 10:
                self.vy = 10
        self.actor.y += self.vy
        self.on_ground = False
        for tile in solid_tiles:
            if self.actor.colliderect(tile):
                if self.vy > 0:
                    self.actor.bottom = tile.top
                    self.on_ground = True
                    self.vy = 0
                elif self.vy < 0:
                    self.actor.top = tile.bottom
                    self.vy = 0
        if self.on_ground and keyboard.up:
            self.vy = self.jump_force
            self.on_ground = False
        if self.actor.left < 0:
            self.actor.left = 0
        if self.actor.right > self.screen_width:
            self.actor.right = self.screen_width
        if self.actor.top > self.screen_height:
            self.take_damage(self.health)
        self.animate()

    def animate(self):
        if self.is_dead:
            self.current_animation = 'death'
        elif self.is_hit:
            self.current_animation = 'hit'
        elif not self.on_ground:
            self.current_animation = 'jump'
        elif self.vx != 0 and not self.is_hit:
            self.current_animation = 'run'
        else:
            self.current_animation = 'idle'
        self.animation_frame += self.animation_speed
        animation_list = self.images.get(self.current_animation, self.images['idle'])
        if self.animation_frame >= len(animation_list):
            if self.is_hit:
                self.animation_frame = 0
            elif self.is_dead:
                self.animation_frame = len(animation_list) - 1
            else:
                self.animation_frame = 0
        self.actor.image = animation_list[int(self.animation_frame)]
        if self.flip_x:
            self.actor._surf = pg.transform.flip(self.actor._surf, True, False)

    def draw(self, screen):
        if self.is_invincible:
            if self.invincibility_timer % 0.2 < 0.1:
                return
        self.actor.draw()