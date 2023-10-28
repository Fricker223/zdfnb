chanse = 0
image: Image = None
image2: Image = None
image3: Image = None

def on_button_pressed_a():
    if input.button_is_pressed(Button.A):
        pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_screen_down():
    global chanse
    chanse = randint(1, 3)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_pressed_ab():
    if input.button_is_pressed(Button.AB):
        pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if input.button_is_pressed(Button.B):
        pass
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    global image, image2, image3
    image = images.create_image("""
        . # # . .
        . # . # .
        . # # . .
        . # . # .
        . # . # .
        """)
    image2 = images.create_image("""
        . # # . .
        . # . # .
        . # # . .
        . # . . .
        . # . . .
        """)
    image3 = images.create_image("""
        . . # # .
        . # . . .
        . . # . .
        . . . # .
        . # # . .
        """)
basic.forever(on_forever)

def on_in_background():
    if :
        pass
control.in_background(on_in_background)
