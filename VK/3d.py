from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

player = FirstPersonController(
    height=4,
    speed=6,
    position=(22,0,-10),
    collider='box'
)

ground = Entity(
    model='cube',
    scale=(100,1,100),
    texture='assets/rocky_terrain_02_diff_1k.jpg',
    collider = 'mesh',
    texture_scale=(20,10)
)

wall1 = Entity(
    model='cube',
    scale=(8,5,0.5),
    texture='assets/broken_brick_wall_diff_1k.jpg',
    position=(20,2.5,10),
    collider='box'
)

wall2 = Entity(
    model='cube',
    scale=(8,5,0.5),
    texture='assets/broken_brick_wall_diff_1k.jpg',
    position=(17,2.5,7),
    rotation_y=90,
    collider='box'
)

brick1 = Entity(
    model='cube',
    scale=(2,2,3),
    texture='assets/plastered_stone_wall_diff_1k.jpg',
    position=(19,1,8),
    collider='box'
)

block1 = Entity(
    model='cube',
    scale=(4,0.5,5),
    texture='assets/dark_wooden_planks_diff_1k.jpg',
    position=(0,10,55),
    collider='box'
)

block2 = Entity(
    model='sphere',
    scale=(3,3,3),
    texture='assets/rock.jpg',
    position=(0,12,55),
    collider='box'
)

coins = []

for i in range(5):
    coin = Entity(
        model='sphere',
        color=color.gold,
        scale=1,
        collider='box',
        position=(random.uniform(-30, 30), 1, random.uniform(-30, 40))
    )
    coins.append(coin)

coords_display = Text(text='Position: ', origin=(-0.5, 0.5), scale=1, x=-0.8, y=0.45)
coins_collected = 0
coin_display = Text(text='Coins: 0', origin=(-0.5, 0.5), scale=1, x=-0.8, y=0.40)

lvl = 1
sky = Sky()

blocks = []
directions = []

for i in range(10):
    r = random.uniform(-2, 2)
    block = Entity(
        model='cube',
        scale=(3,0.5,3),
        texture='assets/dark_wooden_planks_diff_1k.jpg',
        position=(r, 1 + i, 3 + i * 5),
        collider='box'
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

    i = 0
    for block in blocks:
        block.x += directions[i] * time.dt * 2 
        if abs(block.x) > 5:
            directions[i] *= -1
            block.x = 5 if block.x > 0 else -5
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

window.fullscreen = True

def input(key):
    if key == 'escape':
        app.quit()

app.run()