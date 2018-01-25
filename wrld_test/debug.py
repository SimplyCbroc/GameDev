#debug tool
from tkinter import *
import random, time
tk = Tk()
canvas = Canvas(tk, width=1616, height=224)
canvas.pack()
tk.title('Test')

grass = PhotoImage(file="tile_grass.gif")
dirt = PhotoImage(file="tile_dirt.gif")
platform = PhotoImage(file="tile_platform.gif")
flag = PhotoImage(file="tile_flag.gif")
stone = PhotoImage(file="tile_stone.gif")
spikes = PhotoImage(file="tile_spikes.gif")
post = PhotoImage(file="tile_post.gif")
player = PhotoImage(file="obj_player_right.gif")
goblin = PhotoImage(file="obj_goblin_left.gif")
img_enemy1 = PhotoImage(file="obj_enemy1.gif")
bckg1 = PhotoImage(file="bckg_overworld.gif")
bricks = PhotoImage(file="tile_stonebrick.gif")
img_archer = PhotoImage(file="obj_archer.gif")
img_arrow = PhotoImage(file="obj_arrow.gif")
img_beam = PhotoImage(file="obj_beam.gif")
img_boss = PhotoImage(file="obj_boss.gif")
final = PhotoImage(file="ui_victory_text.gif")

jumping = False
frame = 0
lvlIndex = ['template.txt','test.txt']
currentLevel = 1
enemy = False
archer = False
arrowFiring = False
boss = False
text = False
ax = 0
ay = 0
collisions = 0
jumpIndex = 0
grav = 0
acceleration = 0
leftCollide = False
rightCollide = False
frame = 0
frame2 = 0
enemyIndex = 0
enemyMove = 1
enemyPos = 0
tileIndex = -32
vertIndex = 96
currentLevel = 1
enemy = False
archer = False
arrowFiring = False
boss = False
text = False
ax = 0
ay = 0
jumping = False
#canvas.create_image(808, 808, image=bckg1)
# levels are 52 tiles long
def layoutRead(file):
    global enemy1, enemy, enemyMove, enemyPos, ax, ay, archer, boss
    global obj_player, x, y
    global startX, startY, textIndex, vertText, text
    
    tileIndex = -32
    vertIndex = 96
    lv = open(file, 'r')
    canvas.delete('all')
    #canvas.create_image(808, 850, image=bckg1)
    for tile2 in lv.read():
        if (tileIndex/32) == 52:
            tileIndex = -32
            vertIndex += 32
        if tile2 == 'L':
            startX = tileIndex
            startY = vertIndex
            obj_player = canvas.create_image(startX, startY, image=player)
            x = (canvas.coords(obj_player))[0]
            y = (canvas.coords(obj_player))[1]
        tileIndex += 32
    tileIndex = -32
    vertIndex = 96
    lv = open(file, 'r')

    for tile in lv.read():
        
        if (tileIndex/32) == 52:
            tileIndex = -32
            vertIndex += 32
        if tile == 'G':
            left = canvas.create_line((tileIndex-16), (vertIndex-12), (tileIndex-16), (vertIndex+16))
            canvas.itemconfig(left, tags=('left'))
            right = canvas.create_line((tileIndex+14), (vertIndex-12), (tileIndex+14), (vertIndex+16))
            canvas.itemconfig(right, tags=('right'))
            solid = canvas.create_image(tileIndex, vertIndex, image=grass)
            canvas.itemconfig(solid, tags=('solid'))
        if tile == 'D':
            left = canvas.create_line((tileIndex-16), (vertIndex-12), (tileIndex-16), (vertIndex+16))
            canvas.itemconfig(left, tags=('left'))
            right = canvas.create_line((tileIndex+14), (vertIndex-12), (tileIndex+14), (vertIndex+16))
            canvas.itemconfig(right, tags=('right'))
            solid = canvas.create_image(tileIndex, vertIndex, image=dirt)
            canvas.itemconfig(solid, tags=('solid'))

        if tile == 'P':
            left = canvas.create_line((tileIndex-16), (vertIndex-12), (tileIndex-16), (vertIndex+16))
            canvas.itemconfig(left, tags=('left'))
            right = canvas.create_line((tileIndex+14), (vertIndex-12), (tileIndex+14), (vertIndex+16))
            canvas.itemconfig(right, tags=('right'))
            solid = canvas.create_image(tileIndex, vertIndex, image=platform)
            canvas.itemconfig(solid, tags=('solid'))   
        if tile == 'F':
            objective = canvas.create_image(tileIndex, vertIndex, image=flag)
            canvas.itemconfig(objective, tags='objective')
        if tile == 'S':
            death = canvas.create_image(tileIndex, vertIndex+6, image=spikes)
            canvas.itemconfig(death, tags=('death'))
        if tile == 'T':
            left = canvas.create_line((tileIndex-16), (vertIndex-12), (tileIndex-16), (vertIndex+16))
            canvas.itemconfig(left, tags=('left'))
            right = canvas.create_line((tileIndex+14), (vertIndex-12), (tileIndex+14), (vertIndex+16))
            canvas.itemconfig(right, tags=('right'))
            solid = canvas.create_image(tileIndex, vertIndex, image=stone)
            canvas.itemconfig(solid, tags=('solid'))
        if tile == 'K':
            canvas.create_image(tileIndex, vertIndex, image=post)
        
        if tile == 'O':
            canvas.create_image(tileIndex, vertIndex, image=goblin)
        if tile == 'E':
            enemyMove = 1
            enemyPos = 0
            enemy = True
            enemy1 = canvas.create_image(tileIndex, vertIndex, image=img_enemy1)
            canvas.itemconfig(enemy1, tags=('death'))
        if tile == 'B':
            left = canvas.create_line((tileIndex-16), (vertIndex-12), (tileIndex-16), (vertIndex+16))
            canvas.itemconfig(left, tags=('left'))
            right = canvas.create_line((tileIndex+14), (vertIndex-12), (tileIndex+14), (vertIndex+16))
            canvas.itemconfig(right, tags=('right'))
            solid = canvas.create_image(tileIndex, vertIndex, image=bricks)
            canvas.itemconfig(solid, tags=('solid'))
        if tile == 'A':
            archerEnemy = canvas.create_image(tileIndex, vertIndex, image=img_archer)
            archer = True
            ax = (canvas.coords(archerEnemy))[0]
            ay = (canvas.coords(archerEnemy))[1]
        if tile == 'M':
            archerEnemy = canvas.create_image(tileIndex, vertIndex, image=img_boss)
            boss = True
            archer = True
            ax = (canvas.coords(archerEnemy))[0]
            ay = (canvas.coords(archerEnemy))[1]
        tileIndex += 32
