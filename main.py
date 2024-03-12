@namespace
class SpriteKind:
    healthAdd = SpriteKind.create()
    mediumEnemy = SpriteKind.create()
    hardestEnemy = SpriteKind.create()
    biggestBaddestEnemy = SpriteKind.create()
    attack = SpriteKind.create()

def on_hit_wall(sprite, location):
    global jumpCount
    if not (GreenApple.is_hitting_tile(CollisionDirection.TOP)):
        jumpCount = 0
    if GreenApple.is_hitting_tile(CollisionDirection.LEFT) or GreenApple.is_hitting_tile(CollisionDirection.RIGHT):
        GreenApple.vy = 0
scene.on_hit_wall(SpriteKind.player, on_hit_wall)

def on_on_overlap(sprite2, otherSprite):
    sprites.destroy(sprite2, effects.fire, 100)
    scaling.scale_by_percent(otherSprite,
        -10,
        ScaleDirection.UNIFORMLY,
        ScaleAnchor.MIDDLE)
sprites.on_overlap(SpriteKind.attack,
    SpriteKind.biggestBaddestEnemy,
    on_on_overlap)

def on_b_pressed():
    global flyingSeed
    flyingSeed = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . e e e . . . . . . . . . 
                    . e e e e e e e e e . . . . . . 
                    . e e e e e e e e e e e e e e . 
                    . e e e e e e e e e e e e e e e 
                    . . e e e e e e e e e e e e . . 
                    . . . . . . e e e . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        GreenApple,
        -75,
        0)
    flyingSeed.set_kind(SpriteKind.attack)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap2(sprite5, otherSprite2):
    sprites.destroy(otherSprite2, effects.bubbles, 100)
    info.change_life_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.healthAdd, on_on_overlap2)

