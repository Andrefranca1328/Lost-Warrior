import pgzrun
from pgzero.actor import Actor
from classes.player import Player
from classes.enemy import Enemy
from classes.coin import Coin

TILE_SIZE = 18

LEVEL_MAP = (
    "                                                          ", "                                                         ",
    "  <->           (====)                  <->               ", "                                                          ",
    "          C                             <-> C         (==)", "        (====)                                            ",
    "                      V                   (====)          ", "                       (====)                             ",
    "           C                                              ", "              <->                          V              ",
    "                                          (====)          ", "               E                (====)                 <->",
    "     <->                                                  ", "                                                          ",
    "      C       p     p         m C f f   m     p     C     ", "        t gGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
    "      gGGGGDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDBDDDDDDDDDDDDDD", "    gGDDDDDDDDBDDDDDDDDDDDDDDDDBDDDDDDDDDDDDBDDDDDDDDDDDDDDDD",
    "GGGDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD", "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD",
)

TILE_MAPPING = {
    '(': 'platform_grass_left.png', '=': 'platform_grass_mid.png', ')': 'platform_grass_right.png',
    'G': 'ground_top.png', 'D': 'ground_dirt.png', 'g': 'ground_topleft.png',
    '<': 'cloud_left.png', '-': 'cloud_mid.png', '>': 'cloud_right.png',
    'p': 'decor_plant.png', 'f': 'decor_plant2.png', 't': 'decor_tree.png', 'B': 'box_item.png',
    'E': 'enemy_move_0', 'V': 'enemy_move_0', 'C': 'coin_anim_0',
}

WIDTH = len(LEVEL_MAP[0]) * TILE_SIZE
HEIGHT = len(LEVEL_MAP) * TILE_SIZE

game_state = 'menu'
music_on = True

button_start = Actor('button_start_0', center=(WIDTH / 2, HEIGHT / 2 - 80))
button_music = Actor('button_music_on_0', center=(WIDTH / 2, HEIGHT / 2 + 0))
button_quit = Actor('button_quit_0', center=(WIDTH / 2, HEIGHT / 2 + 80))
menu_buttons = [button_start, button_music, button_quit]

background_actors = []
interactive_actors = []
coins = []
enemies = []
player = None
total_coins = 0

enemy_images = {'walk': ['enemy_move_0', 'enemy_move_1', 'enemy_move_2']}
coin_images = ['coin_anim_0', 'coin_anim_1', 'coin_anim_2', 'coin_anim_3', 'coin_anim_4', 'coin_anim_5', 'coin_anim_6', 'coin_anim_7', 'coin_anim_8', 'coin_anim_9', 'coin_anim_10', 'coin_anim_11']
player_images = {
    'idle': ['hero_idle_0', 'hero_idle_1', 'hero_idle_2', 'hero_idle_3'],
    'run': ['hero_run_0', 'hero_run_1', 'hero_run_2', 'hero_run_3', 'hero_run_4', 'hero_run_5', 'hero_run_6', 'hero_run_7'],
    'hit': ['hero_hit_0', 'hero_hit_1', 'hero_hit_2', 'hero_hit_3'],
    'death': ['hero_death_0', 'hero_death_1', 'hero_death_2', 'hero_death_3'],
    'jump': ['hero_run_2'],
}

def reset_game():
    global player, total_coins, game_state, background_actors, interactive_actors, coins, enemies
    background_actors.clear()
    interactive_actors.clear()
    coins.clear()
    enemies.clear()
    total_coins = 0
    for row_index, row in enumerate(LEVEL_MAP):
        for col_index, symbol in enumerate(row):
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
            if symbol == 'C':
                coins.append(Coin(pos=(x, y), images=coin_images))
                total_coins += 1
            elif symbol == 'E':
                enemies.append(Enemy(pos=(x, y + TILE_SIZE), images=enemy_images, move_type='horizontal'))
            elif symbol == 'V':
                enemies.append(Enemy(pos=(x, y), images=enemy_images, move_type='vertical'))
            elif symbol in TILE_MAPPING:
                image_file = TILE_MAPPING[symbol]
                if symbol in '<->pft':
                    background_actors.append(Actor(image_file, topleft=(x, y)))
                else:
                    interactive_actors.append(Actor(image_file, topleft=(x, y)))
    player = Player(pos=(150, 200), images=player_images, screen_width=WIDTH, screen_height=HEIGHT)
    game_state = 'playing'
    if music_on:
        music.play('background_music')
        music.set_volume(0.3)

