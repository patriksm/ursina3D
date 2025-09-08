from random import randint, uniform
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController( 
    height=2,
    speed = 10,
    collider = 'box',
)

ground = Entity(
    model = 'cube',
    texture= 'assets\moon_01_disp_4k.png',
    scale = (100,1,100),
    collider = 'box'
)

level = 1 
blocks = []
directions= []
colors = [color.blue, color.pink, color.violet, color.green, color.orange, color.brown, color.gold]

def update():
    global lvl
    # print(myText)
    i=0
    for block in blocks:
        block.x -= directions[i] * (time.dt*i)
        if abs(block.x) > 5:
            directions[i] *= -1
        if block.intersects().hit :
            player.x -= directions[i]*(time.dt*i)
        if block.intersects().hit:
            block.color = color.gold
            ding.play()
        # if ground.intersects(player).hit:
        #     block.color = color.random_color()
        i+=1


    walking = held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']
    if walking and player.grounded:
        myText.text = player.x 
        if not walk.playing:
            walk.play()
    else:
        if walk.playing:
            walk.stop()



def input(key):
    if key == 'escape':
        quit()
    if key == 'space':
        jump.play()
        

for i in range(10):
    r = uniform(-2,2)
    block = Entity(
        model='cube',
        texture='assets\slab_tiles_diff_1k.jpg',
        color=color.random_color(),
        scale=(3,0.5,3),
        position=(r,1+i,3+i*5),
        collider='box',
        
    )
    blocks.append(block)
    if r<0:
        directions.append(1)
    else:
        directions.append(-1)

goal = Entity(
    model='cube',
    color = color.gold,
    texture= 'assets\slab_tiles_diff_1k.jpg',
    position = (0, 11, 55),
    scale = (10,1,10),
    collider='box',
)

pillar = Entity(
    color=color.green,
    model='cube',
    texture = 'assets\metal_grate_rusty_disp_1k.png',
    scale = (1,50,1),
    position = (0,36,58),
),


myText= Text(
    text = "Wow, a game!",
    origin = (5, -15)
)

walk = Audio(
    'assets\walking2.mp3',
    loop = False,
    autoplay = False,
)

jump = Audio(
    'assets\jumping.mp3',
    loop = False,
    autoplay = False,
)

ding = Audio(
    'assets\ding.mp3',
    loop = False,
    autoplay = False,
)

window.fullscreen = False
sky = Sky(texture='assets\starsky2.hdr')
app.run()