def enemyLevel2(numEnemyLevel: number):
    global spawningList, projectile
    spawningList = [assets.image("""
            archnemesis
        """),
        assets.image("""
            rottenBanana
        """),
        img("""
            . . . . . . . e c 7 . . . . . . 
                    . . . . e e e c 7 7 e e . . . . 
                    . . c e e e e c 7 e 2 2 e e . . 
                    . c e e e e e c 6 e e 2 2 2 e . 
                    . c e e e 2 e c c 2 4 5 4 2 e . 
                    c e e e 2 2 2 2 2 2 4 5 5 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 4 4 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 4 2 e 
                    . e e e 2 2 2 2 2 2 2 2 2 4 e . 
                    . 2 e e 2 2 2 2 2 2 2 2 4 2 e . 
                    . . 2 e e 2 2 2 2 2 4 4 2 e . . 
                    . . . 2 2 e e 4 4 4 2 e e . . . 
                    . . . . . 2 2 e e e e . . . . .
        """),
        img("""
            4 4 4 . . 4 4 4 4 4 . . . . . . 
                    4 5 5 4 4 5 5 5 5 5 4 4 . . . . 
                    b 4 5 5 1 5 1 1 1 5 5 5 4 . . . 
                    . b 5 5 5 5 1 1 5 5 1 1 5 4 . . 
                    . b d 5 5 5 5 5 5 5 5 1 1 5 4 . 
                    b 4 5 5 5 5 5 5 5 5 5 5 1 5 4 . 
                    c d 5 5 5 5 5 5 5 5 5 5 5 5 5 4 
                    c d 4 5 5 5 5 5 5 5 5 5 5 1 5 4 
                    c 4 5 5 5 d 5 5 5 5 5 5 5 5 5 4 
                    c 4 d 5 4 5 d 5 5 5 5 5 5 5 5 4 
                    . c 4 5 5 5 5 d d d 5 5 5 5 5 b 
                    . c 4 d 5 4 5 d 4 4 d 5 5 5 4 c 
                    . . c 4 4 d 4 4 4 4 4 d d 5 d c 
                    . . . c 4 4 4 4 4 4 4 4 5 5 5 4 
                    . . . . c c b 4 4 4 b b 4 5 4 4 
                    . . . . . . c c c c c c b b 4 .
        """),
        img("""
            . . 2 2 b b b b b . . . . . . . 
                    . 2 b 4 4 4 4 4 4 b . . . . . . 
                    2 2 4 4 4 4 d d 4 4 b . . . . . 
                    2 b 4 4 4 4 4 4 d 4 b . . . . . 
                    2 b 4 4 4 4 4 4 4 d 4 b . . . . 
                    2 b 4 4 4 4 4 4 4 4 4 b . . . . 
                    2 b 4 4 4 4 4 4 4 4 4 e . . . . 
                    2 2 b 4 4 4 4 4 4 4 b e . . . . 
                    . 2 b b b 4 4 4 b b b e . . . . 
                    . . e b b b b b b b e e . . . . 
                    . . . e e b 4 4 b e e e b . . . 
                    . . . . . e e e e e e b d b b . 
                    . . . . . . . . . . . b 1 1 1 b 
                    . . . . . . . . . . . c 1 d d b 
                    . . . . . . . . . . . c 1 b c . 
                    . . . . . . . . . . . . c c . .
        """)]
    if numEnemyLevel <= 3:
        for index in range(4):
            spawningList.shift()
        for index2 in range(30):
            projectile = sprites.create_projectile_from_side(spawningList._pick_random(), 0, 60)
            projectile.set_kind(SpriteKind.healthAdd)
            projectile.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
            tiles.place_on_tile(projectile,
                tiles.get_tile_location(randint(0, 29), randint(0, 140)))
    elif numEnemyLevel <= 7:
        for index3 in range(3):
            spawningList.shift()
        for index4 in range(60):
            projectile = sprites.create_projectile_from_side(spawningList._pick_random(), 0, 60)
            projectile.set_kind(SpriteKind.mediumEnemy)
            projectile.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
            tiles.place_on_tile(projectile,
                tiles.get_tile_location(randint(0, 29), randint(0, 140)))
    else:
        for index5 in range(80):
            projectile = sprites.create_projectile_from_side(spawningList._pick_random(), 0, 60)
            projectile.set_kind(SpriteKind.hardestEnemy)
            projectile.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
            tiles.place_on_tile(projectile,
                tiles.get_tile_location(randint(0, 29), randint(0, 140)))