def draw_hud():
    for i in range(player.coins_collected):
        coin_icon = Actor('coin_anim_1')
        coin_icon.topleft = (20 + i * 20, 20)
        coin_icon.draw()
    for i in range(player.max_health):
        heart_image = 'heart' if i < player.health else 'heart3'
        screen.blit(heart_image, (20 + i * 20, 55))

def draw():
    screen.fill((135, 206, 235))
    if game_state == 'menu':
        for button in menu_buttons:
            button.draw()
    elif game_state in ['playing', 'win', 'lose']:
        for actor in background_actors:
            actor.draw()
        for actor in interactive_actors:
            actor.draw()
        for coin in coins:
            coin.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)
        player.draw(screen)
        draw_hud()
        if game_state == 'win':
            screen.draw.text("VOCE VENCEU!", center=(WIDTH/2, HEIGHT/2), color="green", fontsize=60, fontname="press_start.ttf",
                            shadow=(2, 2), scolor="darkgreen")
            screen.draw.text("Pressione ENTER para voltar ao menu", center=(WIDTH/2, HEIGHT/2 + 50), color="white", fontsize=20, fontname="press_start.ttf",
                            shadow=(1, 1), scolor="black")
        elif game_state == 'lose':
            screen.draw.text("FIM DE JOGO", center=(WIDTH/2, HEIGHT/2), color="red", fontsize=60, fontname="press_start.ttf",
                            shadow=(2, 2), scolor="darkred")
            screen.draw.text("Pressione ENTER para voltar ao menu", center=(WIDTH/2, HEIGHT/2 + 50), color="white", fontsize=20, fontname="press_start.ttf",
                            shadow=(1, 1), scolor="black")

def update(dt):
    global game_state
    if game_state != 'playing':
        return
    player.update(keyboard, interactive_actors, dt)
    for enemy in enemies:
        enemy.update()
    for coin in coins:
        coin.update()
    coins_a_remover = []
    for coin in coins:
        if player.actor.colliderect(coin.actor):
            sounds.coin_collect.play()
            player.coins_collected += 1
            coins_a_remover.append(coin)
    for coin in coins_a_remover:
        coins.remove(coin)
    if not player.is_invincible:
        for enemy in enemies:
            if player.actor.colliderect(enemy.actor):
                sounds.player_hit.play()
                player.take_damage(1, enemy.actor)
                break
    if player.is_dead:
        game_state = 'lose'
        music.stop()
    elif total_coins > 0 and player.coins_collected >= total_coins:
        game_state = 'win'
        music.stop()

def on_mouse_down(pos):
    global music_on
    if game_state == 'menu':
        if button_start.collidepoint(pos):
            reset_game()
        elif button_quit.collidepoint(pos):
            quit()
        elif button_music.collidepoint(pos):
            music_on = not music_on
            base_music_image = 'button_music_on' if music_on else 'button_music_off'
            button_music.image = base_music_image + '_1'

def on_key_down(key):
    global game_state
    if game_state in ['win', 'lose'] and key == keys.RETURN:
        game_state = 'menu'
    if game_state == 'playing' and player.on_ground and key == keys.UP:
        sounds.player_jump.play()

def on_mouse_move(pos):
    if game_state == 'menu':
        if button_start.collidepoint(pos):
            button_start.image = 'button_start_1'
        else:
            button_start.image = 'button_start_0'
        if button_quit.collidepoint(pos):
            button_quit.image = 'button_quit_1'
        else:
            button_quit.image = 'button_quit_0'
        base_music_image = 'button_music_on' if music_on else 'button_music_off'
        if button_music.collidepoint(pos):
            button_music.image = base_music_image + '_1'
        else:
            button_music.image = base_music_image + '_0'

pgzrun.go()