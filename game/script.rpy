# 게임 스크립트
default preferences.text_cps = 30

# 이미지 정의
image black = "bg image/bg_black.png"
image white = "bg image/bg_white.png"

image deck = "bg image/bg_deck.jpg"
image hallway = "bg image/bg_hallway.jpg"
image harbor = "bg image/보정/bg_harbor.png"
image hjh_house = "bg image/bg_hjh_house.png"
image hotel = "bg image/bg_hotel.jpg"
image kog_house = "bg image/bg_kog_house.png"
image library = "bg image/bg_library.jpg"
image nightsea = "bg image/bg_nightsea.jpg"
image palaceis = "bg image/bg_palaceis.jpg"
image palaceos = "bg image/보정/bg_palaceos.png"
image river = "bg image/bg_river.jpg"
image sea = "bg image/보정/bg_sea.png"
image street = "bg image/보정/bg_street.png"
image tatami = "bg image/bg_tatami.jpg"


#메인 캐릭터
define narrator = Character(None, what_color="#e6e6e6")

define jh = Character('정훈', color="#a0a0a0", image="jh")
define hjh = Character('한정훈', color="#ffffff")
define kog = Character('김옥균', color="#ffffff", image="kog")
define jy = Character('종윤', color="#5587ED")
define emp = Character('이희', color="#F6F6F6")
define umm = Character('엄 상궁', color="#23A41A")
define iw = Character('이완', color="#740000")
define iy = Character('이연', color="#38610B")
define soph = Character('소피', color="#143d8e")
define wada = Character('와다', color="#9cf89f")
define hsg = Character('홍승규', color="#FF7171")
define hjw = Character('홍종우', color="#ff3434")
define hjw_q = Character('홍종우?', color="#a0a0a0", image="hjw_q")


# 캐릭터 이미지 정의
layeredimage jh :
    attribute inner
    attribute outer default

layeredimage kog :
    attribute inner
    attribute outer default


image jh = im.FactorScale("Character Standing/범정훈2.png", 0.75)
image kog = im.FactorScale("Character Standing/웅옥2.png", 0.75)


# 정훈
image jh inner = ConditionSwitch(
    "_last_say_who == 'jh'", im.FactorScale("Character Standing/범정훈1.png", 0.78),
    "not _last_say_who == 'jh'", im.Grayscale(im.FactorScale("Character Standing/범정훈1.png", 0.75))
)
image jh innerLeft = ConditionSwitch(
    "_last_say_who == 'jh'", im.FactorScale("Character Standing/범정훈1.png", 0.78),
    "not _last_say_who == 'jh'", im.Grayscale(im.FactorScale("Character Standing/범정훈1.png", 0.75))
)
image jh innerRight = ConditionSwitch(
    "_last_say_who == 'jh'", im.FactorScale(im.Flip("Character Standing/범정훈1.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/범정훈1.png", horizontal=True), 0.75))
)

image jh outer = ConditionSwitch(
    "_last_say_who == 'jh'", im.FactorScale("Character Standing/범정훈2.png", 0.78),
    "not _last_say_who == 'jh'", im.Grayscale(im.FactorScale("Character Standing/범정훈2.png", 0.75))
)
image jh outerLeft = ConditionSwitch(
    "_last_say_who == 'jh'", im.FactorScale("Character Standing/범정훈2.png", 0.78),
    "not _last_say_who == 'jh'", im.Grayscale(im.FactorScale("Character Standing/범정훈2.png", 0.75))
)
image jh outerRight = ConditionSwitch(
    "_last_say_who == 'jh'", im.FactorScale(im.Flip("Character Standing/범정훈2.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/범정훈2.png", horizontal=True), 0.75))
)

image jh innerColor = im.FactorScale("Character Standing/범정훈1.png", 0.75)
image jh innerGray = im.Grayscale(im.FactorScale("Character Standing/범정훈1.png", 0.75))

image jh innerLeftColor = im.FactorScale("Character Standing/범정훈1.png", 0.75)
image jh innerLeftGray = im.Grayscale(im.FactorScale("Character Standing/범정훈1.png", 0.75))

image jh innerRightColor = im.FactorScale(im.Flip("Character Standing/범정훈1.png", horizontal=True), 0.75)
image jh innerRightGray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/범정훈1.png", horizontal=True), 0.75))

image jh outerColor = im.FactorScale("Character Standing/범정훈2.png", 0.75)
image jh outerGray = im.Grayscale(im.FactorScale("Character Standing/범정훈2.png", 0.75))

image jh outerLeftColor = im.FactorScale("Character Standing/범정훈2.png", 0.75)
image jh outerLeftGray = im.Grayscale(im.FactorScale("Character Standing/범정훈2.png", 0.75))

image jh outerRightColor = im.FactorScale(im.Flip("Character Standing/범정훈2.png", horizontal=True), 0.75)
image jh outerRightGray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/범정훈2.png", horizontal=True), 0.75))


# 홍종우?
image hjw_q inner = ConditionSwitch(
    "_last_say_who == 'hjw_q'", im.FactorScale("Character Standing/범정훈1.png", 0.78),
    "not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/범정훈1.png", 0.75))
)
image hjw_q innerLeft = ConditionSwitch(
    "_last_say_who == 'hjw_q'", im.FactorScale("Character Standing/범정훈1.png", 0.78),
    "not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/범정훈1.png", 0.75))
)
image hjw_q innerRight = ConditionSwitch(
    "_last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/범정훈1.png", horizontal=True), 0.78),
    "not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/범정훈1.png", horizontal=True), 0.75))
)

