import random
import time

from ursina import *
# roll
cool_down = 0
split1 = True
split2 = False
number2 = 0
# coins
amount = 1000
def update():
    # globals
    global roll, cool_down, split1, split2, number2, amount
    # coins
    hit_info = player.intersects()
    if hit_info.hit:
        amount += random.randint(1,5)
        R = random.randint(0, 4)
        if R == 0:
            for z in range(1):
                for x in range(random.randint(1, 9)):
                    coin.position = (x - 4.5, y + 1, z + 4.5)
        if R == 1:
            for z in range(random.randint(0, 5)):
                for x in range(1):
                    coin.position = (x - 4.5, y + 1, z)
        if R == 3:
            for z in range(1):
                for x in range(random.randint(0, 5)):
                    coin.position = (x, y + 1, z - 4.5)
        if R == 4:
            for z in range(random.randint(1, 9)):
                for x in range(1):
                    coin.position = (x + 4.5, y + 1, z - 4.5)
        # -----------------------------------
        R = random.randint(0, 4)
        if R == 0:
            for z in range(1):
                for x in range(random.randint(1, 9)):
                    coin2.position = (x - 4.5, y + 1, z + 4.5)
        if R == 1:
            for z in range(random.randint(0, 5)):
                for x in range(1):
                    coin2.position = (x - 4.5, y + 1, z)
        if R == 3:
            for z in range(1):
                for x in range(random.randint(0, 5)):
                    coin2.position = (x, y + 1, z - 4.5)
        if R == 4:
            for z in range(random.randint(1, 9)):
                for x in range(1):
                    coin2.position = (x + 4.5, y + 1, z - 4.5)
    # money text
    Money.text = 'Money = ' + str(amount)
    # cool down
    if cool_down > 0:
        dice.color = color.white
        roll = False
        cool_down -= 1
    if cool_down == 0:
        dice.color = color.pink
        roll = True
    if mouse.x > -0.32 and mouse.x < 0.32 and mouse.y < 0.32 and mouse.y > -0.32:
        # roll
        if roll == True:
            # roll
            cool_down = 20
            for x in range(13):
                number = random.randint(1,1)
                num.text = str(number)
            # move
            number = number
            if split1 == True:
                number2 = 0
                player.x -= 1
                if player.x < -4.5:
                    player.x = -4.5
                    player.z -= number
                if player.z < -4.5:
                    split1 = False
                    split2 = True
            if split2 == True:
                player.z = -4.5
                player.x += number
                if player.x > 4.5:
                    player.x = 4.5
                    number2 += number
                    player.z += number2
                if player.z > 4.5:
                    player.z = 4.5
                    split1 = True
                    split2 = False

app = Ursina()
# camera
camera.rotation_x = 90
camera.y = 33
camera.z = 0
# side window
Money = Text(text = 'Money = ' + str(amount), position = (0.6,0.4), color = color.white)
# value scales
def coloration():
    global amount
    # player color
    if amount > (red1.value + green1.value + blue1.value):
        amount = round(amount - (red1.value + green1.value + blue1.value))
        player.color = color.rgb(red1.value, green1.value, blue1.value)
    # background color
    if amount > (red1.value + green1.value + blue1.value):
        amount = round(amount - (red3.value - green3.value - blue3.value))
        bord.color = color.rgb(red3.value, green3.value, blue3.value)

# space color
y = 0
def space_c():
    global y, amount
    if amount > (red1.value + green1.value + blue1.value):
        amount = round(amount - (red2.value - green2.value - blue2.value))
        # sides
        y += 1
        coin.y = (y) + 1
        coin2.y = (y) + 1
        player.y = (y) + 1
        bord.y = (y) - 1
        dice.y = (y) - 1
        if player.y % 5:
            camera.y += 1
        for z in range(10):
            for x in range(1):
                voxel = Voxel(position=(x - 4.5, y, z - 4.5))
                voxel.color = color.rgb(red2.value, green2.value, blue2.value)
            for x in range(1):
                voxel = Voxel(position=(x + 4.5, y, z - 4.5))
                voxel.color = color.rgb(red2.value, green2.value, blue2.value)
        # top/bottom
        for z in range(1):
            for x in range(10):
                voxel = Voxel(position=(x - 4.5, y, z + 4.5))
                voxel.color = color.rgb(red2.value, green2.value, blue2.value)
            for x in range(10):
                voxel = Voxel(position=(x - 4.5, y, z - 4.5))
                voxel.color = color.rgb(red2.value, green2.value, blue2.value)

