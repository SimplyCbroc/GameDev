from tkinter import *
import random, time
tk = Tk()
canvas = Canvas(tk, width=1616, height=350)
canvas.pack()
tk.title('Sandbox Test')
def create_new(index, side):
    global region, testRegion, testRegion3
    tile = ' '
    region = open("layout_lvl" + str(index) + ".txt", "w")
    testRegion = ''
    testRegion2 = ' '
    testRegion3 = ' '
    # nested tile writing
    for y in range(-6, 0):
        region.write('\n')
        for x in range(0, 52):
            testRegion += random.choice(['G','D','D','D'])
            if abs(y) == 1:
                tile = 'T'
                
            if abs(y) == 2:
                tile = 'D'
            if abs(y) == 3:
                tile = testRegion[x]
            if abs(y) == 4:
                if testRegion[x] == 'G':
                    testRegion2 = ' '
                else:
                    testRegion2 = 'G'
                    if random.choice(['A','B','C']) == 'C':
                        testRegion3 = 'G'
                    else:
                        testRegion3 = ' '
                    
                tile = testRegion2
            if abs(y) == 5:
                tile = testRegion3
                if side == 'left' and x == 4:
                    tile = 'L'
                if side == 'right' and x == 48:
                    tile = 'L'
            region.write(tile)
    region.close()
# Determining if the game needs to create a new world
import load
if load.load() == 'empty':
    index = 0
    create_new(index, 'right')
    print(index)

# Sprite designation
grass = PhotoImage(file="tile_grass.gif")
dirt = PhotoImage(file="tile_dirt.gif")
platform = PhotoImage(file="tile_platform.gif")
flag = PhotoImage(file="tile_flag.gif")
stone = PhotoImage(file="tile_stone.gif")
spikes = PhotoImage(file="tile_spikes.gif")
post = PhotoImage(file="tile_post.gif")
goblin = PhotoImage(file="obj_goblin_left.gif")
img_enemy1 = PhotoImage(file="obj_enemy1.gif")
bckg1 = PhotoImage(file="bckg_overworld.gif")
bricks = PhotoImage(file="tile_stonebrick.gif")
img_archer = PhotoImage(file="obj_archer.gif")
img_arrow = PhotoImage(file="obj_arrow.gif")
img_beam = PhotoImage(file="obj_beam.gif")
img_boss = PhotoImage(file="obj_boss.gif")
final = PhotoImage(file="ui_victory_text.gif")
tree1 = PhotoImage(file="Tree1.gif")
grass1 = PhotoImage(file="Deco_grass.gif")
canvas.create_image(808, 808, image=bckg1)

# Players

player1 = PhotoImage(file="Walk_1.gif", format="gif -index 0")
player2 = PhotoImage(file="Walk_1.gif", format="gif -index 1")
player3 = PhotoImage(file="Walk_1.gif", format="gif -index 2")
player4 = PhotoImage(file="Walk_1.gif", format="gif -index 3")
player5 = PhotoImage(file="Walk_1.gif", format="gif -index 4")
player6 = PhotoImage(file="Walk_1.gif", format="gif -index 5")
player7 = PhotoImage(file="Walk_1.gif", format="gif -index 6")
player8 = PhotoImage(file="Walk_1.gif", format="gif -index 7")

player9 = PhotoImage(file="Walk_2.gif", format="gif -index 0")
player10 = PhotoImage(file="Walk_2.gif", format="gif -index 1")
player11 = PhotoImage(file="Walk_2.gif", format="gif -index 2")
player12 = PhotoImage(file="Walk_2.gif", format="gif -index 3")
player13 = PhotoImage(file="Walk_2.gif", format="gif -index 4")
player14 = PhotoImage(file="Walk_2.gif", format="gif -index 5")
player15 = PhotoImage(file="Walk_2.gif", format="gif -index 6")
player16 = PhotoImage(file="Walk_2.gif", format="gif -index 7")

# Slashing Animation

slash1 = PhotoImage(file="ui_slashing.gif", format="gif -index 0")
slash2 = PhotoImage(file="ui_slashing.gif", format="gif -index 1")
slash3 = PhotoImage(file="ui_slashing.gif", format="gif -index 2")
slash4 = PhotoImage(file="ui_slashing.gif", format="gif -index 3")
slash5 = PhotoImage(file="ui_slashing.gif", format="gif -index 4")
slash6 = PhotoImage(file="ui_slashing.gif", format="gif -index 5")
slash7 = PhotoImage(file="ui_slashing.gif", format="gif -index 6")
slash8 = PhotoImage(file="ui_slashing.gif", format="gif -index 7")
slash9 = PhotoImage(file="ui_slashing.gif", format="gif -index 8")
slash10 = PhotoImage(file="ui_slashing.gif", format="gif -index 9")
slash11 = PhotoImage(file="ui_slashing.gif", format="gif -index 10")
slash12 = PhotoImage(file="ui_slashing.gif", format="gif -index 11")

