define test = Character('테스트', color="#FFD9FA")
define mimi = Character('미니정훈', color="#a0a0a0", image="jh")


label script_test:
    scene black

    show jh
    jh "default"
    test "next"

    jh jacket_smile_right "jacket_smile"
    test "next"

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