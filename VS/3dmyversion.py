from random import randint, uniform
from ursina import * 
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController(
    height=2,
    speed=15,
    collider='box'
)

wall_left = Entity( #kreisa siena
    model='cube',
    scale=(1, 50, 150),
    texture='assets/siena.jpg',
    position=(-50, 2.5, 0),
    collider='box'
)

wall_right = Entity( #laba siena
    model='cube',
    scale=(1, 50, 150),
    texture='assets/siena.jpg',
    position=(50, 2.5, 0),
    collider='box'
)

wall_back = Entity( #aizmugureja siena
    model='cube',
    scale=(100, 50, 1),
    texture='assets/siena.jpg',
    position=(0, 2.5, -50),
    #collider='box'
)
wall_front = Entity( #priekseja siena
    model='cube',
    scale=(100, 50, 1),
    texture='assets/siena.jpg',
    position=(0, 2.5, 75),
    collider='box'
)
block_1 = Entity( #block 1
    model='sphere',
    scale=(3, 2, 3),
    texture='assets/block.jpg',
    position=(-40, 1.5, -65),
    collider='box'
)
block_2 = Entity( #block 2
    model='sphere',
    scale=(3, 5, 3),
    texture='assets/block.jpg',
    position=(-35, 1.5, -65),
    collider='box'
)
block_3 = Entity( #block 3
    model='sphere',
    scale=(3, 8, 3),
    texture='assets/block.jpg',
    position=(-30, 1.5, -65),
    collider='box'
)
block_4 = Entity( #block 4
    model='sphere',
    scale=(3, 11, 3),
    texture='assets/block.jpg',
    position=(-25, 1.5, -65),
    collider='box'
)
block_5 = Entity( #block 5
    model='sphere',
    scale=(3, 14, 3),
    texture='assets/block.jpg',
    position=(-20, 1.5, -65),
    collider='box'
)
block_6 = Entity( #block 6
    model='sphere',
    scale=(3, 17, 3),
    texture='assets/block.jpg',
    position=(-15, 1.5, -65),
    collider='box'
)
block_7 = Entity( #block 7
    model='sphere',
    scale=(3, 20, 3),
    texture='assets/block.jpg',
    position=(-10, 1.5, -65),
    collider='box'
)
block_8 = Entity( #block 8
    model='sphere',
    scale=(3, 23, 3),
    texture='assets/block.jpg',
    position=(-5, 1.5, -65),
    collider='box'
)
block_9 = Entity( #block 9
    model='sphere',
    scale=(3, 26, 3),
    texture='assets/block.jpg',
    position=(0, 1.5, -65),
    collider='box'
)
block_10 = Entity( #block 10
    model='sphere',
    scale=(3, 29, 3),
    texture='assets/block.jpg',
    position=(5, 1.5, -65),
    collider='box'
)
block_11 = Entity( #block 11
    model='sphere',
    scale=(3, 32, 3),
    texture='assets/block.jpg',
    position=(10, 1.5, -65),
    collider='box'
)
block_12 = Entity( #block 12
    model='sphere',
    scale=(3, 35, 3),
    texture='assets/block.jpg',
    position=(15, 1.5, -65),
    collider='box'
)
block_13 = Entity( #block 13
    model='sphere',
    scale=(3, 38, 3),
    texture='assets/block.jpg',
    position=(20, 1.5, -65),
    collider='box'
)
block_14 = Entity( #block 14
    model='sphere',
    scale=(3, 41, 3),
    texture='assets/block.jpg',
    position=(25, 1.5, -65),
    collider='box'
)
block_15 = Entity( #block 15
    model='sphere',
    scale=(3, 44, 3),
    texture='assets/block.jpg',
    position=(30, 1.5, -65),
    collider='box'
)
block_16 = Entity( #block 16
    model='sphere',
    scale=(3, 47, 3),
    texture='assets/block.jpg',
    position=(35, 1.5, -65),
    collider='box'
)
block_17 = Entity( #block 17
    model='sphere',
    scale=(3, 50, 3),
    texture='assets/block.jpg',
    position=(40, 1.5, -65),
    collider='box'
)
block_18 = Entity( #block 18
    model='cube',
    scale=(5, 53, 5),
    texture='assets/siena2.jpg',
    position=(45, 1.5, -65),
    collider='box'
)
block_19 = Entity( #block 19
    model='cube',
    scale=(5, 53, 5),
    texture='assets/siena2.jpg',
    position=(45, 1.5, -60),
    collider='box'
)
block_20 = Entity( #block 20
    model='cube',
    scale=(5, 53, 5),
    texture='assets/siena2.jpg',
    position=(45, 1.5, -55),
    collider='box'
)

block_list = [
    block_1, block_2, block_3, block_4, block_5, block_6, block_7, block_8,
    block_9, block_10, block_11, block_12, block_13, block_14, block_15,
    block_16, block_17, block_18, block_19, block_20
]

