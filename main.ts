input.onButtonPressed(Button.A, function () {
    if (input.buttonIsPressed(Button.A)) {
        chanse = 1
    }
})
input.onGesture(Gesture.SixG, function () {
    chanse = randint(1, 3)
})
input.onButtonPressed(Button.AB, function () {
    if (input.buttonIsPressed(Button.AB)) {
        chanse = 3
    }
})
input.onButtonPressed(Button.B, function () {
    if (input.buttonIsPressed(Button.B)) {
        chanse = 2
    }
})
input.onGesture(Gesture.Shake, function () {
    if (chanse == 1) {
        r.showImage(0)
    } else if (chanse == 2) {
        p.showImage(0)
    } else if (chanse == 3) {
        s.showImage(0)
    }
})
let chanse = 0
let s: Image = null
let p: Image = null
let r: Image = null
r = images.createImage(`
    . # # . .
    . # . # .
    . # # . .
    . # . # .
    . # . # .
    `)
p = images.createImage(`
    . # # . .
    . # . # .
    . # # . .
    . # . . .
    . # . . .
    `)
s = images.createImage(`
    . . # # .
    . # . . .
    . . # . .
    . . . # .
    . # # . .
    `)
