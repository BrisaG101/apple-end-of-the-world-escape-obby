namespace SpriteKind {
    export const simpleEnemy = SpriteKind.create()
    export const mediumEnemy = SpriteKind.create()
    export const hardestEnemy = SpriteKind.create()
    export const biggestBaddestEnemy = SpriteKind.create()
}
function enemyLevel (numEnemyLevel: number) {
    enemyList = [
    assets.image`archnemesis`,
    assets.image`rottenBanana`,
    img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . 3 3 . . . . 
        . . . . . . . 3 3 3 . . . . . . 
        . . . . . 3 3 3 . . . . . . . . 
        . . . . 3 3 . . . . . . . . . . 
        . . . . . . 3 3 3 3 3 3 3 . . . 
        . . . . . . . . . . . 3 3 3 . . 
        . . . . . . . . 3 3 3 . . . . . 
        . . . . . . 3 3 . . . . . . . . 
        . . . . . . 3 . . . . . . . . . 
        . . . . . . 3 3 . . . . . . . . 
        . . . . . . . . 3 3 3 3 3 3 . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `,
    img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . 2 2 2 . . . . . 
        . . . 2 2 2 2 2 . . . . . . . . 
        . . 2 . . . . . . . . . . . . . 
        . . 2 2 2 2 2 2 2 2 2 2 2 . . . 
        . . . . . . . . . . . 2 2 . . . 
        . . . . 2 2 2 2 2 2 2 2 . . . . 
        . . . 2 2 . . . . . . . . . . . 
        . . . 2 2 . . . . . . . . . . . 
        . . . . 2 2 2 2 2 2 . . . . . . 
        . . . . . . . . . 2 . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `,
    img`
        . . . . . . . . . . . . . . . . 
        . . . . b b b b b b b b b b . . 
        . . . b . . . . . . . . . . . . 
        . . . b . . . . . . . . . . . . 
        . . . b b . . . . . . . . . . . 
        . . . . . b b b b b b b . . . . 
        . . . . . . . . . . . . b . . . 
        . . . . . . . . . . . . b . . . 
        . . . . . . . b b b b b . . . . 
        . . . . b b b . . . . . . . . . 
        . . b b . . . . . . . . . . . . 
        . . b . . . . . . . . . . . . . 
        . . b b b . . . . . . . . . . . 
        . . . . b b b b b b . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `,
    img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . 8 . . . . . 8 8 8 . . . 
        . . . . 8 . . . . . 8 . . . . . 
        . 8 . . 8 . . . . 8 . . . . . . 
        8 . . 8 8 . . . 8 8 . . . . . . 
        8 . . 8 . . . . 8 . . . . . . . 
        8 . . 8 . . . . 8 . . . . . . . 
        8 . . 8 . . . . . . . . . . . 8 
        8 . . . . . . . . . . . . . 8 . 
        8 8 . . . . . . . . . . . 8 8 . 
        . 8 8 . . . . . . . . . 8 8 . . 
        . . . 8 8 8 . . . . 8 8 . . . . 
        . . . . . 8 8 8 8 8 8 . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `,
    img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . 6 6 . . . . . . . . . . . 
        . . . . . 6 6 6 6 6 . . . . . . 
        . . . . . . . . . 6 . . . . . . 
        . . . . . . . 6 6 6 . . . . . . 
        . . . . 6 6 6 . . . . . . . . . 
        . . . 6 6 . . . . . . . . . . . 
        . . . 6 . . . . . . . . . . . . 
        . . . 6 . . . . . . . . . . . . 
        . . . 6 . . . . . . . . . . . . 
        . . . . 6 6 6 6 6 . . . . . . . 
        . . . . . . . . 6 6 6 6 . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `,
    img`
        . . . . . . . . . . . . . . . . 
        . . . . . a a a a a a a a . . . 
        . . . . a a a a a . . . . . . . 
        . . . a a a . . . a a a . . . . 
        . . a . a . . . . . . . a . . . 
        . . a . a . . . . . . . a . . . 
        . . a a a a . . . . . a a . . . 
        . . . a a a a a a a a . . . . . 
        . a a . . . . a . a a . . . . . 
        a . . . . . . . a a a a . . . . 
        a . . . . . . . . . a a . . . . 
        a a . . . . . . . a a . a a . . 
        . a a a a a a a a . . . . a . . 
        . . . . . . . . a a a a a a . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `,
    img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . d . . . . 
        . . . . . . . . . d d d . . . . 
        . . . . . . . . d d . . . . . . 
        . . . . . . . d d d d d d d d d 
        . . . . . d d d . . . . . . . . 
        . . . . d . d . . . . . . . . . 
        . . . d d . d . . . . . . . . . 
        . . . d . d . . . . . . . . . . 
        . . . d . d d . . . . . . . . . 
        . . . d . . d d . . . . . . . . 
        . . . . d d d d . . . . . . . . 
        . . . . . . . d . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `,
    img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . f f . . . . . 
        . . . . . . . . . . f . . . . . 
        . . . . . . . f f f f f f f f f 
        . . . . f f f f f . . . . . . f 
        . . . f . f f . f . . . . . . f 
        . . . . f f . . . f . . . . f . 
        . . . . f f . . . f . . . . f . 
        . . . f f f . . . f . . . f . . 
        . . . f f f . . f f . . f . . . 
        . . . f f f f f f f f f . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `
    ]
    if (numEnemyLevel <= 3) {
        for (let index = 0; index < 6; index++) {
            enemyList.shift()
        }
        for (let index = 0; index < 30; index++) {
            projectile = sprites.createProjectileFromSide(enemyList._pickRandom(), 0, 60)
            projectile.setKind(SpriteKind.simpleEnemy)
            projectile.setFlag(SpriteFlag.GhostThroughWalls, true)
            tiles.placeOnTile(projectile, tiles.getTileLocation(randint(0, 29), randint(0, 140)))
        }
    } else if (numEnemyLevel <= 8) {
        for (let index = 0; index < 4; index++) {
            enemyList.shift()
        }
        for (let index = 0; index < 60; index++) {
            projectile = sprites.createProjectileFromSide(enemyList._pickRandom(), 0, 60)
            projectile.setKind(SpriteKind.mediumEnemy)
            projectile.setFlag(SpriteFlag.GhostThroughWalls, true)
            tiles.placeOnTile(projectile, tiles.getTileLocation(randint(0, 29), randint(0, 140)))
        }
    } else {
        for (let index = 0; index < 80; index++) {
            projectile = sprites.createProjectileFromSide(enemyList._pickRandom(), 0, 60)
            projectile.setKind(SpriteKind.hardestEnemy)
            projectile.setFlag(SpriteFlag.GhostThroughWalls, true)
            tiles.placeOnTile(projectile, tiles.getTileLocation(randint(0, 29), randint(0, 140)))
        }
    }
}
scene.onHitWall(SpriteKind.Player, function (sprite, location) {
    if (!(GreenApple.isHittingTile(CollisionDirection.Top))) {
        jumpCount = 0
    }
    if (GreenApple.isHittingTile(CollisionDirection.Left) || GreenApple.isHittingTile(CollisionDirection.Right)) {
        GreenApple.vy = 0
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (jumpCount < 2) {
        jumpCount += 1
        GreenApple.vy = -150
        animation.runImageAnimation(
        GreenApple,
        [img`
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
            `,img`
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
            `,img`
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
            `],
        100,
        false
        )
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava0, function (sprite, location) {
    if (controller.up.isPressed()) {
        GreenApple.vy = -50
    } else {
        GreenApple.vy = 50
    }
    timer.throttle("action", 1000, function () {
        info.changeLifeBy(-1)
    })
})
function SpawnInBoss () {
    if (GreenApple.tileKindAt(TileDirection.Bottom, sprites.builtin.oceanSand14)) {
        finalBoss = sprites.create(assets.image`archnemesis`, SpriteKind.biggestBaddestEnemy)
        finalBoss.setVelocity(0, 20)
        finalBoss.setFlag(SpriteFlag.GhostThroughWalls, false)
        tiles.placeOnTile(finalBoss, tiles.getTileLocation(3, 14))
    }
}
function lavaRisingLevel (numLavaLevel: number) {
    if (numLavaLevel <= 3) {
        lavaBlock += 1
        for (let index = 0; index <= 30; index++) {
            tiles.setTileAt(tiles.getTileLocation(index, lavaBlock * -1 + 154), sprites.dungeon.hazardLava0)
            tiles.setWallAt(tiles.getTileLocation(index, lavaBlock * -1 + 154), false)
        }
    } else if (numLavaLevel <= 8) {
        lavaBlock += 5
        for (let index = 0; index <= 30; index++) {
            tiles.setTileAt(tiles.getTileLocation(index, lavaBlock * -1 + 154), sprites.dungeon.hazardLava0)
            tiles.setWallAt(tiles.getTileLocation(index, lavaBlock * -1 + 154), false)
        }
    } else {
        lavaBlock += 10
        for (let index = 0; index <= 30; index++) {
            tiles.setTileAt(tiles.getTileLocation(index, lavaBlock * -1 + 154), sprites.dungeon.hazardLava0)
            tiles.setWallAt(tiles.getTileLocation(index, lavaBlock * -1 + 154), false)
        }
    }
}
let lavaBlock = 0
let finalBoss: Sprite = null
let projectile: Sprite = null
let enemyList: Image[] = []
let jumpCount = 0
let GreenApple: Sprite = null
scene.setBackgroundImage(img`
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
    `)
tiles.setCurrentTilemap(tilemap`level1`)
lavaRisingLevel(game.askForNumber("Lava Difficulty Level (0-easiest/9-hardest)", 1))
enemyLevel(game.askForNumber("Enemy Difficulty Level (0-easiest/9-hardest)", 1))
GreenApple = sprites.create(assets.image`myImage`, SpriteKind.Player)
tiles.placeOnTile(GreenApple, tiles.getTileLocation(26, 134))
controller.moveSprite(GreenApple, 100, 0)
GreenApple.ay = 300
GreenApple.setStayInScreen(true)
scene.cameraFollowSprite(GreenApple)
jumpCount = 0
info.setLife(20)
game.onUpdateInterval(2000, function () {
    enemyLevel(1)
})
game.onUpdateInterval(1000, function () {
    lavaRisingLevel(1)
})
