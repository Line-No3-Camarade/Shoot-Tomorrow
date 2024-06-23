image choice = im.Scale("baduk/choice_test.png", 200, 150)
image choice_1 = im.Scale("baduk/choice1_test.png", 200, 150)

default co = None

# init python:
#     def clear_states():
#         for i in range(rows):
#             for j in range(cols):
#                 button_states[i][j] = False
    
#     def save_states():
#         num = 0
#         with open("D:/GitHub/Shoot-Tomorrow/game" + "/" + "baduk_board.txt", "w") as f:
#             for i in range(rows):
#                 for j in range(cols):
#                     if button_states[i][j]:
#                         f.write(str(num) + ": (" + str(i) + ", " + str(j) + ")")
#                         num += 1
#             f.close()

        

label script_test_baduk:
    scene black

    show jh_left shirt_hurt at right
    show kog_right shirt at left
    
    jump round1

label round1:
    kog "자네가 먼저 두게."
    jh "…예, 알겠습니다."

    "바둑알을 선택해 주세요."

    show screen baduk

    # $ choice_flag = 1
    # menu:
    #     "진행하기":
    #         pass
    # $ choice_flag = 0

    $ choice_flag = 2
    menu:
        "1. {image=choice_1}":
            hide screen baduk
            hide kog_right 
            show jh_left at center
            jh "찬란한 세상이라도 보고자 하였습니다."
        "2. {image=choice}":
            hide screen baduk
            hide kog_right 
            show jh_left at center
            jh "2번을 고르겠습니다."
        "3. {image=choice}":
            hide screen baduk
            hide kog_right 
            show jh_left at center
            jh "3번을 고르겠습니다."
    $ choice_flag = 0


    jump round2


label round2:
    scene black

    show jh_left shirt_hurt at right
    show kog_right shirt at left

    kog "계속하지."
    jh "…예."
    call screen baduk

    "게임이 끝났습니다."

    return