def on_a_pressed():
    global jumpCount
    if jumpCount < 2:
        jumpCount += 1
        GreenApple.vy = -150
        animation.run_image_animation(GreenApple,
            [img("""
                    .............................
                                .............................
                                .............f...............
                                ............f7f..............
                                ...........f777f.............
                                ..........f77777f............
                                .........f777777f............
                                ........f7777777ff...........
                                ........f77777f777ff.........
                                .....f..f77777f77777f........
                                ....f7f.f7777f777ff7f........
                                .....f7f7777f7777ff7f........
                                ....ff7f7777f77777777f.......
                                ...f777f7777f77777777f.......
                                ..f7777f7777f77777777f.......
                                ..ff777f7777f77777777fff.....
                                ...f777f7777f7777ff77feef....
                                ...f777f7777ff777ff7ffefef...
                                ..f77777f77777f77777f.f.fef..
                                ..fff77fff7777f7777ff....f...
                                .....f7f.f7777777ff..........
                                ....f7f..f7777777f...........
                                .....f...ff77777ff...........
                                ..........ff7777f............
                                ...........ff77f.............
                                ............ffff.............
                                ..............f..............
                                .............................
                                .............................
                """),
                img("""
                    .............................
                                .............................
                                .........ff..ff..............
                                .........f7fff7f.............
                                .......f.f777777f.f..........
                                ......f7f7777777ff7f.........
                                .......f7777777777f..........
                                ........ff7fffffff...........
                                .........ff7777777ffff.......
                                ......ffff777777777777f......
                                .....ff7777777777777777f.....
                                ....ff777777777777777777f....
                                ...ff777777fffffff7777777f...
                                ...f7777777f777777f7777777f..
                                ..ff77777ff77777777ff7777f...
                                ...ff7777777777777777777f....
                                .....ff77777777777777fff.....
                                ......fff77ff7777ff77f.......
                                ........f77ff7777ff7f........
                                .........f7777777777f........
                                .........fff77777fff.........
                                ...........ffffff............
                                ..........feef...............
                                ...........fef...............
                                ..........fef................
                                .........fef.................
                                ..........f..................
                                .............................
                                .............................
                """),
                img("""
                    .............................
                                .............................
                                ..................f..........
                                .................fef.........
                                ................fef..........
                                ...............fef...........
                                ...............feef..........
                                ............ffffff...........
                                .........fff77777fff.........
                                ........f7777777777f.........
                                ........f7ff7777ff77f........
                                .......f77ff7777ff77fff......
                                .....fff77777777777777ff.....
                                ....f7777777777777777777ff...
                                ...f7777ff77777777ff77777ff..
                                ..f7777777f777777f7777777f...
                                ...f7777777fffffff777777ff...
                                ....f777777777777777777ff....
                                .....f7777777777777777ff.....
                                ......f777777777777ffff......
                                .......ffff7777777ff.........
                                ...........fffffff7ff........
                                ..........f7777777777f.......
                                .........f7ff7777777f7f......
                                ..........f.f777777f.f.......
                                .............f7fff7f.........
                                ..............ff..ff.........
                                .............................
                                .............................
                """)],
            100,
            False)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap3(sprite4, otherSprite3):
    sprites.destroy(otherSprite3, effects.fire, 100)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.mediumEnemy, on_on_overlap3)

def on_on_overlap4(sprite6, otherSprite32):
    sprites.destroy(otherSprite32, effects.fire, 100)
    info.change_life_by(-2)
sprites.on_overlap(SpriteKind.player, SpriteKind.hardestEnemy, on_on_overlap4)

def on_overlap_tile(sprite3, location3):
    if controller.up.is_pressed():
        GreenApple.vy = -50
    else:
        GreenApple.vy = 50
    
    def on_throttle():
        info.change_life_by(-1)
    timer.throttle("action", 1000, on_throttle)
    
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava0,
    on_overlap_tile)

def lavaRisingLevel(numLavaLevel: number):
    global lavaBlock
    if numLavaLevel <= 3:
        lavaBlock += 1
        for index6 in range(31):
            tiles.set_tile_at(tiles.get_tile_location(index6, lavaBlock * -1 + 154),
                sprites.dungeon.hazard_lava0)
            tiles.set_wall_at(tiles.get_tile_location(index6, lavaBlock * -1 + 154), False)
    elif numLavaLevel <= 7:
        lavaBlock += 5
        for index7 in range(31):
            tiles.set_tile_at(tiles.get_tile_location(index7, lavaBlock * -1 + 154),
                sprites.dungeon.hazard_lava0)
            tiles.set_wall_at(tiles.get_tile_location(index7, lavaBlock * -1 + 154), False)
    else:
        lavaBlock += 10
        for index8 in range(31):
            tiles.set_tile_at(tiles.get_tile_location(index8, lavaBlock * -1 + 154),
                sprites.dungeon.hazard_lava0)
            tiles.set_wall_at(tiles.get_tile_location(index8, lavaBlock * -1 + 154), False)

def on_overlap_tile2(sprite22, location2):
    global finalBoss, finalBossSpawned
    if finalBossSpawned == False:
        if GreenApple.tile_kind_at(TileDirection.BOTTOM, sprites.castle.tile_path5):
            finalBoss = sprites.create(assets.image("""
                    archnemesis
                """),
                SpriteKind.biggestBaddestEnemy)
            finalBoss.ay = 800
            finalBoss.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, False)
            tiles.place_on_tile(finalBoss, tiles.get_tile_location(5, 20))
            finalBoss.vx += 10
    finalBossSpawned = True
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile2)

