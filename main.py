def pulsador_a():
    basic.show_string("Brayan Cardoso")

def pulsador_b():
    basic.show_string("mi edad es 16 ")

input.on_button_pressed(Button.A, pulsador_a)
input.on_button_pressed(Button.B, pulsador_b)
   
