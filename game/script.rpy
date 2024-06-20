#################################################################################################################
### 게임 스크립트 설정 ####
#################################################################################################################
default preferences.text_cps = 30





#################################################################################################################
#### 이미지 정의 ####
#################################################################################################################
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





#################################################################################################################
#### 캐릭터 정의 ####
#################################################################################################################
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
define hjw_q = Character('홍종우?', color="#a0a0a0", image="jh")





#################################################################################################################
#### 캐릭터 이미지 정의 ####
#################################################################################################################
##################
#### 정훈 ####
##################
## base
image jh = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.75))
)
image jh color = im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.75)
image jh gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.75))


### jacket1
## default (hard)
image jh jacket = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.75))
)
image jh jacket_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.75))
)
image jh jacket_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-default1.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-default1.png", horizontal=True), 0.75))
)
image jh jacket_color = im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.75)
image jh jacket_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.75))
image jh jacket_left_color = im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.75)
image jh jacket_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.75))
image jh jacket_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-default1.png", horizontal=True), 0.75)
image jh jacket_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-default1.png", horizontal=True), 0.75))


## default1 (hard)
image jh jacket_hard = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.75))
)
image jh jacket_hard_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.75))
)
image jh jacket_hard_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-default1.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-default1.png", horizontal=True), 0.75))
)
image jh jacket_hard_color = im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.75)
image jh jacket_hard_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.75))
image jh jacket_hard_left_color = im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.75)
image jh jacket_hard_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-default1.png", 0.75))
image jh jacket_hard_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-default1.png", horizontal=True), 0.75)
image jh jacket_hard_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-default1.png", horizontal=True), 0.75))


## default2 (soft)
image jh jacket_soft = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-jacket1-default2.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-default2.png", 0.75))
)
image jh jacket_soft_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-jacket1-default2.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-default2.png", 0.75))
)
image jh jacket_soft_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-default2.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-default2.png", horizontal=True), 0.75))
)
image jh jacket_soft_color = im.FactorScale("Character Standing/mini-standing-jacket1-default2.png", 0.75)
image jh jacket_soft_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-default2.png", 0.75))
image jh jacket_soft_left_color = im.FactorScale("Character Standing/mini-standing-jacket1-default2.png", 0.75)
image jh jacket_soft_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-default2.png", 0.75))
image jh jacket_soft_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-default2.png", horizontal=True), 0.75)
image jh jacket_soft_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-default2.png", horizontal=True), 0.75))


## smile
image jh jacket_smile = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-jacket1-smile.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-smile.png", 0.75))
)
image jh jacket_smile_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-jacket1-smile.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-smile.png", 0.75))
)
image jh jacket_smile_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-smile.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-smile.png", horizontal=True), 0.75))
)
image jh jacket_smile_color = im.FactorScale("Character Standing/mini-standing-jacket1-smile.png", 0.75)
image jh jacket_smile_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-smile.png", 0.75))
image jh jacket_smile_left_color = im.FactorScale("Character Standing/mini-standing-jacket1-smile.png", 0.75)
image jh jacket_smile_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-jacket1-smile.png", 0.75))
image jh jacket_smile_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-smile.png", horizontal=True), 0.75)
image jh jacket_smile_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-jacket1-smile.png", horizontal=True), 0.75))



### shirt (longshirt)
## default (hard)
image jh shirt = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
)
image jh shirt_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
)
image jh shirt_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.75))
)
image jh shirt_color = im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75)
image jh shirt_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
image jh shirt_left_color = im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75)
image jh shirt_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
image jh shirt_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.75)
image jh shirt_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.75))


## default1 (hard)
image jh shirt_hard = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
)
image jh shirt_hard_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
)
image jh shirt_hard_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.75))
)
image jh shirt_hard_color = im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75)
image jh shirt_hard_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
image jh shirt_hard_left_color = im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75)
image jh shirt_hard_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
image jh shirt_hard_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.75)
image jh shirt_hard_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.75))


