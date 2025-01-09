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
#sprites, images en platformer
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
#beweging
@play.when_key_pressed('right')
def platformer_bewegen_rechts(key):
    if key == 'right':
        platformer.x = platformer.x + 5

@play.when_key_released('right')
def platformer_stoppen_rechts(key):
    if key == 'right':
        platformer.x_speed = 0
        platformer.x = platformer.x + 0

@play.when_key_pressed('left')
def platformer_bewegen_links(key):
    if key == 'left':
        platformer.x = platformer.x - 5
    #print(f"Nieuwe positie: ({platformerx}, {platformery})")

@play.when_key_released('left')
def platformer_stoppen_links(key):
    if key == 'left':
        platformer.x_speed = 0
        platformer.x = platformer.x + 0

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
    global platformery, grond
    if platformery == platformhoogte or platformer.is_touching(boxlevel2_1) or platformer.is_touching(boxlevel2_2):
        grond = 'ja'
    elif platformer.is_touching(level1) or platformer.is_touching(level2):
        grond = 'nee'
    else:
        grond = 'nee'

@play.when_key_pressed('space')
async def spatie(key):
    global grond, snelheidy
    #print(grond, spring_kracht)    
    if grond == 'ja':
        snelheidy = spring_kracht
        platformer.physics.y_speed = snelheidy
        grond = 'nee'
    await play.timer(1)

#spel en levels
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
@platformer.when_touching(level1)
def level2_plus_sprites():
    global level2, boxlevel2_1
    level2 = play.new_box(
    color='light green',
    width=20,
    height=20,
    x=350,
    y=50,
    angle=0,
)
    boxlevel2_1 = play.new_box(
        color='black',
        width=150,
        height=20,
        x=-100,
        y=-80,
        angle=25,
)
    boxlevel2_1.start_physics(
        obeys_gravity = False,
        stable = True,
        can_move = False,
        bounciness = 0,
)
    boxlevel2_2 = play.new_box(
        color='black',
        width=50,
        height=20,
        x=100,
        y=10,
        angle=345,
)
    boxlevel2_2.start_physics(
        obeys_gravity = False,
        stable = True,
        can_move = False,
        bounciness = 0,
)
def level1_verdwijnen():
    if platformer.is_touching(level1):
        platformer.go_to(x=0, y=104)
        level1.hide
play.start_program()