# 지속데이터 정의
default persistent.jh_selected = False
default persistent.kog_selected = False

default in_opening = False


label saving(savable = True):
    if savable:
        python:
            _autosave = True
            _game_menu_scree = "save"
            in_opening = False
    else:
        python:
            _autosave = False
            _game_menu_scree = "preferences"
            in_opening = True
    return


label script_opening:
    default persistent.start = False

    #### 저장 막아 두기 ####
    call saving(False)
    #### 저장 막아 두기 ####

    scene black
    play sound wave fadein 1.0 loop

    "파도치는 소리만이 침묵을 메웠다."
    "높게 매달린 등불과 달무리가 뒤엉켜 갑판을 어스레하게 비춘다."
    "겨눠진 총구에는 흔들림이 없었으나, 총 든 자의 마음은 내내 현기증을 앓았다."
    "저 멀리, 불빛이 아지랑이라도 된 것처럼 흩어졌다."

    show jh_left at right
    show kog_right at left

    jh "개인은, 국가로부터 자유로울 수 없는 겁니까?"
    kog "…그런 사람이 있다면 부럽네."
    jh "내 나라의 현실을 뒤로하고 싶습니다."
    kog "살아서는 힘들지."
    
    scene black
    stop sound fadeout 1.0

    "총구를 목전에 둔 자의 입에서 나온 말은 {color=[highlight]}신탁{/color}과 다르지 않았다."
    "갑판의 집행자는 외려 사형을 언도 받은 사람의 얼굴로 형대 위에 섰다."
    "시간은 무심하게 흐르고,"
    "찰나의 불꽃이 별을 떨어뜨릴 차례였다."

    scene black with fade
    show jh_left at right
    show kog_right at left

    "플레이를 원하는 {color=[highlight]}캐릭터{/color}를 선택해주세요."
    "{color=[highlight]}게임 종료{/color} 혹은 {color=[highlight]}초기화{/color}하기 전까지, 다른 캐릭터의 루트는 확인할 수 없습니다."
    "{color=[highlight]}김옥균{/color}을 선택하시겠습니까? or {color=[highlight]}한정훈{/color}을 선택하시겠습니까?"

    ## 오프닝 선택이 끝나면 지속데이터에 저장 ##
    $ persistent.start = True
    $ persistent.start = False
    ## 오프닝 선택이 끝나면 지속데이터에 저장 ##

    menu:
        "김옥균":
            scene black
            show kog_color_right shirt at center
            
            "{color=[highlight]}김옥균{/color}을 선택하셨습니다."
            
            play sound wave fadein 1.0 loop
            $ kog_selected = 1
            $ jh_selected = 0
            $ persistent.kog_selected = True
            $ persistent.jh_selected = False
            
            "그 짧은 순간, 옥균은 생각했다."
            "땅 위에는 선을 그을 수 있으나, 물 위에는 그러지를 못하는 법."
            "바다는 누구에게도 속하지 않아 이곳이야말로 죽을 자리로구나."
            "이제 드디어 {color=[highlight]}나{/color}를 내려놓을 수 있겠다."

            stop sound fadeout 1.0
            # play sound gun_handling
            # play sound gun_fire
            jump script_kog
        
        "한정훈":
            scene black
            show jh_color_left shirt_hurt at center

            "{color=[highlight]}한정훈{/color}을 선택하셨습니다."
            
            play sound wave fadein 1.0 loop
            $ jh_selected = 1
            $ kog_selected = 0
            $ persistent.jh_selected = True
            $ persistent.kog_selected = False
            
            "그 짧은 순간, 정훈은 생각했다."
            "떠나고 지우고 잊으려 애썼던 시간이 무색하도록 지나온 발자국이 여태 선명하다."
            "아, 나 이제 영영 나아가기만 할 뿐 돌아가지 못하리라."
            "결코 돌아서지 못하리라."

            stop sound fadeout 1.0
            # play sound gun_handling
            # play sound gun_fire
            jump script_hjh
    
    return
