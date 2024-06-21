image rock_black = im.Scale("baduk/rock_black.png", 30, 30)
image rock_white = im.Scale("baduk/rock_white.png", 30, 30)


init python:
    rows = 19
    cols = 19

    baduk_board = []

    baudk_width = 800
    baudk_height = 800

    square_width = 22
    square_height = 22

    zero_x = 24
    zero_y = 24

    for i in range(rows):
        row = []
        for j in range(cols):
            x = zero_x + i*square_width
            y = zero_y + j*square_height
            row.append((x, y))
        baduk_board.append(row)






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
                            imagebutton:
                                xsize 30
                                ysize 30
                                xalign 0.5
                                yalign 0.5

                                if i % 2 == 0:
                                    if j % 2 == 0:
                                        idle "rock_white"
                                    else:
                                        idle "rock_black"
                                else:
                                    if j % 2 == 0:
                                        idle "rock_black"
                                    else:
                                        idle "rock_white"
                                
                                action [SetVariable("co", (i, j)), Return()]

    