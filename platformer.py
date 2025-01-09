import play
#variabelen
grond = 'ja'
platformerx = 50
platformery = 150
spring_kracht = 50
zwaartekracht = -1
snelheidy = 0
platformx = 200
platformy = 0
platformbreedte = 300
platformhoogte = 104
tijd = 0
#sprites, images, tijd en platformer
@play.when_program_starts
def laat_de_goede_dingen_zien():
    level1.show()
    level2.hide()
    level3.hide()
    level4.hide()
    boxlevel2_1.hide()
    boxlevel2_2.hide()
    boxlevel3_1.hide()
    boxlevel3_2.hide()
    boxlevel3_3.hide()
    boxlevel4_1.hide()
    boxlevel4_2.hide()
    boxlevel4_3.hide()
    boxlevel4_4.hide()

floorgame = play.new_image('floorrealreal.jpg',
                           x=-300,
                           y=-250,
                           size=100,
                           angle=0,
)
floorgame2 = play.new_image('floorrealreal2.jpg',
                            x=0,
                            y=-250,
                            size=100,
                            angle=0,
)
floorgame3 = play.new_image('floorrealreal3.jpg',
                            x=300,
                            y=-250,
                            size=100,
                            angle=0,
)

#NIEUWE VERSIE 300 BIJ 104
floorgame.start_physics(
    obeys_gravity = False,
    stable = True,
    can_move = False,
    bounciness = 0,
)
floorgame2.start_physics(
    obeys_gravity = False,
    stable = True,
    can_move = False,
    bounciness = 0,
)
floorgame3.start_physics(
    obeys_gravity = False,
    stable = True,
    can_move = False,
    bounciness = 0,
)
#level sprites
tekstlevel = play.new_text(
    words='Level 1',
    x=0,
    y=250,
    font='arial.ttf',
    font_size=50,
    color='black',
    angle=0,
    size=100,
)
level1 = play.new_box(
    color='light green',
    width=20,
    height=20,
    x=200,
    y=-50,
    angle=0,
)
level2 = play.new_box(
    color='light green',
    width=20,
    height=20,
    x=350,
    y=50,
    angle=0,
)
level3 = play.new_box(
    color='light green',
    width=20,
    height=20,
    x=200,
    y=200,
    angle=0,
)
level4 = play.new_box(
    color='light green',
    width=20,
    height=20,
    x=-225,
    y=0,
    angle=0,
)
boxlevel2_1 = play.new_box(
    color='black',
    width=150,
    height=20,
    x=-100,
    y=-80,
    angle=0,
)
boxlevel2_2 = play.new_box(
    color='black',
    width=50,
    height=20,
    x=100,
    y=10,
    angle=0,
)
boxlevel3_1 = play.new_box(
    color='black',
    width=40,
    height=20,
    x=150,
    y=0,
    angle=0,
)
boxlevel3_2 = play.new_box(
    color='black',
    width=40,
    height=20,
    x=50,
    y=-80,
    angle=0,
)
boxlevel3_3 = play.new_box(
    color='black',
    width=40,
    height=20,
    x=200,
    y=50,
    angle=0,
)
boxlevel4_1 = play.new_box(
    color='black',
    width=20,
    height=20,
    x=325,
    y=120,
    angle=0,
)
boxlevel4_2 = play.new_box(
    color='black',
    width=190,
    height=20,
    x=175,
    y=80,
    angle=90,
)
boxlevel4_3 = play.new_box(
    color='black',
    width=100,
    height=20,
    x=225,
    y=10,
    angle=0,
)
boxlevel4_4 = play.new_box(
    color='black',
    width=50,
    height=20,
    x=-25,
    y=0,
    angle=0,
)
platformer = play.new_circle(color = 'blue',
                          x = 0,
                          y = 0,
                          radius = 20,
                          border_width = 0,
                          angle = 0,
)
platformer.start_physics(can_move = True,
                         stable=True,
                         bounciness=0,
)
#levels bouwen
@platformer.when_touching(level1)
def bouw_level_2():
    tekstlevel.words = 'Level 2'
    level1.hide()
    if level1.physics:
        level1.physics.pause()
    level2.show()
    boxlevel2_1.show()
    boxlevel2_2.show()
    
    boxlevel2_1.start_physics(
    obeys_gravity = False,
    stable = True,
    can_move = False,
    bounciness = 0,
    friction = 1,
)
    boxlevel2_2.start_physics(
    obeys_gravity = False,
    stable = True,
    can_move = False,
    bounciness = 0,
    friction = 1,
)
@platformer.when_touching(level2)
def bouw_level_3():
    tekstlevel.words = 'Level 3'
    boxlevel2_1.hide()
    boxlevel2_2.hide()
    level1.hide()
    if level1.physics:
        level1.physics.pause()
    level2.hide()
    if level2.physics:
        level2.physics.pause()
    level3.show()
    boxlevel3_1.show()
    boxlevel3_2.show()
    boxlevel3_3.show()
    
    boxlevel3_1.start_physics(
    obeys_gravity = False,
    stable = True,
    can_move = False,
    friction = 1,
    bounciness = 0,
)
    boxlevel3_2.start_physics(
        obeys_gravity = False,
        stable = True,
        can_move = False,
        friction = 1,
        bounciness = 0,
)
    boxlevel3_3.start_physics(
        obeys_gravity = False,
        stable = True,
        can_move = False,
        friction = 1,
        bounciness = 0,
)
@platformer.when_touching(level3)
def bouw_level4():
    tekstlevel.words = 'Level 4'
    level1.hide()
    if level1.physics:
        level1.physics.pause()
    level2.hide()
    if level2.physics:
        level2.physics.pause()
    level3.hide()
    if level3.physics:
        level3.physics.pause()
    level4.show()
    boxlevel3_1.hide()
    boxlevel3_2.hide()
    boxlevel3_3.hide()
    boxlevel4_1.show()
    boxlevel4_2.show()
    boxlevel4_3.show()
    boxlevel4_4.show()
    
    boxlevel4_1.start_physics(
        obeys_gravity = False,
        can_move = False,
        stable = True,
        bounciness = 0,
        friction = 1,
)
    boxlevel4_2.start_physics(
        obeys_gravity = False,
        can_move = False,
        stable = True,
        bounciness = 0,
        friction = 1,
)
    boxlevel4_3.start_physics(
        obeys_gravity = False,
        can_move = False,
        stable = True,
        bounciness = 0,
        friction = 1,
)
    boxlevel4_4.start_physics(
        obeys_gravity = False,
        can_move = False,
        stable = True,
        bounciness = 0,
        friction = 1,
)
@platformer.when_touching(level4)
def bouw_einde():
    tekstlevel.words = 'Gefeliciteerd!'
    level1.hide()
    if level1.physics:
        level1.physics.pause()
    level2.hide()
    if level2.physics:
        level2.physics.pause()
    level3.hide()
    if level3.physics:
        level3.physics.pause()
    level4.hide()
    level4.hide()
    if level4.physics:
        level4.physics.pause()
    boxlevel4_1.hide()
    boxlevel4_2.hide()
    boxlevel4_3.hide()
    boxlevel4_4.hide()
    @play.repeat_forever
    async def do():
        tekstlevel.go_to(play.mouse)