## default2 (soft)
image jh shirt_soft = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.75))
)
image jh shirt_soft_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.75))
)
image jh shirt_soft_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default2.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default2.png", horizontal=True), 0.75))
)
image jh shirt_soft_color = im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.75)
image jh shirt_soft_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.75))
image jh shirt_soft_left_color = im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.75)
image jh shirt_soft_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.75))
image jh shirt_soft_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default2.png", horizontal=True), 0.75)
image jh shirt_soft_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default2.png", horizontal=True), 0.75))


## smile
image jh shirt_smile = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.75))
)
image jh shirt_smile_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.75))
)
image jh shirt_smile_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-smile.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-smile.png", horizontal=True), 0.75))
)
image jh shirt_smile_color = im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.75)
image jh shirt_smile_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.75))
image jh shirt_smile_left_color = im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.75)
image jh shirt_smile_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.75))
image jh shirt_smile_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-smile.png", horizontal=True), 0.75)
image jh shirt_smile_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-smile.png", horizontal=True), 0.75))



### shirt1 (longshirt)
## default (hard)
image jh shirt_long = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
)
image jh shirt_long_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
)
image jh shirt_long_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.75))
)
image jh shirt_long_color = im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75)
image jh shirt_long_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
image jh shirt_long_left_color = im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75)
image jh shirt_long_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
image jh shirt_long_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.75)
image jh shirt_long_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.75))


## default1 (hard)
image jh shirt_long_hard = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
)
image jh shirt_long_hard_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
)
image jh shirt_long_hard_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.75))
)
image jh shirt_long_hard_color = im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75)
image jh shirt_long_hard_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
image jh shirt_long_hard_left_color = im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75)
image jh shirt_long_hard_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default1.png", 0.75))
image jh shirt_long_hard_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.75)
image jh shirt_long_hard_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default1.png", horizontal=True), 0.75))


## default2 (soft)
image jh shirt_long_soft = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.75))
)
image jh shirt_long_soft_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.75))
)
image jh shirt_long_soft_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default2.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default2.png", horizontal=True), 0.75))
)
image jh shirt_long_soft_color = im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.75)
image jh shirt_long_soft_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.75))
image jh shirt_long_soft_left_color = im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.75)
image jh shirt_long_soft_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-default2.png", 0.75))
image jh shirt_long_soft_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default2.png", horizontal=True), 0.75)
image jh shirt_long_soft_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-default2.png", horizontal=True), 0.75))


## smile
image jh shirt_long_smile = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.75))
)
image jh shirt_long_smile_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.75))
)
image jh shirt_long_smile_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-smile.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-smile.png", horizontal=True), 0.75))
)
image jh shirt_long_smile_color = im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.75)
image jh shirt_long_smile_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.75))
image jh shirt_long_smile_left_color = im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.75)
image jh shirt_long_smile_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt1-smile.png", 0.75))
image jh shirt_long_smile_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-smile.png", horizontal=True), 0.75)
image jh shirt_long_smile_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt1-smile.png", horizontal=True), 0.75))



### shirt2 (shirt)
## default (hard)
image jh shirt_hurt = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.75))
)
image jh shirt_hurt_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.75))
)
image jh shirt_hurt_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-default1.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-default1.png", horizontal=True), 0.75))
)
image jh shirt_hurt_color = im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.75)
image jh shirt_hurt_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.75))
image jh shirt_hurt_left_color = im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.75)
image jh shirt_hurt_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.75))
image jh shirt_hurt_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-default1.png", horizontal=True), 0.75)
image jh shirt_hurt_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-default1.png", horizontal=True), 0.75))


## default1 (hard)
image jh shirt_hurt_hard = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.75))
)
image jh shirt_hurt_hard_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.75))
)
image jh shirt_hurt_hard_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-default1.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-default1.png", horizontal=True), 0.75))
)
image jh shirt_hurt_hard_color = im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.75)
image jh shirt_hurt_hard_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.75))
image jh shirt_hurt_hard_left_color = im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.75)
image jh shirt_hurt_hard_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-default1.png", 0.75))
image jh shirt_hurt_hard_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-default1.png", horizontal=True), 0.75)
image jh shirt_hurt_hard_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-default1.png", horizontal=True), 0.75))


