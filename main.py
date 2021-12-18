def on_button_pressed_a():
    basic.show_string("I'm a bit sad now look at me :(")
    basic.show_leds("""
        # # . # #
                # # . # #
                . . . . .
                # # # # #
                # . . . #
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_string("Functioning... Error occurred in system function")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_string("Woohoo!")
    basic.show_leds("""
        # # . # #
                # # . # #
                . . . . .
                # . . . #
                # # # # #
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_string("Hello!")
basic.show_string("Epic gamer 1619")
basic.show_string("What will you do?")
basic.show_leds("""
    . # # . .
        # . # . .
        . . # . .
        . . # . .
        # # # # #
""")
basic.show_leds("""
    # # # . .
        # . . . .
        # # # . .
        # . # . .
        # # # . .
""")
basic.show_leds("""
    . # # . .
        # . # . .
        . . # . .
        . . # . .
        # # # # #
""")
basic.show_leds("""
    . # # # #
        . # . . #
        . # # # #
        . . . . #
        . . . . #
""")