#beweging
@play.when_key_pressed('right')
def platformer_bewegen_rechts(key):
    if key == 'right':
        platformer.x = platformer.x + 5

@play.when_key_released('right')
def platformer_stoppen_rechts(key):
    if key == 'right':
        platformer.x_speed = 0

@play.when_key_pressed('left')
def platformer_bewegen_links(key):
    if key == 'left':
        platformer.x = platformer.x - 5
    #print(f"Nieuwe positie: ({platformerx}, {platformery})")

@play.when_key_released('left')
def platformer_stoppen_links(key):
    if key == 'left':
        platformer.x_speed = 0

@play.repeat_forever
def update_positie():
    global platformery, snelheidy
    snelheidy += zwaartekracht
    platformery += snelheidy
    platformery = platformy + platformhoogte
    snelheidy = 0
    #print(f"Positie: ({platformerx}, {platformery}), Snelheid: {snelheidy}")

@play.repeat_forever
def check_grond():
    global grond
    if platformery == platformhoogte:
        grond = 'ja'
        #print(grond)
    elif (round(platformer.x)) or (round(platformer.y)) == (round(level1.x)) or (round(level1.y)) or (round(level2.x)) or (round(level2.y)) or (round(level3.x)) or (round(level3.y)):
        grond = 'nee'
        #print(grond)
    elif (round(platformer.x)) or (round(platformer.y)) == (round(boxlevel2_1.x)) or (round(boxlevel2_1.y)) or (round(boxlevel2_2.x)) or (round(boxlevel2_2.y)) or (round(boxlevel3_1.x)) or (round(boxlevel3_1.y)):
        grond = 'ja'
    else:
        grond = 'nee'
        #print(grond)

@play.when_key_pressed('space')
async def spatie(key):
    global grond, snelheidy
    #print(grond, spring_kracht)    
    if grond == 'ja':
        snelheidy = spring_kracht
        platformer.physics.y_speed = snelheidy
        grond = 'nee'
    await play.timer(1)
play.start_program()
