


label test:
    show jh innerLeft at right
    show kog innerRight at left

    "캐릭터를 골라주세요."

    menu:
        "한정훈":
            hide kog
            show jh innerLeftColor at center
            "한정훈을 선택하셨습니다."
            $ jh_selected = 1
            $ kog_selected = 0
            $ persistent.jh_selected = True
            $ persistent.kog_selected = False
            "계속하시겠습니까?"
        "김옥균":
            hide jh
            show kog innerRightColor at center
            "김옥균을 선택하셨습니다."
            $ kog_selected = 1
            $ jh_selected = 0
            $ persistent.kog_selected = True
            $ persistent.jh_selected = False
            "계속하시겠습니까?"