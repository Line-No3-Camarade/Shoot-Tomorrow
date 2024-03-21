# 엑스트라
define psg1 = Character('승객1', color="#FFD9FA", who_outlines=[(0.3, "#000000")])
define psg2 = Character('승객2', color="#FFD9FA", who_outlines=[(0.3, "#000000")])
define hjw2 = Character('???', color="#ff3434", who_outlines=[(0.3, "#000000")])

# define  = Character('', color="#FFD9FA", who_outlines=[(0.3, "#000000")])

label script_ep1:
    # Intro
    $ renpy.pause(1.0, hard=True)
    show text "‘Original: Musical Gone Tomorrow’" with fade
    $ renpy.pause(1.0, hard=True)
    show text "‘제작 - 삼호선 까마하드’" with fade
    $ renpy.pause(1.0, hard=True)
    show text "‘SHOOT TOMORROW’" with fade
    $ renpy.pause(1.0, hard=True)
    show text "‘끝은 새로운 시작이니, 누군가는 그 길을 가야 한다’" with fade
    $ renpy.pause(1.0, hard=True)
    hide text with fade

    "옷깃 스치는 소리도 선명할 만큼 깊은 정적이 흘렀다."

    $ renpy.pause(0.2, hard=True)
    play sound "audio/Handling.mp3"
    $ renpy.pause(1.0, hard=True)

    scene library with fade
    "정훈은 허리춤에 숨겨두었던 총신을 잡아 꺼냈다."
    "쇠붙이를 붙든 손에 차마 훔쳐내지 못한 식은땀이 흐른다."
    "정훈은 방아쇠에 검지를 올렸다."
    "옥균은 그제야 활자에서 눈을 떼어 고개를 들었다."

    show jh innerLeft at right
    show kog innerRight at left

    jh "……."
    kog "……곰곰이 생각해보았네."
    jh "……."
    kog "자네와 내가 이룩할 수 있는 새로운 세상에 관해서."
    jh "……새로운 세상."
    
    "정훈은 저도 모르게 그의 말을 되풀이했다."
    
    show black
    centered "‘새로운 세상으로 가고 싶다.’" with fade
    centered "‘그 나라로, 가고 싶다.’"
    centered "하지만 당신은, 어쩌면 나 역시 갈 수 없는 나라다."
    "그런데도 만들 수 있단 말인가."
    "정훈은 심장이 저릿해지는 감각을 느꼈다."
    hide black

    kog "해서, 내 물음에 답해주었으면 하네."
    jh "……그게 무엇입니까."
    kog "대단한 건 아닐세. 말 몇 마디 궁금할 뿐이야."
    kog "자네는 전부 알고 있을 거야."
    
    "정훈은 총을 고쳐 잡으며 다음 말을 기다렸다."

    kog "불란서 말로 희망이 무엇인가."
    jh "……."
    kog "희망이, 무엇인가."
    jh "……Désir."
    kog "혁명은 무엇인가."
    jh "Révolution."
    kog "그럼, 동지는 무엇인가."

    "이건 시험이다."
    
    show black
    centered "잔인하고 명료한 시험." with fade
    hide black

    menu:
        "총을 쏜다.":
            hide jh
            hide kog
            show black
            $ renpy.pause(1.0, hard=True)
            play sound "audio/Gunfire.mp3"
            $ renpy.pause(2.0, hard=True)
            stop sound

        "총을 내린다.":
            hide jh
            hide kog
            show black
            "정훈은 그만 눈을 감으며 총구를 거두었다."
            "자리에서 일어난 옥균이 다가왔다."
            "그는 미소를 띠고 말했다."
            hide black
            show kog outerRight at center
            kog "그래. 가자, 청국으로."
            show black
            $ renpy.pause(1.0, hard=True)

    # 01. 귀환
    scene black
    centered "1893년 12월, 조선."

    "갑판에 섰다."
    scene nightsea with fade
    show jh at center
    # 파도 소리
    "차디찬 바닷바람이 숨통을 조이듯 밀려든다."
    "하늘이 낮고 짙게 깔려 수평선조차 보이지 않는다."
    "남몰래 지은 한숨이 싸늘한 공기 위로 겨우 흩어졌다."
    "숨조차 숨어서 쉬는 게 습관이 된 탓이다."
    $ renpy.pause(1.5, hard=True)
    "정훈은 육지를 등지고 한참을 서 있었다."
    hide jh

    play sound "audio/Crowd Talking.mp3" volume 0.1 fadein 0.1
    "불빛을 향해 서 있던 승객들의 대화 소리가 들렸다."
    "기모노 차림의 일본 여인 둘이었다."

    show jh outerLeft at center
    psg1 "{color=#ffb980}저기 보이는 게 조선인가?"
    psg2 "{color=#ffb980}그런 것 같네. 오래 걸렸다."
    psg1 "{color=#ffb980}기대된다."
    psg2 "{color=#ffb980}기대하지 마. 동경보다 훨씬 별로라고 했어."
    psg1 "{color=#ffb980}누가?{/color}"
    hide jh
    stop sound fadeout 0.5

    "정훈은 고개를 돌려 의식에서 소리를 지웠다."
    "지금의 조선이 어떤 모습이든, 보지 않고는 알 수 없다."

    show jh outerLeft at center
    jh "……."
    hide jh
    
    "다시는 돌아오지 못할 땅이라고 여겼다."
    "일평생 그리워만 하다 죽겠거니 생각했다."
    "곧 조선 땅을 다시 밟는다."

    show black with dissolve
    centered "'국왕이 속히 알현할 것을 명하다.'"
    
    "짧은 전보 한 장에 만 리 길을 달려왔다."
    "누군가는 어리석은 일이라고 했지만, 모르겠다."
    "조선이 나를 찾는다는 사실이 중요했다."
    "돌아와야 했다."
    "거부할 힘이 없으니까."

    hide black with fade
    show jh at center
    "정훈은 제 심장처럼 일렁이는 파도를 바라보았다."
    
    # 종 소리
    play sound "audio/Ship Bell.mp3"

    "종소리가 울린다."
    "갑판에 있던 승객들이 선실로 돌아갔다."
    "정훈도 그들을 따라 안으로 들어갔다."
    hide jh

    scene hallway with fade
    # Walking Wooden
    play sound "<loop 0>audio/Walking Wooden.mp3"

    "아른거리는 조명이 좁은 복도를 비춘다."
    "걸음마다 마룻바닥이 소리를 냈다."
    "모퉁이 너머 다가오는 그림자가 벽면을 타고 길게 늘어졌다."
    "인영이 느리게 다가온다."
    "신발코가 벽 너머로 모습을 드러냈다."
    stop sound

    show jh innerLeft at center
    "정훈은 본능적으로 걸음을 멈추었다."
    "빛바랜 한복 차림의 남자, 그는 갓을 쓰고 있었다."
    "정훈이 그쪽을 바라보듯 남자도 이쪽을 바라보고 섰다."
    "날카롭게 빛나는 눈과 마주쳤다."

    menu:
        "정훈은……."

        "시선을 피한다.":
            hide jh
            "정훈은 곧 고개를 숙이고 빠르게 걸음을 옮겼다."
            "남자의 시선이 이쪽을 향하는 게 느껴진다."
            "정훈은 곁눈으로 남자의 행색을 살피면서 스쳐 지나갔다."
            "그 순간 느낀 기시감은 뭐였을까."
            "정훈은 생각을 떨어내려 애써야 했다."

        "그를 계속 마주 보았다.":
            hide jh
            "마주하던 남자의 시선이 가슴 언저리로 떨어졌다."
            "남자는 곧 입매를 샐긋하게 기울이더니 말했다."

            show jh innerLeft at center
            hjw2 "불란서에 계셨소?"

            "정훈은 눈을 동그랗게 뜨며 경계하는 눈빛을 아끼지 않았다."

            hjw2 "군번줄. 외인부대의 것이 아니오."
            hide jh

            "정훈은 그제야 자신이 여태 군번줄을 걸고 있었음을 깨달았다."
            "정훈은 손바닥으로 이름을 감추어 쥐었다."

            if not achievement.has("hongjongwoo"):
                $ get_achievement("hongjongwoo")

            show jh innerLeft at center
            hjw "홍종우라고 합니다."
            jh "홍종우……?"

            "홍종우는 돌아오지 않는 대꾸에도 사람 좋은 웃음을 지어 보였다."

            hjw "동포끼리 한 번쯤 마주쳤을 법도 한데, 처음 뵙습니다."
            jh "……있는 곳이 달랐으니까요."
            hide jh

            "홍종우는 양반이었고 문인이었고 유학생이다."
            "그는 양인이었고 군인이었고 이방인이다."
            "물론 홍종우는 그 말의 의미를 알아채지 못한 듯했다."
            "홍종우는 이마를 두어 번 긁더니 손을 내밀고 악수를 청했다."

            show jh innerLeft at center
            hjw "이렇게 만나니 반갑군요."
            hjw "나중에 또 만나면 와인이라도 한잔합시다. 귀향한 사람끼리."

            "정훈은 마지못해 그의 손을 맞잡고 대답했다."

            jh "……그러죠."

            "홍종우는 갓의 양태를 살짝 잡아 인사하곤 복도를 가로질러 갔다."
            hide jh
    
    $ renpy.pause(1.0, hard=True)
    show black with fade
    soph "……정말 떠나는 거야?"

    scene library with fade
    "정훈은 가방을 챙기던 손을 멈추고 소피를 돌아보았다."
    "왜 떠나느냐, 어디로 가느냐 물을 줄 알았는데."
    "소피는 이미 답이 나와 있는 질문만 던질 뿐이었다."
    "정훈이 머뭇거리자 소피는 책장에서 책 한 권을 꺼내어 건넸다."
    "‘Printemps parfume’"
    "조선인 유학생이 번역했다던 그 책이었다."

    soph "이거."
    
    show jh outerLeft at center
    "정훈은 고개를 들어 소피를 바라보았다."

    soph "조선에 돌아가면 사람들한테 이 책, 꼭 보여줘."
    jh "……조선으로 가는 거 어떻게 알았어?"

    "소피는 정훈을 밉지 않게 흘겨보다 옅게 웃었다."

    soph "전보 받은 후로 기분이 좋아 보였거든."
    soph "넌 아닌 척하지만, 다 티나."
    jh "……그렇구나."
    soph "축하해, 훈. 분명 축하할 일 맞지?"

    "정훈은 말없이 소피를 바라보았다."

    soph "먼 길 조심해서 가고 꼭 잘 지내."
    jh "그럴게."
    soph "가서는 많이 웃고 행복해야 해."
    jh "……소피."
    soph "아프지도 말고 다치지도 마."
    jh "그거 너무 어렵다."
    soph "엄청 쉬운 거만 얘기하는 건데."
    hide jh

    "정훈은 작게 소리내어 웃으며 손에 든 책을 물끄러미 보았다."
    "소피는 항상 그의 얼굴을 바라보았다."
    "그 속에서 무엇을 읽었을까."
    "무엇을 읽었기에 슬픈 눈으로 이별을 축복하는 걸까."

    show jh outerLeft at center
    jh "소피."
    soph "응?"
    jh "……그동안 고마웠어."
    hide jh

    "소피는 낯을 기울여 감추고 끄덕이기만 했다."

    show sea with fade

    "정훈은 창틈으로 하늘을 올려다보았다."
    "지금쯤 그곳엔 한낮의 햇살이 내리고 있을 것이다."
    "맑은 하늘 아래의 너는 잘 지내고 있기를."

    $ renpy.pause(1.0, hard=True)

    scene palaceis with fade
    emp "아직이라더냐."

    "이희는 붙박이듯 앉아 눈을 내리깔고 있었다."

    umm "곧 당도할 것입니다. ……가비라도 들일까요."
    emp "되었다. ……입이 쓰구나."

    "이희가 가볍게 손짓하였다."
    "엄 상궁은 머리를 조아리곤 자리에서 물러났다."
    "혼자 남겨진 이희는 창밖으로 시선을 돌렸다."
    "틈으로 스며드는 시린 바람이 이마를 적신다."
    "겨울. 겨울인가 보다."
    "……다시 이 계절이 돌아왔다."

    show black with fade
    centered "‘신 김옥균, 절대 전하를 저버리지 않습니다!’"
    hide black with fade

    "벌써 아홉 해 전 일이다."
    "잊힐 만도 하건만, 여전히 또렷하다."
    "그날의 비명, 광기, 그리고 죽음."
    "이희는 눈을 질끈 감았다."

    emp "……."

    "햇볕이 쓰라리다."
    "비단 아래 거죽까지 타들어 가는 것 같다."
    "입 안이 바싹 마른다."
    "이 빛이 그곳에도 가 닿길."

    show black with fade
    centered "……그대도 반드시 아프길."

    # scene ogasawara with fade
    scene sea with fade
    "비 내리는 바다를 망연히 내다 보았다."
    "옥균은 옷깃이 젖는 줄도 모른 채 북쪽을 바라보고 섰다."
    "그가 기다리는 건 배 따위가 아니었다."
    "항구는 남쪽으로 한참 더 내려가야 있었다."
    "옥균은 비 한 줌이 몰고 올 조선을 기다렸다."
    "그거면, 죽기 전에 받은 소식으로 충분하다고 생각했다."
    "그는 많이 지쳐있었다."
    $ renpy.pause(1.0, hard=True)
    "먼 곳에서부터 바쁜 걸음이 다가왔다."
    "옥균은 돌아보지도 않고 말했다."

    kog "……먼저 들어가라 했는데."

    "와다는 허리춤에 찬 칼을 만지작거리며 조용히 입을 열었다."

    wada "그게, 전보가 왔습니다."

    "옥균은 고개를 돌려 와다를 바라보았다."

    kog "……전보? 누가."
    wada "정부입니다."

    "옥균은 기가 찬 듯이 짧게 웃었다."

    kog "또 어디로. 더 보낼 섬이 있다던가."
    kog "이젠 아예 충승이나 북해도로 보내려고? 차라리 죽이라지……."
    wada "동경에, 돌아오라고……."
    kog "……뭐?"

    "되묻는 옥균의 눈이 동그랗게 커졌다."
    "그의 눈동자에 빛이 스며들었다."
    "와다는 단 한번도 본 적 없는 맹렬한 기세에 한발짝 뒤로 물러섰다."
    "옥균은 그 어느 때보다 빠르게 걸음을 옮겼다."
    "뗀 걸음마다 모래가 깊이 패었다."

    scene black with fade
    $ renpy.pause(1.0, hard=True)
    umm "전하의 명을 받잡고 불란서에서 정훈이란 자가 들었습니다."

    scene palaceis with fade

    emp "들라 하라."

    "문이 열렸다."
    "정훈은 반투명한 장막 뒤에서 빛나는 두 눈을 마주하였다."

    menu:
        "정훈은……."

        "그를 뚫어져라 바라보았다.":
            "이희는 고개를 비스듬히 들어올리고 그 어떤 말도 하지 않았다."
            "먼저 입을 연 것은 엄 상궁이었다."

            umm "용안 앞에 머리를 숙이게."

            "정훈은 그제야 바짝 엎드리고 눈치를 살폈다."
        "급하게 고개를 숙였다.":
            "정훈은 다급히 몸을 숙이고 고개를 바닥에 처박았다."
    
    emp "……정훈."

    "정훈은 눈을 굴리다가 더듬거리며 겨우 대답했다."

    jh "예, ……전하."
    emp "불란서에서 군인으로 지냈다지."

    "정훈은 고개를 슬며시 들어 엄 상궁을 돌아보았다."
    "엄 상궁은 작게 눈짓하였다."

    jh "……그렇습니다."
    emp "허면 홍종우란 자를 아느냐."

    "정훈은 바로 어제, 배 안에서 만났던 사내를 떠올렸다."
    "정훈이 머뭇거리자 엄 상궁이 채근하였다."

    umm "전하께서 하문하시네."

    menu:
        "정훈은 임금의 질문에……."

        "만나본 적이 있다고 대답했다.":
            jh "실은, 그를 만난 적이 있습니다."
            emp "그래? 그럼 그에 대해 잘 알겠구나."
            jh "……감히 잘 안다고는 할 수 없으나, 비범하다 생각했습니다."

        "잘 모른다고 대답했다.":
            jh "실은…… 이름 정도만, 들어보았습니다."
            emp "그래."

            "정훈은 죄라도 지은 사람처럼 고개를 푹 숙이고 일어나지 못했다."

            jh "송구, 합니다."
            emp "상관없다."
    
    "이희는 자리에서 천천히 자리에서 일어났다."
    "정훈은 엄 상궁의 서슬 퍼런 눈빛에 차마 함부로 움직이지 못했다."
    "이희는 얇은 손가락으로 장막을 걷어내고 정훈을 향해 한 발짝 다가섰다."
    "그제야 보다 못한 엄 상궁이 임금 앞에 고개를 숙였다."

    umm "전하."

    "이희는 손짓하며 그를 물리고 정훈의 머리맡에 서서 마른 어깨를 내려다보았다."

    emp "엄아."
    umm "……예, 전하."
    emp "오늘이 며칠이냐."
    umm "12월 6일입니다."
    emp "정훈."

    "정훈은 한참 숨죽이고 엎드려 있다 겨우 시선만 올렸다."

    emp "오늘이 무슨 날인지 아느냐."

    menu:
        "잘 모른다고 대답했다.":
            jh "송구하오나…… 잘 모르겠습니다."
            emp "그래… 모를 수도 있지. 벌써 구 년 전 일이니 말이다."
            jh "……."
            emp "허면 김옥균을 아느냐."
            jh "……알고 있습니다."

        "김옥균이 일본으로 도망간 날이다.":
            jh "갑신년, ……그 일을 이르심입니까?"
            emp "그래. 잘 알고 있구나. 온 나라가 떠들썩했으니."

    "이희는 온몸이 쓰라린 듯한 표정으로 고개를 떨어뜨렸다."
    "이내 입술을 달싹이다가 도로 다물어버렸다."
    "그는 엄 상궁을 바라보며 고개를 끄덕였다."
    "그러자 엄 상궁이 비단 봉투에 싸인 서찰을 머리맡에 내려놓았다."

    emp "……네가 할 일은 간단하지만, 목숨을 걸어야 한다."
    emp "일을 꾸며 속이고 유인하여 결행해야 한다."
    emp "네가 본 것, 들은 것 모두 과인에게만 알리고, 잊어야 한다."
    jh "……제가 할 일이란 게 무엇입니까?"

    "이희는 차갑게 식은 눈으로 허공 어딘가를 응시하였다."
    "마치 그곳에 김옥균이 있는 것처럼."

    emp "홍종우의 이름으로 역적 김옥균에게 접근해라."
    emp "그놈도 홍종우에 대해 이미 알고 있을 테니……."
    emp "암살이 두려워 새 사람을 만나지 않아도 호기심이 생길 것이야."
    emp "그렇게 김옥균에게 접근해서,"
    jh "……."

    $ persistent.ep2 = True
    $ get_epsiode("에피소드 2가 열렸습니다.")

    emp "김옥균을…… 죽여라."
    
    scene black with fade

    jump script_ep2
    return
