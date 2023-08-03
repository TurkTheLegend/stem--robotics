def on_button_pressed_a():
    global step
    step = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global step
    step += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

step = 0
step = 0

def on_forever():
    basic.show_number(step)
basic.forever(on_forever)
