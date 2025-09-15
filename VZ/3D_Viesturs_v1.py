from random import randint, uniform
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina() # 00 izveidojam kopējo laukumu

player = FirstPersonController(  # 01 veidojam kopējo skatu un spēlētāju
    #strādā pogas w,a,s,d un citas komandas
    height=2,
    speed = 10,
    collider = 'box',
    #player.gravity = 1 # spēlētāja mijiedarbība ar bloku
    #jump height = 10
    )

ground = Entity( # 04 kautko blakus
    model = 'cube',
    texture = 'assets/segums1.jpg',
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

# wall_front = Entity( #priekseja siena
#     model ='cube',
#     position =(0, 2.5, 100),
#     texture ='assets/mixed_brick_wall_diff_1k.jpg',
#     scale =(100, 50, 1),
#     collider ='box'
# )

lvl = 1 
sky = Sky() # 00 izveidojam debesis

#window.fullscreen = True # 05 pilnā ekrāna režīms

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
        collider='box',
        
        )
    coins.append((block, coin))

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


goal4 = Entity( # pēdējais pakāpiens
    model = 'cube',
    color = color.white,
    #texture = 'white_cube',
    texture = 'assets/mixed_brick_wall_diff_1k.jpg', #šādu \ vai šādu / - labāk "/"
    position = (0, 11, 89),
    scale = (10, 1, 10),
    collider = 'box'
)

goal5 = Entity( # pēdējais pakāpiens
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

gun = Entity( #Izveidojam ieroci
    parent=camera.ui, 
    model='cube',
    texture='gun3.png', 
    #color=color.black, 
    scale=0.5, 
    position=(0.3, -0.6),
    rotation_z=-10,
    origin_y=-0.5
)

# target = Entity(
#     model='cube', 
#     collider='box', 
#     color=color.red, 
#     position=(5, 1, 5)
# )

class Projectile(Entity):
    def __init__(self, direction=Vec3(0, 0, 1), **kwargs):
        super().__init__(
            model='sphere',
            collider='sphere',
            scale=0.1,
            color=color.white,
            name = 'bullet_instance',
            **kwargs
        )
        self.speed = 25
        self.lifetime = 2
        self.direction = direction
        #self.direction = kwargs.get('direction', Vec3(0, 0, 1))


         # Atskaņojam skaņu
        if 'gun_shot_sound' in globals():
            gun_shot_sound.play()

    def update(self):
        self.position += self.direction * self.speed * time.dt
        hit_info = raycast(self.world_position, self.direction, distance=self.speed * time.dt * 2, ignore=[self, player])
        #if hit_info.hit and hit_info.entity.name != 'bullet_instance':
        if hit_info.hit and hit_info.entity is not self:
                print(f'Trāpīts: {hit_info.entity.name}')
                destroy(self)
        
        self.lifetime -= time.dt
        if self.lifetime <= 0:
           destroy(self)
           

myText = Text(
    text = lvl,
    origin = (13, -13),
    color = color.white
)

coords_display = Text(text='Position: ', origin=(-0.5, 0.5), scale=1, x=-0.8, y=0.45)

walk = Audio( # 06 pieslēdzam audio spēlei
    'assets/walking.mp3',
    loop = False, # lai audio neatkārtojas
    autoplay = False # lai nespēlē uzreizes, ieslēdzot spēli
)

jump = Audio( # 06 pieslēdzam audio spēlei
    'assets/jumping_1-6452.mp3',
    loop = False, 
    autoplay = False 
)

collect_sound = Audio(
    'assets/coin_sound.mp3',
    loop = False,
    autoplay = False
)

scream = Audio(
    'assets/kliedziens.mpeg', 
    loop=False, 
    autoplay=False)

shot_gun = Audio(
    'assets/laser.mp3', 
    loop=False, 
    autoplay=False)


def update():
    global lvl, coins_collected, scream, shot_gun #te ir mēģinājums veidot līmeņus lvl - level
    i = 0
    for block in blocks:
        block.x -= directions[i] * time.dt
        if abs(block.x) > 5:
            directions[i] *= -1
        if block.intersects().hit: # spēlētājs mijiedarbojas ar bloku - abiem viena kustība.
            player.x -= directions[i]*time.dt
        i += 1

    for block, coin in coins:
        if coin.enabled and player.intersects(coin).hit:
            coins_collected += 1
            coin_display.text = f'Coins: {coins_collected}'
            coin.enabled = False  # moneta pazud
            collect_sound.play()

    for block, coin in coins:
        if coin.enabled:  
           coin.x = block.x
           coin.z = block.z
           coin.y = block.y + block.scale_y/2 + 0.5

    # if player.z > 56 and player.y > 10 and lvl == 1:
    #     lvl = 2 #te ir mēģinājums veidot līmeņus vairākus
    #     myText.text = lvl
    #     player.speed = 100 #mēģinu 2.līmenī 'palielināt' ātrumu
    #     print(myText.text)
    #sky.texture = 'sky.sunset' #Tā doma ir, ka 2.līmenī mainās debesis
   
    if lvl == 1 and player.z > 56 and player.y > 10:
        lvl = 2
        myText.text = lvl
        player.speed = 100
        print(myText.text)

        if not scream_played:
            scream.play()
            scream_played = True

    if player.y < -1 and not scream.playing:
            scream.play()


    walking = held_keys ['w'] or held_keys ['a'] or held_keys ['s'] or held_keys ['d']
    if walking and player.grounded:
        if not walk.playing:
           walk.stop()
    else:
        if walk.playing:
            walk.stop() 

    for coin in list(coins): #Violetas kods - monētas strādā, bet negriežas
        for coin in coins:
            if coin.enabled:
                coin.rotation_y += 10 * time.dt
            if player.intersects(coin).hit:
                coins_collected += 1
                coin.enabled = False
                coin_display.text = f'Coins: {coins_collected}'
                coin.position = (random.uniform(-30, 30), 1, random.uniform(-30, 40))
                collect_sound.play()

        if mySphere.enabled: #sferas griesana
            mySphere.rotation_y += 10 * time.dt #regulējam sfēras griešanos

    coords_display.text = f'Position: {int(player.x)}, {int(player.y)}, {int(player.z)}'

def input(key): # 02 var programmēt darbības ar taustiņiem
    if key == 'escape': #iziet no spēles, ja nospiests escape, var papildināt ar or = key q
        quit()

    if key == 'space':
        jump.play()

    if key == 'left mouse down':
        #start_position = gun.world_position
        bullet_direction = camera.forward
        Projectile(position=camera.position + bullet_direction * 1.5, direction=bullet_direction) 
        shot_gun.play()

app.run() # 00 izveidojam palaišanas komandu