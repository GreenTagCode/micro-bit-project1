input.onButtonPressed(Button.A, function () {
    basic.showString("I'm a bit sad now look at me :(")
    basic.showLeds(`
        # # . # #
        # # . # #
        . . . . .
        # # # # #
        # . . . #
        `)
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("Functioning... Error occurred in system function")
})
input.onButtonPressed(Button.B, function () {
    basic.showString("Woohoo!")
    basic.showLeds(`
        # # . # #
        # # . # #
        . . . . .
        # . . . #
        # # # # #
        `)
})
basic.showString("Hello!")
basic.showString("Epic gamer 1619")
basic.showString("What will you do?")
basic.showLeds(`
    . # # . .
    # . # . .
    . . # . .
    . . # . .
    # # # # #
    `)
basic.showLeds(`
    # # # . .
    # . . . .
    # # # . .
    # . # . .
    # # # . .
    `)
basic.showLeds(`
    . # # . .
    # . # . .
    . . # . .
    . . # . .
    # # # # #
    `)
basic.showLeds(`
    . # # # #
    . # . . #
    . # # # #
    . . . . #
    . . . . #
    `)