slash21 = PhotoImage(file="ui_slashing2.gif", format="gif -index 0")
slash22 = PhotoImage(file="ui_slashing2.gif", format="gif -index 1")
slash23 = PhotoImage(file="ui_slashing2.gif", format="gif -index 2")
slash24 = PhotoImage(file="ui_slashing2.gif", format="gif -index 3")
slash25 = PhotoImage(file="ui_slashing2.gif", format="gif -index 4")
slash26 = PhotoImage(file="ui_slashing2.gif", format="gif -index 5")
slash27 = PhotoImage(file="ui_slashing2.gif", format="gif -index 6")
slash28 = PhotoImage(file="ui_slashing2.gif", format="gif -index 7")
slash29 = PhotoImage(file="ui_slashing2.gif", format="gif -index 8")
slash210 = PhotoImage(file="ui_slashing2.gif", format="gif -index 9")
slash211 = PhotoImage(file="ui_slashing2.gif", format="gif -index 10")
slash212 = PhotoImage(file="ui_slashing2.gif", format="gif -index 11")


playerFrames = [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, player12, player13, player14, player15, player16]

slashFrames = [slash1, slash2, slash3, slash4, slash5, slash6, slash7, slash8, slash9, slash10, slash11, slash12]
slashFrames2 = [slash21, slash22, slash23, slash24, slash25, slash26, slash27, slash28, slash29, slash210, slash211, slash212]

# Variable designation
jumping = False
frame = 0
currentLevel = 0
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
enemy = False
archer = False
arrowFiring = False
boss = False
text = False
ax = 0
ay = 0

# Level loading

def layoutRead(file):
    global enemy1, enemy, enemyMove, enemyPos, ax, ay, archer, boss
    global obj_player, x, y
    global startX, startY, textIndex, vertText, text
    
    tileIndex = -32
    vertIndex = 180
    lv = open(file, 'r')
    canvas.delete('all')
    canvas.create_rectangle(0, 0, 2000, 500, fill='#bdf7ff')
    canvas.create_image(0, 450, image=bckg1)
    canvas.create_image(900, 450, image=bckg1)
    canvas.create_image(1400, 450, image=bckg1)

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
            if random.randrange(0, 2) == 1:
                if random.choice(['tree', 'grass', 'grass', 'grass']) == 'tree':
                    deco = canvas.create_image(tileIndex, vertIndex-64, image=tree1)
                    canvas.itemconfig(deco, tags=('deco'))
                else:
                    deco = canvas.create_image(tileIndex, vertIndex-24, image=grass1)
                    canvas.itemconfig(deco, tags=('deco'))

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
        if tile == 'L':
            startX = tileIndex
            startY = vertIndex
            obj_player = canvas.create_image(startX, startY, image=playerFrames[0])
            x = (canvas.coords(obj_player))[0]
            y = (canvas.coords(obj_player))[1]
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
    canvas.lower('deco', 'solid')


# Keybind designation

def walk_right(event):
    global acceleration, playerIndex
    if acceleration < 2:
        acceleration += 1
    if not playerIndex == 8:
        playerIndex += 1
    if playerIndex > 7:
        playerIndex = 0
        
canvas.bind_all('d', walk_right)
def walk_left(event):
    global leftCollide
    global acceleration, playerIndex, playerIndex2
    if acceleration > -2:
        acceleration -= 1
    if not playerIndex2 == 8:
        playerIndex2 += 1
        playerIndex = playerIndex2 + 7
    if playerIndex2 == 8:
        playerIndex2 = 0
        playerIndex = 8
    
canvas.bind_all('a', walk_left)
def jump(event):
    global jumping
    global collisions
    if collisions == True:
        jumping = True
canvas.bind_all('w', jump)
canvas.bind_all('<space>', jump)
layoutRead('layout_lvl' + str(currentLevel) + '.txt')

def attack(event):
    global sword
    sword = True
canvas.bind_all('<Button-1>', attack)

# Main game loop
playerIndex = 0
playerIndex2 = 0
jumpIndex2 = 0
slashIndex = 0
sword = False
swordSlash = canvas.create_line(0, 0, 1, 1)
while True:
    frame += 1
    frame2 += 1
    collided = canvas.find_overlapping((x-4), (y), (x+10), (y+17))
    if x < 0:
        create_new(0, 'right')
        layoutRead('layout_lvl' + str(currentLevel) + '.txt')

    for lkn in collided:
        tags = canvas.itemcget(lkn, "tags")
        if 'solid' not in tags:
            collisions = False
        else:
            collisions = True
        
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
        if jumpIndex > 10:
            jumpIndex2 = 1
        if jumpIndex2 == 1:
            jumpIndex -= 2
        if jumpIndex == 0 and jumpIndex2 == 1:
            jumping = False
            jumpIndex2 = 0
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
    canvas.delete(obj_player)
    obj_player = canvas.create_image(x, y, image=playerFrames[playerIndex])
    canvas.lower(obj_player, 'solid')
    canvas.delete(swordSlash)

    if sword and playerIndex < 8:
        swordSlash = canvas.create_image(x+24, y-4, image=slashFrames[slashIndex])
        slashIndex += 1
        if collisions == True:
            grav = 0
    if sword and playerIndex > 7:
        swordSlash = canvas.create_image(x-24, y-4, image=slashFrames2[slashIndex])
        slashIndex += 1
        if collisions == True:
            grav = 0
    if slashIndex == 11:
        sword = False
        slashIndex = 0
        canvas.delete(swordSlash)
    tk.update()