jumping = False
def walk_right(event):
    global acceleration
    if acceleration < 2:
        acceleration += 1
canvas.bind_all('<KeyPress-Right>', walk_right)
def walk_left(event):
    global leftCollide
    global acceleration
    if acceleration > -2:
        acceleration -= 1
canvas.bind_all('<KeyPress-Left>', walk_left)
def jump(event):
    global jumping
    global collisions
    if collisions == True:
        jumping = True
canvas.bind_all('<KeyPress-Up>', jump)
def arrowFire():
    global ax, ay, projectile, arrowFiring
    if not boss:
        projectile = canvas.create_image(ax, ay, image=img_arrow)
    if boss:
        for kj in range(0, 1):
            projectile = canvas.create_image(ax+(kj*12), ay, image=img_beam)
            canvas.itemconfig(projectile, tags=('projectile', 'death'))


    canvas.itemconfig(projectile, tags=('projectile', 'death'))
    arrowFiring = True
    
layoutRead(lvlIndex[currentLevel])
# main game loop

collisions = 0
jumpIndex = 0
grav = 0
acceleration = 0
leftCollide = False
rightCollide = False
frame = 0
frame2 = 0
enemyIndex = 0
enemyMove = 1
enemyPos = 0
while True:
    frame += 1
    frame2 += 1
    collided = canvas.find_overlapping((x-4), (y), (x+10), (y+17))
    for lkn in collided:
        tags = canvas.itemcget(lkn, "tags")
        if 'solid' not in tags:
            collisions = False
        else:
            collisions = True
        if 'death' in tags:
            
            collisions = 0
            jumpIndex = 0
            grav = 0
            acceleration = 0
            leftCollide = False
            rightCollide = False
            frame = 0
            frame2 = 0
            enemyIndex = 0
            enemyMove = 1
            enemyPos = 0
            tileIndex = -32
            vertIndex = 96
            enemy = False
            archer = False
            arrowFiring = False
            boss = False
            text = False
            ax = 0
            ay = 0
            jumping = False
            layoutRead(lvlIndex[currentLevel])
        if 'objective' in tags:
            collisions = 0
            jumpIndex = 0
            grav = 0
            acceleration = 0
            leftCollide = False
            rightCollide = False
            frame = 0
            frame2 = 0
            enemyIndex = 0
            enemyMove = 1
            enemyPos = 0
            tileIndex = -32
            vertIndex = 96
            enemy = False
            archer = False
            arrowFiring = False
            boss = False
            text = False
            ax = 0
            ay = 0
            jumping = False
            time.sleep(1)
            currentLevel += 1
            layoutRead(lvlIndex[currentLevel])
        if 'right' in tags:
            acceleration = 1
        if 'left' in tags:
            acceleration = -1
    if collisions == False and not jumping:
        grav += .07
        canvas.move(obj_player, acceleration, grav)
        y += grav
        x += acceleration
    else:
        canvas.move(obj_player, acceleration, 0)
        x += acceleration
        grav = 0
    if jumping:
        canvas.move(obj_player, acceleration, -(jumpIndex/2))
        y -= (jumpIndex/2)
        x += acceleration
        jumpIndex += 1
        if jumpIndex > 18:
            jumping = False
            jumpIndex = 0
    if enemy:
        canvas.move(enemy1, enemyMove, 0)
        enemyPos += enemyMove
        if enemyPos > 100:
            enemyMove = -1
            if archer:
                arrowFire()
        if enemyPos < -100:
            enemyMove = 1
            if archer:
                arrowFire()
    if arrowFiring and not boss:
        canvas.move('projectile', -5, 0)
    if frame > 200:
        frame = 0
        if boss:
            arrowFire()
            
    if arrowFiring and boss:
        canvas.move('projectile', -6, 0)

    time.sleep(0.01)
    if frame2 > 10:
        frame2 = 0
        if acceleration > 0 and collisions:
            acceleration -= 1
        if acceleration < 0 and collisions:
            acceleration += 1
    tk.update()
                    



