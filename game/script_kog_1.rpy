define sjp = Character('서재필', color="#FFD9FA")
define hys = Character('홍영식', color="#FFD9FA")

label script_kog_1:
    show black
    $ renpy.pause(1.0, hard=True)
    centered "1부. 여명(黎明)의 경계" with fade
    $ renpy.pause(1.0, hard=True)
    hide black

    # 새벽녘
    ## 메모: 새벽 시간대로 사진 보정하기

    scene kog_house
    $ renpy.pause(1.0, hard=True)

    show black with fade
    sjp "이완이 출국했습니다."
    hys "이때를 놓치면, 언제 다시 기회가 올지 모릅니다."
    jy "……결단을 내려야 하네."
    hide black with fade

    "달빛이 창을 때려 산산이 부서진다."
    "옥균은 새벽에 책을 읽고 있다."

    return