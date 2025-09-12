from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

player = FirstPersonController(
    height=2,
    speed=6,
    position=(0,0,0),
    collider='box',
    gravity=1,
    enabled=False
)

ground = Entity(
    model='cube',
    scale=(100,1,100),
    texture='assets/rocky_terrain_02_diff_1k.jpg',
    collider = 'box',
    texture_scale=(20,10),
    enabled=False
)

wall1 = Entity(
    model='cube',
    scale=(8,5,0.5),
    texture='assets/broken_brick_wall_diff_1k.jpg',
    position=(20,2.5,10),
    collider='box',
    enabled=False
)

wall2 = Entity(
    model='cube',
    scale=(8,5,0.5),
    texture='assets/broken_brick_wall_diff_1k.jpg',
    position=(17,2.5,7),
    rotation_y=90,
    collider='box',
    enabled=False
)

brick1 = Entity(
    model='cube',
    scale=(2,2,3),
    texture='assets/plastered_stone_wall_diff_1k.jpg',
    position=(19,1,8),
    collider='box',
    enabled=False
)

block1 = Entity(
    model='cube',
    scale=(4,0.5,5),
    texture='assets/dark_wooden_planks_diff_1k.jpg',
    position=(0,10,55),
    collider='box',
    enabled=False
)

block2 = Entity(
    model='sphere',
    scale=(3,3,3),
    texture='assets/rock.jpg',
    position=(0,12,55),
    collider='box',
    enabled=False
)

coins = []

for i in range(5):
    coin = Entity(
        model='sphere',
        color=color.gold,
        scale=1,
        collider='box',
        enabled=False,
        position=(random.uniform(-30, 30), 1, random.uniform(-30, 40))
    )
    coins.append(coin)

game_ui = Entity(enabled=False)

coords_display = Text(text='Position: ', origin=(-0.5, 0.5), scale=1, x=-0.8, y=0.45)
coins_collected = 0
coin_display = Text(text='Coins: 0', origin=(-0.5, 0.5), scale=1, x=-0.8, y=0.40)

lvl = 1
sky = Sky(enabled=False)

blocks = []
directions = []

for i in range(10):
    r = random.uniform(-2, 2)
    block = Entity(
        model='cube',
        scale=(3,0.5,3),
        texture='assets/dark_wooden_planks_diff_1k.jpg',
        position=(r, 1 + i, 3 + i * 5),
        collider='box',
        enabled=False
    )
    blocks.append(block)

    if r < 0:
        directions.append(1)
    else:
        directions.append(-1)


music = Audio('assets/crickets.mp3', loop=True, autoplay=True, volume=0.1)
walk_sound = Audio('assets/walking-on-grass.mp3', loop=False, autoplay=False, volume=0.2) 
jump_sound = Audio('assets/jump.mp3', loop=False, autoplay=False, volume=0.3)
collect_sound = Audio('assets/coin.mp3', loop=False, autoplay=False, volume=0.5)

space_was_pressed = False

def update():
    global lvl, coins_collected, space_was_pressed

    if not player.enabled:
        return

    i = 0
    for block in blocks:
        block.x -= directions[i] * time.dt
        if abs(block.x) > 5:
            directions[i] *= -1
        if block.intersects().hit:
            player.x -= directions[i]*time.dt
        i += 1

    if player.z > 56 and player.y > 10 and lvl == 1: 
        lvl = 2
    sky.texture = 'sky_sunset'

    walking = held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']
    if walking:
        if not walk_sound.playing:
            walk_sound.play()
    else:
        walk_sound.stop()

    global space_was_pressed
    if held_keys['space']:
        if not space_was_pressed:
            if not jump_sound.playing:
                jump_sound.play()
            space_was_pressed = True
    else:
        space_was_pressed = False

    for coin in list(coins):
        for coin in coins:
            if player.intersects(coin).hit:
                coins_collected += 1
                coin_display.text = f'Coins: {coins_collected}'
                coin.position = (random.uniform(-30, 30), 1, random.uniform(-30, 40))
                collect_sound.play()

    coords_display.text = f'Position: {int(player.x)}, {int(player.y)}, {int(player.z)}'

# window.fullscreen = True

start_menu = Entity(enabled=True)

title = Text("My Game", scale=3, y=0.4, parent=camera.ui, color=color.black)

start_button = Button("Start", scale=(0.2,0.1), y=0.1, parent=camera.ui)
quit_button = Button("Quit", scale=(0.2,0.1), y=-0.2, parent=camera.ui)

def enable_player():
    player.position = (0, ground.y, 0)
    player.enabled = True
    mouse.locked = True

def start_game():

    title.enabled = False
    start_button.enabled = False
    quit_button.enabled = False

    wall1.enabled = True
    wall2.enabled = True
    brick1.enabled = True
    block1.enabled = True
    block2.enabled = True
    ground.enabled = True
    sky.enabled = True
    for b in blocks: b.enabled = True
    for c in coins: c.enabled = True

    player.position = (0, 0, 0)
    player.enabled = True
    player.gravity = 1
    mouse.locked = True

    game_ui.enabled = True

    invoke(enable_player, delay=0.01)
    
def quit_game():
    app.quit()

start_button.on_click = start_game
quit_button.on_click = quit_game

pause_menu = Entity(enabled=False)

resume_button = Button("Resume", scale=(0.2,0.1), y=0.1, parent=pause_menu)
pause_quit_button = Button("Quit", scale=(0.2,0.1), y=-0.2, parent=pause_menu)

def resume_game():
    pause_menu.enabled = False
    player.enabled = True
    game_ui.enabled = True
    mouse.locked = True

resume_button.on_click = resume_game
pause_quit_button.on_click = quit_game

def input(key):
    if key == 'escape':
        app.quit()
    if key == 'p':
        if pause_menu.enabled:
            resume_game()
        else:
            pause_menu.enabled = True
            player.enabled = False
            game_ui.enabled = False
            mouse.locked = False

# def input(key):
#     if key == 'escape':
#         app.quit()

app.run()