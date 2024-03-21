label script_opening:

    scene tatami
    "창호 바른 미닫이문이 양옆으로 열리며 때늦은 햇살이 쏟아져 들어왔다."
    "소매 걷은 팔 위로 온기와 서늘한 바람이 겹쳤다."

    show hjw_q innerLeft at right
    show kog innerRight at left

    "옥균은 빠르지 않은 걸음으로 방에 들어섰다."
    "홍종우라는 청년과 눈이 마주친다."
    "닿은 시선이 서로 떨어지지 않는다."
    "홍종우가 앞으로 나서서 옥균에게 {color=#F53D3D}서찰{/color}을 건넸다."

    hjw_q "선생께 긴히 전해드릴 것이 있어 왔습니다. 청국대신 이홍장의 밀서입니다."
    kog "…이홍장?"

    "옥균은 서찰을 받아 펼쳤다."
    "안에는 {color=#F53D3D}익숙한 필체{/color}로 간결한 전언이 적혀 있었다."

    show black
    centered "‘김옥균, 군과 더불어 어깨를 잡고 의논하여 동양 백년의 대계를 정하고자 한다.’" with fade
    centered "‘청국으로 오라, 이홍장.’"
    hide black

    hjw_q "현재 청과 일본은 조선을 사이에 두고 서로 세력을 과시하고 있습니다."
    hjw_q "최근 이완이 청을 배신하고 일본 정부와 접촉하고 있는 바, 청의 이홍장은 선생과 뜻을 함께 하고 싶어합니다."
    hjw_q "선생께서도 이홍장을 이용해, 조선으로 복귀하시는 편이 더 안전할 것입니다."

    "옥균은 서찰을 도로 접으며 그를 향해 가볍게 고개를 돌렸다."
    "꿰뚫을 것 같은 눈빛이 청년을 향했다."
    "옥균은 천천히 홍종우에게 다가가며 헛웃음을 흘렸다."

    kog "…홍종우?"
    "홍종우는 자세를 고쳐 잡으며 대답했다."
    hjw_q "…예, 선생님."
    "{color=#F53D3D}천지天地의 명운{/color}을 바꾼 만남이었다."

    scene black with fade
    show jh innerLeft at right
    show kog innerRight at left

    "캐릭터를 선택해 인생을 살아 보세요."
    "한 캐릭터 이야기의 끝을 확인하기 전까지 다른 캐릭터의 삶은 확인할 수 없습니다."


    menu:
        "김옥균":
            hide jh
            show kog innerRightColor at center
            "김옥균을 선택하셨습니다."
            $ kog_selected = 1
            $ jh_selected = 0
            $ persistent.kog_selected = True
            $ persistent.jh_selected = False
            "계속하시겠습니까?"
        
        "한정훈":
            hide kog
            show jh innerLeftColor at center
            "한정훈을 선택하셨습니다."
            $ jh_selected = 1
            $ kog_selected = 0
            $ persistent.jh_selected = True
            $ persistent.kog_selected = False
            "계속하시겠습니까?"