game_over_text = Text( # speles beigas teksts
    text = "GAME OVER",
    origin = (0,0),
    scale = 7,
    color = color.red,
    enabled = False   
)

coins = []
score = 0
score_text = Text(
    text=f"Nauda: {score}",
    scale = 2, #zimes izmers
    position = (-0.75, 0.45), # zimes pozicija
    origin=(0, 0),
    color=color.green
)

for block in block_list:
    coin = Entity(
        model='sphere',
        texture='coin.jpg',
        color=color.gold,
        scale=0.5,
        position=(block.x, block.y + block.scale_y/2 + 0.5, block.z),
        collider='box'
    )
    coins.append(coin)

ground = Entity( #zeme
    model='cube', 
    texture='assets/floor2.jpg',
    collider='box',
    scale=(100, 1, 150)
)

lvl = 1
speed_multiplier = 3.0   # platformas atrums
sky = Sky() # 00 debesis

blocks = []
directions = []
colors = [color.azure, color.red, color.orange, color.blue, color.green, color.yellow, color.pink]

for i in range(10):
    r = uniform(-2, 2)
    block = Entity(
        position=(r, 1+i, 3 + i*5),
        model='cube',
        texture='assets/floor.jpg',
        color=colors[randint(0, len(colors)-1)],
        scale=(5, 0.5, 5),
        collider='box'
    )
    blocks.append(block)
    directions.append(1 if r < 0 else -1)
       
goal = Entity(#finish
    model='cube',
    texture='assets/floor.jpg',
    position=(0, 11, 55),
    scale=(10, 1, 10),
    collider='box'
)

pillar = Entity( # stabs
    model='cube',
    texture='assets/metal_plate_diff_1k.jpg',
    position=(0, 36, 58),
    scale=(1, 50, 1)
)

mySphere = Entity(  #sfera 
    texture='assets/box_profile_metal_sheet_diff_1k.jpg',
    model='sphere',
    position=(0, 60, 58),
    scale=(20, 20, 20)
)

myText = Text(
    text=f"Level: {lvl}",
    origin=(13, -17),
    color=color.white
)

walk = Audio( # 06 pieslēgt audio spēlē
    'assets\walking.mp3',
    loop = False, # lai audio neatkārtotos
    autoplay = False # lai nespēlē uzreiz, ieslēdzot spēli
)

jump = Audio( # 06 pieslēgt audio spēlē
    'assets\jumping.mp3',
    loop = False, # lai audio neatkārtotos
    autoplay = False # lai nespēlē uzreiz, ieslēdzot spēli
)

coin_sound = Audio(
    'assets/coin.mp3',
    loop = False,
    autoplay = False
)

def restart_level():# restartešana
    global lvl, speed_multiplier, score
    lvl += 1
    speed_multiplier += 1.0   # bloku atrums
    player.position = (0, 2, 0)   # restart position uz 0
    for coin in coins:
        coin.enabled = True
    score = 0
    score_text.text = f"Nauda: {score}"

def update():
    global score

    for coin in coins:
        if coin.enabled and player.intersects(coin).hit:
            coin.enabled = False  # moneta pazud
            score += 1
            score_text.text = f"Nauda: {score}"
            coin_sound.play()
        if coin.enabled: #monetas griesana
            coin.rotation_y += 100 * time.dt
    i = 0

    for block in blocks:
        block.x -= directions[i] * time.dt * speed_multiplier
        if abs(block.x) > 5:
            directions[i] *= -1
        if block.intersects().hit:
            player.x -= directions[i] * time.dt * speed_multiplier
        i += 1
        #if block.enabled: #bloka griesana
            #block.rotation_y += 100 * time.dt

        if mySphere.enabled: #sferas griesana
            mySphere.rotation_y += 100 * time.dt

        #if game_over_text.enabled:
            #game_over_text.rotation_y +=20 * time.dt

        if all(not coin.enabled for coin in coins):
           game_over_text.enabled = True # teksta ieslegsana kad monetas nav
           for block in blocks:
               block.y -= -5 * time.dt   # bloki lido)
               block.rotation_y += 100 * time.dt  #bloku griesana 

    for block in block_list: #secrel lvl bloku griesana
        block.rotation_y += -50 * time.dt
    
    if player.z > 56 and player.y > 10:
        restart_level()
    sky.texture = 'sky_sunset'
    walking = held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']
    if walking and player.grounded:
        if not walk.playing:
            walk.play()
    else:
        if walk.playing:
            walk.stop()

def input(key):  # 02 ja nospiests kāds taustiņš, šeit var programmēt darbības, kas notiks. 
    if key in ('escape', ): # 03 iziet no spēles, ja ir nospiests taustiņš q
        quit()
    if key == 'space':
        jump.play()
    if key in ('q'):
        restart_level()
    if held_keys['shift']:
        player.speed = 40   # speletaja paatrinasana
    else:
        player.speed = 15
app.run() # 00 palaižām spēles logu
