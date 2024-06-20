define test = Character('테스트', color="#FFD9FA")


label script_test:
    scene black

    show jh shirt_hurt_left at right
    show kog shirt_right at left

    kog "자네가 먼저 두시게."
    jh "…예, 알겠습니다."

    show screen baduk

    jh "……."

    hide screen baduk

    # show jh jacket_soft
    # jh "jh jacket_soft"
    # test "next"
    # hide jh jacket_soft

    # show jh jacket_right
    # jh "jh jacket_right"
    # test "next"
    # hide jh jacket_right

    # show jh jacket_right_smile
    # jh "jh jacket_right_smile"
    # test "next"
    # hide jh jacket_smile
    
    return