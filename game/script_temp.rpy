# 엑스트라
define psg1 = Character('승객1', color="#FFD9FA", who_outlines=[(0.3, "#000000")])
define psg2 = Character('승객2', color="#FFD9FA", who_outlines=[(0.3, "#000000")])
define hjw2 = Character('???', color="#ff3434", who_outlines=[(0.3, "#000000")])

# define  = Character('', color="#FFD9FA", who_outlines=[(0.3, "#000000")])

label script_temp:
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