def on_on_overlap5(sprite7, otherSprite4):
    
    def on_throttle2():
        info.change_life_by(-10)
    timer.throttle("action", 1000, on_throttle2)
    
sprites.on_overlap(SpriteKind.player,
    SpriteKind.biggestBaddestEnemy,
    on_on_overlap5)

finalBoss: Sprite = None
lavaBlock = 0
projectile: Sprite = None
spawningList: List[Image] = []
flyingSeed: Sprite = None
finalBossSpawned = False
jumpCount = 0
GreenApple: Sprite = None
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99d99bbbbbcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99ddbdd66168bcccccc9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff999ddbbbd66888111ccccccb99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9966ddbbbb6688811818ccccccbbc99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdd69dddbbb66618881888818818cccccbe9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddd96dd6b6dbd68888888888888888cccccc99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffdbbd9666666dbb668886888888cccccccccccccc9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffdbbb99666966d68866888888cccccccccccccccccc69ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffdbbb999669666666888888888ccccbbbcc8bcccccccccc9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffdbbb999666666666888888888cbbcbe8bbbcbcccccbbcccb9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff9bbb999666666666688888888bccb888888bbbbb88888bcccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffdbbb999669666666866888868bbbbb8888888ccc888b88bbc8cccffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffdbbb9d99ddd666668868888688bbcb888888888bc888bcc8bc886c9fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbddd966666888688888888888888b88888888888cc8ccc886c9ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffdbbbbbbdd6966666666868888888888bbdbbebb8888888888bcc8c86c9fffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff9bbdbddd6666666666888688868888ddddddddde8888888888bccbbccccfffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff9dbb9dd666666666668868888888bddddddbdbbddcccccd88b8ebccbbbbc9ffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffdd99999666666666668868888888bdddddbbbbbdbbbccccccb8bbbccc8bbb9fffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff9dd99996696966666666668888bbbdddddbbbddbbbbbbbbbcccc8bcccbb8bbcfffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff9d999996666966666668688888bbdddbbbbdbbbbbbbbbbbcccccc8bbccc88bc9ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff99999999666996696668868868bbdddddbbbdbbbbbbbbbbbbcbccc88bcccc88c6ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff999996696669666966d8868666bddbbbddbbdbbbbbbbbbbbbcccccc88bbccc8869fffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9999996699669666666d6688668bddbbdbbbbbbbbbbbbbbbbbccccccc88bcccc866fffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9dd999669966666666666688668bdddbbbbbbbbbbbbbbbbbbbccccccc888bbccc669ffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff999999669d69666666666688868bddbbbdbbbbbbbbbbbbbbbbcccccccc888bbcc869ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99999996ddd69666666688888868ddbddbbbbbbbbbbbbbbbbbbccccccccc888888866ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff999999969ddd6669666688688888bbbbbbbbbbbbbbbbbbbbbbbbccbccccc8888888869fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99999966ddddd669666688888888bbbbbbbbbbbbbbbbbbbbbbbcbccccccccc88888869fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff999bb99666dddd6666666668886888bbbbbbbbbbbbbbbbbbbbbbcccccccccccc8888889fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbbb966696666666666888886888bbbbbbbbbbbbbbbbbbbbbbcbccccccccccc888886fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbdbb666969666666668888868888bbbbbbbbbbbbbbbbbbbbccbccccccccccc8888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99dbbbbb6696966666666668886868888bbbbeb888bbbbbbbbbcccccccccccccc8888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbbbbbe6969666666666888888888888888888888bbbbbbbbccccccccccccc88888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbccbc66966666666688888688888888888d888ebbbbbbbcccccccccccbb88888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbbcc69996666688668886888888dd88dbbd88bbbbbbbccccccccccceb88888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbbccc999966668868888888888ddddbbbbd88cbbbbbbbbccccccccc8888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9ebbbbcccccccc9966666688888888888888ddbbbb888bbbbbbbbccccccccc8888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbccccccccc666666888866888888888dddddbdd88bbbbbbccccccccc88888888bb9ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffbbbbbbcccccccccc6666688888888888888888d8888888bbbbbbccccccccc88888888bb9ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9dbbbbccbbccccccb666688868888888888888888888888bbbbbccccccccc888888888b9ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9dbbbbbbbbcccccbb66666688888888888888888888888bbbbccccccccccc88888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbcccccccb666666688888888888888888888888bbbbcccccccccc888888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbccccccbb666666688888888888888888888888bbbbcccccccccc88888888886fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbbbbbbbccccb6666668888888888888888888888888bbbbcbcccccccc88888888886fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99dbbbcbbccccb6666668888888888888888888888888bbbbbccccccccc888cc888869fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99dbbbcccccccc6666668688688888888888888888888bbbbccccccccc8888cc888869fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff999bbbbbccccbc6666666688688888888888888888888bbbbcccccccc88888dd88886ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff969bbbbbbcccc69666666668688868888888888888888bbbbccccccc88888bd888886ffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff99bbbbcccccc696bb668888888868888888888888888bbbcccccccc8888bbd888869ffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9999bbbcccc9666dbbb8888888888888888888888888ccbcccccccc8888bc888886fffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff699bbbbccc966966bbb8888888888888888888888888bbbbccccc88888bcc88869fffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9999bbcccc666666dbbdd88888888688888888888888bbcccccc88888888888669fffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9699dbcccc66666666bb6d8888888688888888888888bbcccccc8888888888869ffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff9696bbbcc66666666dbbd6886868888888888888888bbcbccc8888888888d669ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff999ebbccc666666666dbb8868888688888888888888bbbccc8888888889b69fffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff969ccbcc66996666666bbb868888888888888888888bbbc888888888888b6ffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff96ccccc966966666666bb8688666888888888888888b8888888888888699ffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff99ccbc996666666666dbb6888668888888888888888888888888888869fffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff969ccb9666666666666dbb88866888888888888888888888888888869ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffff969ccc6696666666666dd8888668888888888888888888888888866fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffff969cc9669666966d66dd8888868888888888888888888bb8888669fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff96ccc66699669dddd888868888888888888888888888be888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffff96c66669966666dd88886666668888888888888888dd888669fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffff96966669966ddd686886868888888888888888888d888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffff969666696666666688686888888888888888888888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffff9966966966666666886888888888888886888888669fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9699996666666888888888888888888118888699ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff969996666668888881188888888881888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff996999666688881818888888881886669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9961161186618811188886116699ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99161111611118111666699fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9999661166669999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff999999999fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
"""))
tiles.set_current_tilemap(tilemap("""
    Runrunrun
"""))
lavaRisingLevel(game.ask_for_number("Lava Difficulty Level (0-easiest/9-hardest)", 1))
fallingSprite = game.ask_for_number("Enemy Difficulty Level (0-easiest/9-hardest)", 1)
GreenApple = sprites.create(assets.image("""
    myImage
"""), SpriteKind.player)
tiles.place_on_tile(GreenApple, tiles.get_tile_location(24, 26))
controller.move_sprite(GreenApple, 100, 0)
GreenApple.ay = 300
GreenApple.set_stay_in_screen(True)
scene.camera_follow_sprite(GreenApple)
jumpCount = 0
info.set_life(100)
finalBossSpawned = False

def on_update_interval():
    enemyLevel2(fallingSprite)
game.on_update_interval(2000, on_update_interval)

def on_update_interval2():
    lavaRisingLevel(1)
game.on_update_interval(1000, on_update_interval2)