image hjw_q outer = ConditionSwitch(
    "_last_say_who == 'hjw_q'", im.FactorScale("Character Standing/범정훈2.png", 0.78),
    "not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/범정훈2.png", 0.75))
)
image hjw_q outerLeft = ConditionSwitch(
    "_last_say_who == 'hjw_q'", im.FactorScale("Character Standing/범정훈2.png", 0.78),
    "not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/범정훈2.png", 0.75))
)
image hjw_q outerRight = ConditionSwitch(
    "_last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/범정훈2.png", horizontal=True), 0.78),
    "not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/범정훈2.png", horizontal=True), 0.75))
)

image jh innerColor = im.FactorScale("Character Standing/범정훈1.png", 0.75)
image jh innerGray = im.Grayscale(im.FactorScale("Character Standing/범정훈1.png", 0.75))

image jh innerLeftColor = im.FactorScale("Character Standing/범정훈1.png", 0.75)
image jh innerLeftGray = im.Grayscale(im.FactorScale("Character Standing/범정훈1.png", 0.75))

image jh innerRightColor = im.FactorScale(im.Flip("Character Standing/범정훈1.png", horizontal=True), 0.75)
image jh innerRightGray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/범정훈1.png", horizontal=True), 0.75))

image jh outerColor = im.FactorScale("Character Standing/범정훈2.png", 0.75)
image jh outerGray = im.Grayscale(im.FactorScale("Character Standing/범정훈2.png", 0.75))

image jh outerLeftColor = im.FactorScale("Character Standing/범정훈2.png", 0.75)
image jh outerLeftGray = im.Grayscale(im.FactorScale("Character Standing/범정훈2.png", 0.75))

image jh outerRightColor = im.FactorScale(im.Flip("Character Standing/범정훈2.png", horizontal=True), 0.75)
image jh outerRightGray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/범정훈2.png", horizontal=True), 0.75))


# 옥균
image kog inner = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/웅옥1.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/웅옥1.png", 0.75))
)
image kog innerLeft = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/웅옥1.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/웅옥1.png", 0.75))
)
image kog innerRight = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("Character Standing/웅옥1.png", horizontal=True), 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/웅옥1.png", horizontal=True), 0.75))
)

image kog outer = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/웅옥2.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/웅옥2.png", 0.75))
)
image kog outerLeft = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/웅옥2.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/웅옥2.png", 0.75))
)
image kog outerRight = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("Character Standing/웅옥2.png", horizontal=True), 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/웅옥2.png", horizontal=True), 0.75))
)


image kog innerColor = im.FactorScale("Character Standing/웅옥1.png", 0.75)
image kog innerGray = im.Grayscale(im.FactorScale("Character Standing/웅옥1.png", 0.75))

image kog innerLeftColor = im.FactorScale("Character Standing/웅옥1.png", 0.75)
image kog innerLeftGray = im.Grayscale(im.FactorScale("Character Standing/웅옥1.png", 0.75))

image kog innerRightColor = im.FactorScale(im.Flip("Character Standing/웅옥1.png", horizontal=True), 0.75)
image kog innerRightGray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/웅옥1.png", horizontal=True), 0.75))

image kog outerColor = im.FactorScale("Character Standing/웅옥2.png", 0.75)
image kog outerGray = im.Grayscale(im.FactorScale("Character Standing/웅옥2.png", 0.75))

image kog outerLeftColor = im.FactorScale("Character Standing/웅옥2.png", 0.75)
image kog outerLeftGray = im.Grayscale(im.FactorScale("Character Standing/웅옥2.png", 0.75))

image kog outerRightcolor = im.FactorScale(im.Flip("Character Standing/웅옥2.png", horizontal=True), 0.75)
image kog outerRightGray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/웅옥2.png", horizontal=True), 0.75))


# 색 설정
define highlight = "#FF8C00"

# 자간 설정
init -2:
    style nvl_dialogue:
        line_spacing 10
    style say_dialogue:
        line_spacing 10 

# 변수
default jh_selected = 0
default kog_selected = 0

# 파이썬 구문
init python:
    pass

# 되감기 취소
define config.hard_rollback_limit = 0

screen remove_rollback():
    key "K_PAGEUP" action NullAction
    # key "'repeat_K_PAGEUP'" action NullAction
    key "K_AC_BACK" action NullAction
    key "mousedown_4" action NullAction
    key "joy_rollback" action NullAction

# 지속데이터 정의
default persistent.jh_selected = False
default persistent.kog_selected = False
default persistent.ep1 = True
default persistent.ep2 = False
default persistent.ep3 = False
default persistent.ep4 = False
default persistent.ep5 = False
default persistent.ep6 = False

# 게임 시작
label start:
    show screen remove_rollback()

    jump intro
    return

# Intro
label intro:
    $ renpy.pause(2.0, hard=True)
    
    # Intro
    # $ renpy.pause(1.0, hard=True)
    # show text "‘Original: Musical Gone Tomorrow’" with fade
    # $ renpy.pause(1.0, hard=True)
    # show text "‘제작 - 삼호선 까마하드’" with fade
    # $ renpy.pause(1.0, hard=True)
    # show text "‘SHOOT TOMORROW’" with fade
    # $ renpy.pause(1.0, hard=True)
    # show text "‘끝은 새로운 시작이니, 누군가는 그 길을 가야 한다’" with fade
    # $ renpy.pause(1.0, hard=True)
    # hide text with fade

    #### TEST ####
    
    #### TEST ####


    jump script_opening
    return
