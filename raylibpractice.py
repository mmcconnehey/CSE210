from pyray import *
init_window(800, 450, 'Hello')
while not window_should_close():
    begin_drawing()
    clear_background(BLACK)
    draw_text('Hello World ', 190, 200, 20, WHITE)
    end_drawing()
close_window()