# player color
player_color = Text(text = 'player color'.title(), origin=(-4.7, -12), color = color.white)
red1 = Slider(0,255, default = 0, position = (0.46, 0.26), scale = 0.6, on_value_changed = coloration, text = 'RED')
green1 = Slider(0,255, default = 0, position = (0.46, 0.22), scale = 0.6, on_value_changed = coloration, text = 'GREEN')
blue1 = Slider(0,255, default = 0, position = (0.46, 0.18), scale = 0.6, on_value_changed = coloration, text = 'BLUE')
# space color
space_color = Text(text = 'spaces color'.title(), origin=(-4.5, -5), color = color.white)
red2 = Slider(0,255, default = 0, position = (0.46, 0.09), scale = 0.6, on_value_changed = space_c, text = 'RED')
green2 = Slider(0,255, default = 0, position = (0.46, 0.05), scale = 0.6, on_value_changed = space_c, text = 'GREEN')
blue2 = Slider(0,255, default = 0, position = (0.46, 0.01), scale = 0.6, on_value_changed = space_c, text = 'BLUE')
# background color
background_color = Text(text = 'background color'.title(), origin=(-3.3, 1.3), color = color.white)
red3 = Slider(0,255, default = 0, position = (0.46, -0.08), scale = 0.6, on_value_changed = coloration, text = 'RED')
green3 = Slider(0,255, default = 0, position = (0.46, -0.12), scale = 0.6, on_value_changed = coloration, text = 'GREEN')
blue3 = Slider(0,255, default = 0, position = (0.46, -0.16), scale = 0.6, on_value_changed = coloration, text = 'BLUE')

# coins
coin = Entity(model='cube', position = (-4.5, y + 1, -4.5), collider = 'box', scale= 0.9, color = color.gold, texture = 'tx/65b9e8ebfd04b8bd2b36d6ef22b385ea.jpg')
coin2 = Entity(model='cube', position = (-4.5, y + 1, -4.5), collider = 'box', scale= 0.9, color = color.blue, texture = 'tx/65b9e8ebfd04b8bd2b36d6ef22b385ea.jpg')
R = random.randint(0,4)
if R == 0:
    for z in range(1):
        for x in range(random.randint(1, 9)):
            coin.position = (x - 4.5, y + 1, z + 4.5)
if R == 1:
    for z in range(random.randint(0, 5)):
        for x in range(1):
            coin.position = (x - 4.5, y + 1, z)
if R == 3:
    for z in range(1):
        for x in range(random.randint(0, 5)):
            coin.position = (x, y + 1, z - 4.5)
if R == 4:
    for z in range(random.randint(1, 9)):
        for x in range(1):
            coin.position = (x + 4.5, y + 1, z - 4.5)
# -----------------------------------
R = random.randint(0, 4)
if R == 0:
    for z in range(1):
        for x in range(random.randint(1, 9)):
            coin2.position = (x - 4.5, y + 1, z + 4.5)
if R == 1:
    for z in range(random.randint(0, 5)):
        for x in range(1):
            coin2.position = (x - 4.5, y + 1, z)
if R == 3:
    for z in range(1):
        for x in range(random.randint(0, 5)):
            coin2.position = (x, y + 1, z - 4.5)
if R == 4:
    for z in range(random.randint(1, 9)):
        for x in range(1):
            coin2.position = (x + 4.5, y + 1, z - 4.5)
# player
player = Entity(model = 'cube', collider = 'box',position = (4.5,1,4.5), scale = 0.9, texture = 'white_cube', color = color.white)
# background
bord = Entity(model = 'plane',position = (0,0,0), scale = 10.2,texture = 'tx/scratch_me_by_darkwood67-d37rgbp.jpg', color = color.white)
# dice
num = Text(text= str(random.randint(1,6)), color=color.black, origin=(0, 0, 0))
dice = Entity(model = 'cube', position = (0,1,0), texture = 'white_cube', scale = 1, color = color.white)
# squares
class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            texture = 'white_cube',
            scale = 0.9,
            color = color.white
        )

# sides
for z in range(10):
    for x in range(1):
        voxel = Voxel(position=(x - 4.5,0,z - 4.5))
    for x in range(1):
        voxel = Voxel(position=(x + 4.5,0,z - 4.5))
# top/bottom
for z in range(1):
    for x in range(10):
        voxel = Voxel(position=(x - 4.5,0,z + 4.5))
    for x in range(10):
        voxel = Voxel(position=(x - 4.5,0,z - 4.5))
app.run()