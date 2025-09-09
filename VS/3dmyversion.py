from random import randint, uniform
from ursina import * 
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController(
    height=2,
    speed=10,
    collider='box'
)

wall_left = Entity(#kreisa siena
    model='cube',
    scale=(1, 50, 100),
    texture='assets/floor.jpg',
    position=(-50, 2.5, 0),
    collider='box'
)
wall_right = Entity(#laba siena
    model='cube',
    scale=(1, 50, 100),
    texture='assets/floor.jpg',
    position=(50, 2.5, 0),
    collider='box'
)
wall_back = Entity(#aizmugureja siena
    model='cube',
    scale=(100, 50, 1),
    texture='assets/floor.jpg',
    position=(0, 2.5, -50),
    collider='box'
)

ground = Entity(
    model='cube', 
    texture='assets/grass.jpg',
    collider='box',
    scale=(100, 1, 100)
)

lvl = 1
speed_multiplier = 1.0   # platformas atrums
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

goal = Entity(
    model='cube',
    texture='assets/floor.jpg',
    position=(0, 11, 55),
    scale=(10, 1, 10),
    collider='box'
)

pillar = Entity(
    model='cube',
    texture='assets/grass.jpg',
    position=(0, 36, 58),
    scale=(1, 50, 1)
)

mySphere = Entity(
    color=color.gold,
    model='sphere',
    position=(0, 60, 58),
    scale=(7, 7, 7)
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

def restart_level():
    global lvl, speed_multiplier
    lvl += 1
    speed_multiplier += 1.0   # bloku atrums
    player.position = (0, 2, 0)   # restart position uz 0
   

def update():
    i = 0
    for block in blocks:
        block.x -= directions[i] * time.dt * speed_multiplier
        if abs(block.x) > 5:
            directions[i] *= -1
        if block.intersects().hit:
            player.x -= directions[i] * time.dt * speed_multiplier
        i += 1

    
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
app.run() # 00 palaižām spēles logu
