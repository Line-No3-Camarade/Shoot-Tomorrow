image rock_black = im.Scale("baduk/rock_black.png", 30, 30)
image rock_white = im.Scale("baduk/rock_white.png", 30, 30)
image rock_transparent = im.Scale("baduk/rock_transparent.png", 30, 30)

default count = 0

init python:
    count = 0

    rows = 19
    cols = 19

    baduk_board = []
    button_states = []

    baudk_width = 800
    baudk_height = 800

    square_width = 22
    square_height = 22

    zero_x = 24
    zero_y = 24
    
    def init_board():    
        for i in range(rows):
            row = []
            state_row = []
            for j in range(cols):
                x = zero_x + i*square_width
                y = zero_y + j*square_height
                row.append((x, y))
                state_row.append(False)
            baduk_board.append(row)
            button_states.append(state_row)


    def clear_states():
        for i in range(rows):
            for j in range(cols):
                button_states[i][j] = False
    

    def count_exit():
        global count
        count += 1

        if count == 2:
            clear_states()
        

    def ToggleButton(i, j):
        button_states[i][j] = not button_states[i][j]

    init_board()


screen baduk():
    modal True
    frame:
        xsize 850
        ysize 850

        xpadding 50
        ypadding 50
        
        xalign 0.5
        yalign 0.5
        
        add "baduk/board.png":
            xsize 800
            fit "contain"
            xalign 0.5
            yalign 0.5
        
        vbox:
            xsize 800
            ysize 800
            xalign 0.5
            yalign 0.5

            vbox:
                xsize 800-20
                ysize 800-20
                xalign 0.5
                yalign 0.5

                grid 19 19:
                    spacing 12
                    
                    for i in range(rows):
                        for j in range(cols):
                            $ button_id = "{}_{}".format(i, j)

                            imagebutton:
                                xsize 30
                                ysize 30
                                xalign 0.5
                                yalign 0.5

                                id button_id

                                if button_states[i][j]:
                                    idle "rock_white"
                                else:
                                    idle "rock_transparent"
                                
                                action Function(ToggleButton, i, j)

                                if i == 0 and j == 0:
                                    idle "rock_black"
                                    action [SetVariable("co", (i, j)), Function(count_exit), Return()]

                                
                                # if renpy.get_screen("baduk").get(button_id).button_state:
                                #     idle "rock_white"
                                # else:
                                #     idle "rock_transparent"

                                # action ToggleButton(button_id)

                                # if i % 2 == 0:
                                #     if j % 2 == 0:
                                #         idle "rock_transparent" if imagebutton.id else "rock_white"
                                #     else:
                                #         idle "rock_transparent" if button_state else "rock_black"
                                # else:
                                #     if j % 2 == 0:
                                #         idle "rock_transparent" if button_state else "rock_white"
                                #     else:
                                #         idle "rock_transparent" if button_state else "rock_black"
                                
                                # action [SetVariable("co", (i, j)), Return()]

    