## default2 (soft)
image jh shirt_hurt_soft = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt2-default2.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-default2.png", 0.75))
)
image jh shirt_hurt_soft_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt2-default2.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-default2.png", 0.75))
)
image jh shirt_hurt_soft_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-default2.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-default2.png", horizontal=True), 0.75))
)
image jh shirt_hurt_soft_color = im.FactorScale("Character Standing/mini-standing-shirt2-default2.png", 0.75)
image jh shirt_hurt_soft_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-default2.png", 0.75))
image jh shirt_hurt_soft_left_color = im.FactorScale("Character Standing/mini-standing-shirt2-default2.png", 0.75)
image jh shirt_hurt_soft_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-default2.png", 0.75))
image jh shirt_hurt_soft_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-default2.png", horizontal=True), 0.75)
image jh shirt_hurt_soft_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-default2.png", horizontal=True), 0.75))


## smile
image jh shirt_hurt_smile = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt2-smile.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-smile.png", 0.75))
)
image jh shirt_hurt_smile_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt2-smile.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-smile.png", 0.75))
)
image jh shirt_hurt_smile_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-smile.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-smile.png", horizontal=True), 0.75))
)
image jh shirt_hurt_smile_color = im.FactorScale("Character Standing/mini-standing-shirt2-smile.png", 0.75)
image jh shirt_hurt_smile_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-smile.png", 0.75))
image jh shirt_hurt_smile_left_color = im.FactorScale("Character Standing/mini-standing-shirt2-smile.png", 0.75)
image jh shirt_hurt_smile_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt2-smile.png", 0.75))
image jh shirt_hurt_smile_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-smile.png", horizontal=True), 0.75)
image jh shirt_hurt_smile_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt2-smile.png", horizontal=True), 0.75))


### shirt3 (shortshirt)
## default (hard)
image jh shirt_short = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.75))
)
image jh shirt_short_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.75))
)
image jh shirt_short_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-default1.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-default1.png", horizontal=True), 0.75))
)
image jh shirt_short_color = im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.75)
image jh shirt_short_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.75))
image jh shirt_short_left_color = im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.75)
image jh shirt_short_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.75))
image jh shirt_short_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-default1.png", horizontal=True), 0.75)
image jh shirt_short_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-default1.png", horizontal=True), 0.75))


## default1 (hard)
image jh shirt_short_hard = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.75))
)
image jh shirt_short_hard_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.75))
)
image jh shirt_short_hard_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-default1.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-default1.png", horizontal=True), 0.75))
)
image jh shirt_short_hard_color = im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.75)
image jh shirt_short_hard_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.75))
image jh shirt_short_hard_left_color = im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.75)
image jh shirt_short_hard_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-default1.png", 0.75))
image jh shirt_short_hard_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-default1.png", horizontal=True), 0.75)
image jh shirt_short_hard_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-default1.png", horizontal=True), 0.75))


## default2 (soft)
image jh shirt_short_soft = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt3-default2.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-default2.png", 0.75))
)
image jh shirt_short_soft_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt3-default2.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-default2.png", 0.75))
)
image jh shirt_short_soft_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-default2.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-default2.png", horizontal=True), 0.75))
)
image jh shirt_short_soft_color = im.FactorScale("Character Standing/mini-standing-shirt3-default2.png", 0.75)
image jh shirt_short_soft_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-default2.png", 0.75))
image jh shirt_short_soft_left_color = im.FactorScale("Character Standing/mini-standing-shirt3-default2.png", 0.75)
image jh shirt_short_soft_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-default2.png", 0.75))
image jh shirt_short_soft_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-default2.png", horizontal=True), 0.75)
image jh shirt_short_soft_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-default2.png", horizontal=True), 0.75))


## smile
image jh shirt_short_smile = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt3-smile.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-smile.png", 0.75))
)
image jh shirt_short_smile_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("Character Standing/mini-standing-shirt3-smile.png", 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-smile.png", 0.75))
)
image jh shirt_short_smile_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-smile.png", horizontal=True), 0.78),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-smile.png", horizontal=True), 0.75))
)
image jh shirt_short_smile_color = im.FactorScale("Character Standing/mini-standing-shirt3-smile.png", 0.75)
image jh shirt_short_smile_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-smile.png", 0.75))
image jh shirt_short_smile_left_color = im.FactorScale("Character Standing/mini-standing-shirt3-smile.png", 0.75)
image jh shirt_short_smile_left_gray = im.Grayscale(im.FactorScale("Character Standing/mini-standing-shirt3-smile.png", 0.75))
image jh shirt_short_smile_right_color = im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-smile.png", horizontal=True), 0.75)
image jh shirt_short_smile_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/mini-standing-shirt3-smile.png", horizontal=True), 0.75))




