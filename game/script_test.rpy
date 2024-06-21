define test = Character('테스트', color="#FFD9FA")

default co = None

init python:
    def clear_states():
        for i in range(rows):
            for j in range(cols):
                button_states[i][j] = False
        

label script_test:
    scene black

    show jh shirt_hurt_left at right
    show kog shirt_right at left
    
    jump round1

label round1:
    kog "자네가 먼저 두게."
    jh "…예, 알겠습니다."

    "바둑알을 선택해 주세요."

    call screen baduk

    if co:
        "선택된 좌표는 [co] 입니다."

    jump round2


label round2:
    kog "계속하지."
    jh "…예."
    call screen baduk

    "게임이 끝났습니다."

    return

