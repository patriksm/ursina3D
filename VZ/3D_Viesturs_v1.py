from random import randint, uniform
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina() # 00 izveidojam kopējo laukumu

player = FirstPersonController(  # 01 veidojam kopējo skatu un spēlētāju
    #strādā pogas w,a,s,d un citas komandas
    height=2,
    speed = 10,
    collider = 'box', # spēlētāja mijiedarbība ar bloku
    #jump height = 10
    )

ground = Entity( # 04 kautko blakus
    model = 'cube',
    texture = 'assets\segums1.jpg',
    collider = 'box', # 'box' (vienkārš) un 'mesh' (sarežģīts) ir kolīziju veidi
    scale = (100, 1, 200)
)

wall_right = Entity( # 04 izveidojam pamatni un segumu
    model = 'cube',
    position = (50, 2.5, 0),
    texture = 'assets/mixed_brick_wall_diff_1k.jpg',
    collider = 'box', # 'box' (vienkārš) un 'mesh' (sarežģīts) ir kolīziju veidi
    scale = (1, 100, 200)
)

wall_left = Entity( #kreisa siena
    model='cube',
    position=(-50, 2.5, 0),
    texture='assets/mixed_brick_wall_diff_1k.jpg',
    collider='box',
    scale=(1, 100, 200)
)

wall_front = Entity( #priekseja siena
    model ='cube',
    position =(0, 2.5, 100),
    texture ='assets/mixed_brick_wall_diff_1k.jpg',
    scale =(100, 50, 1),
    collider ='box'
)






lvl = 1 
sky = Sky() # 00 izveidojam debesis

window.fullscreen = True # 05 pilnā ekrāna režīms

blocks = []
directions = []
colors = [color.azure, color.blue, color.red, color.orange, color.pink, color.yellow] #definējam masīvu krāsas
for i in range(10):
    r = uniform(-2, 2)
    block = Entity(
        position = (r, 1+i, 3 + i*5),
        model = 'cube',
        #texture = 'white_cube',
        texture = 'assets\segums1.jpg',
        color = colors[randint(0, len(colors) -1)], #dažādas krāsas, no masīva garuma atņemam 1.
        scale = (5, 0.5, 5),
        collider = 'box'
)
    blocks.append(block)
    if r < 0:
        directions.append(1)
    else:
        directions.append(-1)

coins = []
score = 0
score_text = Text(
    text = f"Coins: {score}",
    origin = (-13, 17),
    color = color.yellow,
    #texture = 'assets\Coin1.png'
)

for block in blocks:
    coin = Entity(
        model='sphere',
        texture='assets\Coin1.png',
        scale=0.5,
        position=(block.x, block.y + block.scale_y/2 + 0.5, block.z),
        collider='box'
    )
    coins.append(coin)

# for i in range(5): #šis gabals ir no 'Violetas'a
#     coin = Entity(
#         model='sphere',
#         color=color.gold,
#         scale=1,
#         collider='box',
#         position=(random.uniform(-30, 30), 1, random.uniform(-30, 40))
#     )
#     coins.append(coin)

coords_display = Text(text='Position: ', origin=(-0.5, 0.5), scale=1, x=-0.8, y=0.45)
coins_collected = 0
coin_display = Text(text='Coins: 0', origin=(-0.5, 0.5), scale=1, x=-0.8, y=0.40)

goal = Entity( # pēdējais pakāpiens
    model = 'cube',
    color = color.white,
    #texture = 'white_cube',
    texture = 'assets/mixed_brick_wall_diff_1k.jpg', #šādu \ vai šādu / - labāk "/"
    position = (0, 11, 55),
    scale = (10, 1, 10),
    collider = 'box'
)

goal2 = Entity( # pēdējais pakāpiens
    model = 'cube',
    color = color.white,
    #texture = 'white_cube',
    texture = 'assets/mixed_brick_wall_diff_1k.jpg', #šādu \ vai šādu / - labāk "/"
    position = (0, 11, 67),
    scale = (10, 1, 10),
    collider = 'box'
)

goal3 = Entity( # pēdējais pakāpiens
    model = 'cube',
    color = color.white,
    #texture = 'white_cube',
    texture = 'assets/mixed_brick_wall_diff_1k.jpg', #šādu \ vai šādu / - labāk "/"
    position = (0, 11, 78),
    scale = (10, 1, 10),
    collider = 'box'
)


goal3 = Entity( # pēdējais pakāpiens
    model = 'cube',
    color = color.white,
    #texture = 'white_cube',
    texture = 'assets/mixed_brick_wall_diff_1k.jpg', #šādu \ vai šādu / - labāk "/"
    position = (0, 11, 89),
    scale = (10, 1, 10),
    collider = 'box'
)

goal3 = Entity( # pēdējais pakāpiens
    model = 'cube',
    color = color.white,
    #texture = 'white_cube',
    texture = 'assets/mixed_brick_wall_diff_1k.jpg', #šādu \ vai šādu / - labāk "/"
    position = (0, 11, 99),
    scale = (10, 1, 10),
    collider = 'box'
)




pillar = Entity(
    color = color.green,
    model = 'cube',
    position = (0, 36, 58),
    scale = (1, 50, 1)  

)

mySphere = Entity(
    color = color.gold,
    model = 'sphere',
    position = (0, 60, 58),
    scale = (7, 7, 7)
)

myText = Text(
    text = lvl,
    origin = (13, -13),
    color = color.white
)


walk = Audio( # 06 pieslēdzam audio spēlei
    'assets\walking.mp3',
    loop = False, # lai audio neatkārtojas
    autoplay = False # lai nespēlē uzreizes, ieslēdzot spēli
)

jump = Audio( # 06 pieslēdzam audio spēlei
    'assets\jumping_1-6452.mp3',
    loop = False, 
    autoplay = False 
)

collect_sound = Audio(
    'assets/coin_sound.mp3',
    loop = False,
    autoplay = False
)

def update():
    global lvl, coins_collected #te ir mēģinājums veidot līmeņus lvl - level
    i = 0
    for block in blocks:
        block.x -= directions[i] * time.dt
        if abs(block.x) > 5:
            directions[i] *= -1
        if block.intersects().hit: # spēlētājs mijiedarbojas ar bloku - abiem viena kustība.
            player.x -= directions[i]*time.dt
        i += 1
    if player.z > 56 and player.y > 10 and lvl == 1:
        lvl = 2 #te ir mēģinājums veidot līmeņus vairākus
        myText.text = lvl
        player.speed = 100 #mēģinu 2.līmenī 'palielināt' ātrumu
        print(myText.text)
    #sky.texture = 'sky.sunset' #Tā doma ir, ka 2.līmenī mainās debesis

    walking = held_keys ['w'] or held_keys ['a'] or held_keys ['s'] or held_keys ['d']
    if walking and player.grounded:
        if not walk.playing:
            walk.play()
    else:
        if walk.playing:
            walk.stop() 


    for coin in list(coins):
        for coin in coins:
            if player.intersects(coin).hit:
                coins_collected += 1
                coin_display.text = f'Coins: {coins_collected}'
                coin.position = (random.uniform(-30, 30), 1, random.uniform(-30, 40))
                collect_sound.play()

coords_display.text = f'Position: {int(player.x)}, {int(player.y)}, {int(player.z)}'
  

def input(key): # 02 var programmēt darbības ar taustiņiem
    if key == 'escape': #iziet no spēles, ja nospiests escape, var papildināt ar or = key q
        quit()
    if key == 'space':
        jump.play

app.run() # 00 izveidojam palaišanas komandu