##################
#### 김옥균 ####
##################
## base
image kog = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.75))
)
image kog color = im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.75)
image kog gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.75))



### shirt (short)
## default
image kog shirt = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.75))
)
image kog shirt_left = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.75))
)
image kog shirt_right = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-default.png", horizontal=True), 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-default.png", horizontal=True), 0.75))
)
image kog shirt_color = im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.75)
image kog shirt_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.75))
image kog shirt_left_color = im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.75)
image kog shirt_left_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.75))
image kog shirt_right_color = im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-default.png", horizontal=True), 0.75)
image kog shirt_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-default.png", horizontal=True), 0.75))


## angry
image kog shirt_angry = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.75))
)
image kog shirt_angry_left = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.75))
)
image kog shirt_angry_right = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-angry.png", horizontal=True), 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-angry.png", horizontal=True), 0.75))
)
image kog shirt_angry_color = im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.75)
image kog shirt_angry_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.75))
image kog shirt_angry_left_color = im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.75)
image kog shirt_angry_left_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.75))
image kog shirt_angry_right_color = im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-angry.png", horizontal=True), 0.75)
image kog shirt_angry_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-angry.png", horizontal=True), 0.75))


## smile1 (smile)
image kog shirt_smile = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.75))
)
image kog shirt_smile_left = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.75))
)
image kog shirt_smile_right = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile1.png", horizontal=True), 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile1.png", horizontal=True), 0.75))
)
image kog shirt_smile_color = im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.75)
image kog shirt_smile_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.75))
image kog shirt_smile_left_color = im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.75)
image kog shirt_smile_left_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.75))
image kog shirt_smile_right_color = im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile1.png", horizontal=True), 0.75)
image kog shirt_smile_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile1.png", horizontal=True), 0.75))


## smile2 (laugh)
image kog shirt_laugh = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.75))
)
image kog shirt_laugh_left = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.75))
)
image kog shirt_laugh_right = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile2.png", horizontal=True), 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile2.png", horizontal=True), 0.75))
)
image kog shirt_laugh_color = im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.75)
image kog shirt_laugh_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.75))
image kog shirt_laugh_left_color = im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.75)
image kog shirt_laugh_left_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.75))
image kog shirt_laugh_right_color = im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile2.png", horizontal=True), 0.75)
image kog shirt_laugh_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile2.png", horizontal=True), 0.75))



### shirt1 (short)
## default
image kog shirt_short = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.75))
)
image kog shirt_short_left = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.75))
)
image kog shirt_short_right = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-default.png", horizontal=True), 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-default.png", horizontal=True), 0.75))
)
image kog shirt_short_color = im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.75)
image kog shirt_short_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.75))
image kog shirt_short_left_color = im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.75)
image kog shirt_short_left_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-default.png", 0.75))
image kog shirt_short_right_color = im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-default.png", horizontal=True), 0.75)
image kog shirt_short_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-default.png", horizontal=True), 0.75))


## angry
image kog shirt_short_angry = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.75))
)
image kog shirt_short_angry_left = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.75))
)
image kog shirt_short_angry_right = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-angry.png", horizontal=True), 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-angry.png", horizontal=True), 0.75))
)
image kog shirt_short_angry_color = im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.75)
image kog shirt_short_angry_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.75))
image kog shirt_short_angry_left_color = im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.75)
image kog shirt_short_angry_left_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-angry.png", 0.75))
image kog shirt_short_angry_right_color = im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-angry.png", horizontal=True), 0.75)
image kog shirt_short_angry_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-angry.png", horizontal=True), 0.75))


## smile1 (smile)
image kog shirt_short_smile = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.75))
)
image kog shirt_short_smile_left = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.75))
)
image kog shirt_short_smile_right = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile1.png", horizontal=True), 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile1.png", horizontal=True), 0.75))
)
image kog shirt_short_smile_color = im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.75)
image kog shirt_short_smile_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.75))
image kog shirt_short_smile_left_color = im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.75)
image kog shirt_short_smile_left_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile1.png", 0.75))
image kog shirt_short_smile_right_color = im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile1.png", horizontal=True), 0.75)
image kog shirt_short_smile_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile1.png", horizontal=True), 0.75))


## smile2 (laugh)
image kog shirt_short_laugh = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.75))
)
image kog shirt_short_laugh_left = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.75))
)
image kog shirt_short_laugh_right = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile2.png", horizontal=True), 0.78),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile2.png", horizontal=True), 0.75))
)
image kog shirt_short_laugh_color = im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.75)
image kog shirt_short_laugh_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.75))
image kog shirt_short_laugh_left_color = im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.75)
image kog shirt_short_laugh_left_gray = im.Grayscale(im.FactorScale("Character Standing/pil-standing-shirt1-smile2.png", 0.75))
image kog shirt_short_laugh_right_color = im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile2.png", horizontal=True), 0.75)
image kog shirt_short_laugh_right_gray = im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-shirt1-smile2.png", horizontal=True), 0.75))


# ### jacket1
# ## default1 (hard)
# image kog jacket_hard = ConditionSwitch(
#     "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-jacket1-default1.png", 0.78),
#     "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-jacket1-default1.png", 0.75))
# )
# image kog jacket_hard_left = ConditionSwitch(
#     "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-jacket1-default1.png", 0.78),
#     "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-jacket1-default1.png", 0.75))
# )
# image kog jacket_hard_right = ConditionSwitch(
#     "_last_say_who == 'kog'", im.FactorScale(im.Flip("Character Standing/pil-standing-jacket1-default1.png", horizontal=True), 0.78),
#     "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-jacket1-default1.png", horizontal=True), 0.75))
# )


# ## default2 (soft)
# image kog jacket_soft = ConditionSwitch(
#     "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-jacket1-default2.png", 0.78),
#     "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-jacket1-default2.png", 0.75))
# )
# image kog jacket_soft_left = ConditionSwitch(
#     "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-jacket1-default2.png", 0.78),
#     "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-jacket1-default2.png", 0.75))
# )
# image kog jacket_soft_right = ConditionSwitch(
#     "_last_say_who == 'kog'", im.FactorScale(im.Flip("Character Standing/pil-standing-jacket1-default2.png", horizontal=True), 0.78),
#     "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-jacket1-default2.png", horizontal=True), 0.75))
# )


# ## smile
# image kog jacket_smile = ConditionSwitch(
#     "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-jacket1-smile.png", 0.78),
#     "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-jacket1-smile.png", 0.75))
# )
# image kog jacket_smile_left = ConditionSwitch(
#     "_last_say_who == 'kog'", im.FactorScale("Character Standing/pil-standing-jacket1-smile.png", 0.78),
#     "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("Character Standing/pil-standing-jacket1-smile.png", 0.75))
# )
# image kog jacket_smile_right = ConditionSwitch(
#     "_last_say_who == 'kog'", im.FactorScale(im.Flip("Character Standing/pil-standing-jacket1-smile.png", horizontal=True), 0.78),
#     "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("Character Standing/pil-standing-jacket1-smile.png", horizontal=True), 0.75))
# )





#################################################################################################################
#### 기타 설정 ####
#################################################################################################################
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
    key "K_AC_BACK" action NullAction
    key "mousedown_4" action NullAction
    key "joy_rollback" action NullAction





#################################################################################################################
#### label ####
#################################################################################################################
# 시작
label start:
    show screen remove_rollback()

    # jump script_test
    jump script_opening
    
    # if not persistent.start:
    #     jump intro
    # else:
    #     if (persistent.jh_selected == True):
    #         jump script_hjh
    #     elif (persistent.kog_selected == True):
    #         jump script_kog
    #     else:
    #         jump script_opening

    return


# 인트로
label intro:
    $ renpy.pause(2.0, hard=True)
    
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

    jump script_opening
    
    return