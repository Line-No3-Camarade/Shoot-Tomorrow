#################################################################################################################
###### 게임 스크립트 설정 ######
#################################################################################################################
default preferences.text_cps = 30

define zoom_in = 0.78
define zoom_out = 0.75






#################################################################################################################
###### 이미지 정의 ######
#################################################################################################################
image black = "background/bg_black.png"
image white = "background/bg_white.png"

image deck = "background/bg_deck.jpg"
image hallway = "background/bg_hallway.jpg"
image harbor = "background/보정/bg_harbor.png"
image hjh_house = "background/bg_hjh_house.png"
image hotel = "background/bg_hotel.jpg"
image kog_house = "background/bg_kog_house.png"
image library = "background/bg_library.jpg"
image nightsea = "background/bg_nightsea.jpg"
image palaceis = "background/bg_palaceis.jpg"
image palaceos = "background/보정/bg_palaceos.png"
image river = "background/bg_river.jpg"
image sea = "background/보정/bg_sea.png"
image street = "background/보정/bg_street.png"
image tatami = "background/bg_tatami.jpg"






#################################################################################################################
###### 캐릭터 정의 ######
#################################################################################################################
define dnarrator = Character(None, what_color="#e6e6e6")

define jh = Character('정훈', color="#a0a0a0")
define hjh = Character('한정훈', color="#ffffff")
define kog = Character('김옥균', color="#ffffff")
define jy = Character('종윤', color="#5587ED")
define emp = Character('이희', color="#F6F6F6")
define umm = Character('엄 상궁', color="#23A41A")
define iw = Character('이완', color="#740000")
define iy = Character('이연', color="#38610B")
define soph = Character('소피', color="#143d8e")
define wada = Character('와다', color="#9cf89f")
define hsg = Character('홍승규', color="#FF7171")
define hjw = Character('홍종우', color="#ff3434")
define hjw_q = Character('홍종우?', color="#a0a0a0")






#################################################################################################################
###### 캐릭터 이미지 정의 ######
#################################################################################################################
image none = im.FactorScale("character/standing-x.png", zoom_out)


##################
##### 정훈 #####
##################
### color & gray
## default
# outfit
image jh_jacekt_base = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("character/mini-standing-jacket1-x.png", zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("character/mini-standing-jacket1-x.png", zoom_out))
)
image jh_shirt_long = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("character/mini-standing-shirt1-x.png", zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("character/mini-standing-shirt1-x.png", zoom_out))
)
image jh_shirt_hurt = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("character/mini-standing-shirt2-x.png", zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("character/mini-standing-shirt2-x.png", zoom_out))
)
image jh_shirt_short = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("character/mini-standing-shirt3-x.png", zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("character/mini-standing-shirt3-x.png", zoom_out))
)


# face
image jh_hard = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("character/mini-default1.png", zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("character/mini-default1.png", zoom_out))
)
image jh_soft = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("character/mini-default2.png", zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("character/mini-default2.png", zoom_out))
)
image jh_smile = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("character/mini-smile.png", zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("character/mini-smile.png", zoom_out))
)



## left
# outfit
image jh_jacekt_base_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("character/mini-standing-jacket1-x.png", zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("character/mini-standing-jacket1-x.png", zoom_out))
)
image jh_shirt_long_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("character/mini-standing-shirt1-x.png", zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("character/mini-standing-shirt1-x.png", zoom_out))
)
image jh_shirt_hurt_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("character/mini-standing-shirt2-x.png", zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("character/mini-standing-shirt2-x.png", zoom_out))
)
image jh_shirt_short_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("character/mini-standing-shirt3-x.png", zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("character/mini-standing-shirt3-x.png", zoom_out))
)


# face
image jh_hard_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("character/mini-default1.png", zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("character/mini-default1.png", zoom_out))
)
image jh_soft_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("character/mini-default2.png", zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("character/mini-default2.png", zoom_out))
)
image jh_smile_left = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale("character/mini-smile.png", zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale("character/mini-smile.png", zoom_out))
)



## right
# outfit
image jh_jacekt_base_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("character/mini-standing-jacket1-x.png", horizontal=True), zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("character/mini-standing-jacket1-x.png", horizontal=True), zoom_out))
)
image jh_shirt_long_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("character/mini-standing-shirt1-x.png", horizontal=True), zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("character/mini-standing-shirt1-x.png", horizontal=True), zoom_out))
)
image jh_shirt_hurt_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("character/mini-standing-shirt2-x.png", horizontal=True), zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("character/mini-standing-shirt2-x.png", horizontal=True), zoom_out))
)
image jh_shirt_short_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("character/mini-standing-shirt3-x.png", horizontal=True), zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("character/mini-standing-shirt3-x.png", horizontal=True), zoom_out))
)


# face
image jh_hard_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("character/mini-default1.png", horizontal=True), zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("character/mini-default1.png", horizontal=True), zoom_out))
)
image jh_soft_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("character/mini-default2.png", horizontal=True), zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("character/mini-default2.png", horizontal=True), zoom_out))
)
image jh_smile_right = ConditionSwitch(
    "_last_say_who == 'jh' or _last_say_who == 'hjw_q'", im.FactorScale(im.Flip("character/mini-smile.png", horizontal=True), zoom_in),
    "not _last_say_who == 'jh' or not _last_say_who == 'hjw_q'", im.Grayscale(im.FactorScale(im.Flip("character/mini-smile.png", horizontal=True), zoom_out))
)





### color
## default
# outfit
image jh_jacekt_base_color = im.FactorScale("character/mini-standing-jacket1-x.png", zoom_out)
image jh_shirt_long_color = im.FactorScale("character/mini-standing-shirt1-x.png", zoom_out)
image jh_shirt_hurt_color = im.FactorScale("character/mini-standing-shirt2-x.png", zoom_out)
image jh_shirt_short_color = im.FactorScale("character/mini-standing-shirt3-x.png", zoom_out)

# face
image jh_hard_color = im.FactorScale("character/mini-default1.png", zoom_out)
image jh_soft_color = im.FactorScale("character/mini-default2.png", zoom_out)
image jh_smile_color = im.FactorScale("character/mini-smile.png", zoom_out)



## left
# outfit
image jh_jacekt_base_color_left = im.FactorScale("character/mini-standing-jacket1-x.png", zoom_out)
image jh_shirt_long_color_left = im.FactorScale("character/mini-standing-shirt1-x.png", zoom_out)
image jh_shirt_hurt_color_left = im.FactorScale("character/mini-standing-shirt2-x.png", zoom_out)
image jh_shirt_short_color_left = im.FactorScale("character/mini-standing-shirt3-x.png", zoom_out)

# face
image jh_hard_color_left = im.FactorScale("character/mini-default1.png", zoom_out)
image jh_soft_color_left = im.FactorScale("character/mini-default2.png", zoom_out)
image jh_smile_color_left = im.FactorScale("character/mini-smile.png", zoom_out)



## right
# outfit
image jh_jacekt_base_color_right = im.FactorScale(im.Flip("character/mini-standing-jacket1-x.png", horizontal=True), zoom_out)
image jh_shirt_long_color_right = im.FactorScale(im.Flip("character/mini-standing-shirt1-x.png", horizontal=True), zoom_out)
image jh_shirt_hurt_color_right = im.FactorScale(im.Flip("character/mini-standing-shirt2-x.png", horizontal=True), zoom_out)
image jh_shirt_short_color_right = im.FactorScale(im.Flip("character/mini-standing-shirt3-x.png", horizontal=True), zoom_out)

# face
image jh_hard_color_right = im.FactorScale(im.Flip("character/mini-default1.png", horizontal=True), zoom_out)
image jh_soft_color_right = im.FactorScale(im.Flip("character/mini-default2.png", horizontal=True), zoom_out)
image jh_smile_color_right = im.FactorScale(im.Flip("character/mini-smile.png", horizontal=True), zoom_out)




### gray
## default
# outfit
image jh_jacekt_base_gray = im.Grayscale("character/mini-standing-jacket1-x.png")
image jh_shirt_long_gray = im.Grayscale("character/mini-standing-shirt1-x.png")
image jh_shirt_hurt_gray = im.Grayscale("character/mini-standing-shirt2-x.png")
image jh_shirt_short_gray = im.Grayscale("character/mini-standing-shirt3-x.png")

# face
image jh_hard_gray = im.Grayscale("character/mini-default1.png")
image jh_soft_gray = im.Grayscale("character/mini-default2.png")
image jh_smile_gray = im.Grayscale("character/mini-smile.png")



## left
# outfit
image jh_jacekt_base_gray_left = im.Grayscale("character/mini-standing-jacket1-x.png")
image jh_shirt_long_gray_left = im.Grayscale("character/mini-standing-shirt1-x.png")
image jh_shirt_hurt_gray_left = im.Grayscale("character/mini-standing-shirt2-x.png")
image jh_shirt_short_gray_left = im.Grayscale("character/mini-standing-shirt3-x.png")

# face
image jh_hard_gray_left = im.Grayscale("character/mini-default1.png")
image jh_soft_gray_left = im.Grayscale("character/mini-default2.png")
image jh_smile_gray_left = im.Grayscale("character/mini-smile.png")



## right
# outfit
image jh_jacekt_base_gray_right = im.Grayscale(im.Flip("character/mini-standing-jacket1-x.png", horizontal=True))
image jh_shirt_long_gray_right = im.Grayscale(im.Flip("character/mini-standing-shirt1-x.png", horizontal=True))
image jh_shirt_hurt_gray_right = im.Grayscale(im.Flip("character/mini-standing-shirt2-x.png", horizontal=True))
image jh_shirt_short_gray_right = im.Grayscale(im.Flip("character/mini-standing-shirt3-x.png", horizontal=True))

# face
image jh_hard_gray_right = im.Grayscale(im.Flip("character/mini-default1.png", horizontal=True))
image jh_soft_gray_right = im.Grayscale(im.Flip("character/mini-default2.png", horizontal=True))
image jh_smile_gray_right = im.Grayscale(im.Flip("character/mini-smile.png", horizontal=True))





### layeredimage
layeredimage jh:
    group outfit:
        attribute jacket:
            "jh_jacekt_base"
        attribute shirt default:
            "jh_shirt_long "
        attribute shirt_long:
            "jh_shirt_long "
        attribute shirt_short:
            "jh_shirt_short"
        attribute shirt_hurt:
            "jh_shirt_hurt"
    
    group face:
        attribute hard default:
            "jh_hard"
        attribute soft:
            "jh_soft"
        attribute smile:
            "jh_smile"


layeredimage jh_left:
    group outfit:
        attribute jacket:
            "jh_jacekt_base_left"
        attribute shirt default:
            "jh_shirt_long_left"
        attribute shirt_long:
            "jh_shirt_long_left"
        attribute shirt_short:
            "jh_shirt_short_left"
        attribute shirt_hurt:
            "jh_shirt_hurt_left"
    
    group face:
        attribute hard default:
            "jh_hard_left"
        attribute soft:
            "jh_soft_left"
        attribute smile:
            "jh_smile_left"


layeredimage jh_right:
    group outfit:
        attribute jacket:
            "jh_jacekt_base_right"
        attribute shirt default:
            "jh_shirt_long_right"
        attribute shirt_long:
            "jh_shirt_long_right"
        attribute shirt_short:
            "jh_shirt_short_right"
        attribute shirt_hurt:
            "jh_shirt_hurt_right"
    
    group face:
        attribute hard default:
            "jh_hard_right"
        attribute soft:
            "jh_soft_right"
        attribute smile:
            "jh_smile_right"



layeredimage jh_color:
    group outfit:
        attribute jacket:
            "jh_jacekt_base_color"
        attribute shirt default:
            "jh_shirt_long_color"
        attribute shirt_long:
            "jh_shirt_long_color"
        attribute shirt_short:
            "jh_shirt_short_color"
        attribute shirt_hurt:
            "jh_shirt_hurt_color"
    
    group face:
        attribute hard default:
            "jh_hard_color"
        attribute soft:
            "jh_soft_color"
        attribute smile:
            "jh_smile_color"


layeredimage jh_color_left:
    group outfit:
        attribute jacket:
            "jh_jacekt_base_color_left"
        attribute shirt default:
            "jh_shirt_long_color_left"
        attribute shirt_long:
            "jh_shirt_long_color_left"
        attribute shirt_short:
            "jh_shirt_short_color_left"
        attribute shirt_hurt:
            "jh_shirt_hurt_color_left"
    
    group face:
        attribute hard default:
            "jh_hard_color_left"
        attribute soft:
            "jh_soft_color_left"
        attribute smile:
            "jh_smile_color_left"


layeredimage jh_color_right:
    group outfit:
        attribute jacket:
            "jh_jacekt_base_color_right"
        attribute shirt default:
            "jh_shirt_long_color_right"
        attribute shirt_long:
            "jh_shirt_long_color_right"
        attribute shirt_short:
            "jh_shirt_short_color_right"
        attribute shirt_hurt:
            "jh_shirt_hurt_color_right"
    
    group face:
        attribute hard default:
            "jh_hard_color_right"
        attribute soft:
            "jh_soft_color_right"
        attribute smile:
            "jh_smile_color_right"



layeredimage jh_gray:
    zoom 0.75

    group outfit:
        attribute jacket:
            "jh_jacekt_base_gray"
        attribute shirt default:
            "jh_shirt_long_gray"
        attribute shirt_long:
            "jh_shirt_long_gray"
        attribute shirt_short:
            "jh_shirt_short_gray"
        attribute shirt_hurt:
            "jh_shirt_hurt_gray"
    
    group face:
        attribute hard default:
            "jh_hard_gray"
        attribute soft:
            "jh_soft_gray"
        attribute smile:
            "jh_smile_gray"


layeredimage jh_gray_left:
    zoom 0.75
    
    group outfit:
        attribute jacket:
            "jh_jacekt_base_gray_left"
        attribute shirt default:
            "jh_shirt_long_gray_left"
        attribute shirt_long:
            "jh_shirt_long_gray_left"
        attribute shirt_short:
            "jh_shirt_short_gray_left"
        attribute shirt_hurt:
            "jh_shirt_hurt_gray_left"
    
    group face:
        attribute hard default:
            "jh_hard_gray_left"
        attribute soft:
            "jh_soft_gray_left"
        attribute smile:
            "jh_smile_gray_left"


layeredimage jh_gray_right:
    zoom 0.75
    
    group outfit:
        attribute jacket:
            "jh_jacekt_base_gray_right"
        attribute shirt default:
            "jh_shirt_long_gray_right"
        attribute shirt_long:
            "jh_shirt_long_gray_right"
        attribute shirt_short:
            "jh_shirt_short_gray_right"
        attribute shirt_hurt:
            "jh_shirt_hurt_gray_right"
    
    group face:
        attribute hard default:
            "jh_hard_gray_right"
        attribute soft:
            "jh_soft_gray_right"
        attribute smile:
            "jh_smile_gray_right"





# ##################
# #### 김옥균 ####
# ##################

### color & gray
## default
# outfit
image kog_shirt = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("character/pil-standing-shirt1-x.png", zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("character/pil-standing-shirt1-x.png", zoom_out))
)
image kog_shirt_base = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("character/pil-standing-shirt1-x.png", zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("character/pil-standing-shirt1-x.png", zoom_out))
)


# face
image kog_neutral = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("character/pil-default.png", zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("character/pil-default.png", zoom_out))
)
image kog_smile = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("character/pil-smile.png", zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("character/pil-smile.png", zoom_out))
)
image kog_laugh = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("character/pil-smile2.png", zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("character/pil-smile2.png", zoom_out))
)
image kog_angry = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("character/pil-angry.png", zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("character/pil-angry.png", zoom_out))
)



## left
image kog_shirt_left = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("character/pil-standing-shirt1-x.png", zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("character/pil-standing-shirt1-x.png", zoom_out))
)
image kog_shirt_base_left = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("character/pil-standing-shirt1-x.png", zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("character/pil-standing-shirt1-x.png", zoom_out))
)


# face
image kog_neutral_left = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("character/pil-default.png", zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("character/pil-default.png", zoom_out))
)
image kog_smile_left = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("character/pil-smile.png", zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("character/pil-smile.png", zoom_out))
)
image kog_laugh_left = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("character/pil-smile2.png", zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("character/pil-smile2.png", zoom_out))
)
image kog_angry_left = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale("character/pil-angry.png", zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale("character/pil-angry.png", zoom_out))
)



## right
# outfit
image kog_shirt_right = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("character/pil-standing-shirt1-x.png", horizontal=True), zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("character/pil-standing-shirt1-x.png", horizontal=True), zoom_out))
)
image kog_shirt_base_right = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("character/pil-standing-shirt1-x.png", horizontal=True), zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("character/pil-standing-shirt1-x.png", horizontal=True), zoom_out))
)


# face
image kog_neutral_right= ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("character/pil-default.png", horizontal=True), zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("character/pil-default.png", horizontal=True), zoom_out))
)
image kog_smile_right = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("character/pil-smile.png", horizontal=True), zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("character/pil-smile.png", horizontal=True), zoom_out))
)
image kog_laugh_right = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("character/pil-smile2.png", horizontal=True), zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("character/pil-smile2.png", horizontal=True), zoom_out))
)
image kog_angry_right = ConditionSwitch(
    "_last_say_who == 'kog'", im.FactorScale(im.Flip("character/pil-angry.png", horizontal=True), zoom_in),
    "not _last_say_who == 'kog'", im.Grayscale(im.FactorScale(im.Flip("character/pil-angry.png", horizontal=True), zoom_out))
)





### color
## default
# outfit
image kog_shirt_color = im.FactorScale("character/pil-standing-shirt1-x.png", zoom_out)
image kog_shirt_base_color = im.FactorScale("character/pil-standing-shirt1-x.png", zoom_out)

# face
image kog_neutral_color = im.FactorScale("character/pil-default.png", zoom_out)
image kog_smile_color = im.FactorScale("character/pil-smile.png", zoom_out)
image kog_laugh_color = im.FactorScale("character/pil-smile2.png", zoom_out)
image kog_angry_color = im.FactorScale("character/pil-angry.png", zoom_out)



## left
# outfit
image kog_shirt_color_left = im.FactorScale("character/pil-standing-shirt1-x.png", zoom_out)
image kog_shirt_base_color_left = im.FactorScale("character/pil-standing-shirt1-x.png", zoom_out)

# face
image kog_neutral_color_left = im.FactorScale("character/pil-default.png", zoom_out)
image kog_smile_color_left = im.FactorScale("character/pil-smile.png", zoom_out)
image kog_laugh_color_left = im.FactorScale("character/pil-smile2.png", zoom_out)
image kog_angry_color_left = im.FactorScale("character/pil-angry.png", zoom_out)



## right
# outfit
image kog_shirt_color_right = im.FactorScale(im.Flip("character/pil-standing-shirt1-x.png", horizontal=True), zoom_out)
image kog_shirt_base_color_right = im.FactorScale(im.Flip("character/pil-standing-shirt1-x.png", horizontal=True), zoom_out)

# face
image kog_neutral_color_right = im.FactorScale(im.Flip("character/pil-default.png", horizontal=True), zoom_out)
image kog_smile_color_right = im.FactorScale(im.Flip("character/pil-smile.png", horizontal=True), zoom_out)
image kog_laugh_color_right = im.FactorScale(im.Flip("character/pil-smile2.png", horizontal=True), zoom_out)
image kog_angry_color_right = im.FactorScale(im.Flip("character/pil-angry.png", horizontal=True), zoom_out)




### gray
## default
# outfit
image kog_shirt_gray = im.Grayscale("character/pil-standing-shirt1-x.png")
image kog_shirt_base_gray = im.Grayscale("character/pil-standing-shirt1-x.png")

# face
image kog_neutral_gray = im.Grayscale("character/pil-default.png")
image kog_smile_gray = im.Grayscale("character/pil-smile.png")
image kog_laugh_gray = im.Grayscale("character/pil-smile2.png")
image kog_angry_gray = im.Grayscale("character/pil-angry.png")



## left
# outfit
image kog_shirt_gray_left = im.Grayscale("character/pil-standing-shirt1-x.png")
image kog_shirt_base_gray_left = im.Grayscale("character/pil-standing-shirt1-x.png")

# face
image kog_neutral_gray_left = im.Grayscale("character/pil-default.png")
image kog_smile_gray_left = im.Grayscale("character/pil-smile.png")
image kog_laugh_gray_left = im.Grayscale("character/pil-smile2.png")
image kog_angry_gray_left = im.Grayscale("character/pil-angry.png")



## right
# outfit
image kog_shirt_gray_right = im.Grayscale(im.Flip("character/pil-standing-shirt1-x.png", horizontal=True))
image kog_shirt_base_gray_right = im.Grayscale(im.Flip("character/pil-standing-shirt1-x.png", horizontal=True))

# face
image kog_neutral_gray_right = im.Grayscale(im.Flip("character/pil-default.png", horizontal=True))
image kog_smile_gray_right = im.Grayscale(im.Flip("character/pil-smile.png", horizontal=True))
image kog_laugh_gray_right = im.Grayscale(im.Flip("character/pil-smile2.png", horizontal=True))
image kog_angry_gray_right = im.Grayscale(im.Flip("character/pil-angry.png", horizontal=True))





### layeredimage
layeredimage kog:
    group outfit:
        attribute shirt default:
            "kog_shirt_base"
    
    group face:
        attribute neutral default:
            "kog_neutral"
        attribute smile:
            "kog_smile"
        attribute laugh:
            "kog_laugh"
        attribute angry:
            "kog_angry"


layeredimage kog_left:
    group outfit:
        attribute shirt default:
            "kog_shirt_left"
    
    group face:
        attribute neutral default:
            "kog_neutral_left"
        attribute smile:
            "kog_smile_left"
        attribute laugh:
            "kog_laugh_left"
        attribute angry:
            "kog_angry_left"


layeredimage kog_right:
    group outfit:
        attribute shirt default:
            "kog_shirt_right"
    
    group face:
        attribute neutral default:
            "kog_neutral_right"
        attribute smile:
            "kog_smile_right"
        attribute laugh:
            "kog_laugh_right"
        attribute angry:
            "kog_angry_right"



layeredimage kog_color:
    group outfit:
        attribute shirt default:
            "kog_shirt_color"
    
    group face:
        attribute neutral default:
            "kog_neutral_color"
        attribute smile:
            "kog_smile_color"
        attribute laugh:
            "kog_laugh_color"
        attribute angry:
            "kog_angry_color"


layeredimage kog_color_left:
    group outfit:
        attribute shirt default:
            "kog_shirt_color_left"
    
    group face:
        attribute neutral default:
            "kog_neutral_color_left"
        attribute smile:
            "kog_smile_color_left"
        attribute laugh:
            "kog_laugh_color_left"
        attribute angry:
            "kog_angry_color_left"


layeredimage kog_color_right:
    group outfit:
        attribute shirt default:
            "kog_shirt_color_right"
    
    group face:
        attribute neutral default:
            "kog_neutral_color_right"
        attribute smile:
            "kog_smile_color_right"
        attribute laugh:
            "kog_laugh_color_right"
        attribute angry:
            "kog_angry_color_right"



layeredimage kog_gray:
    zoom 0.75

    group outfit:
        attribute shirt default:
            "kog_shirt_gray"
    
    group face:
        attribute neutral default:
            "kog_neutral_gray"
        attribute smile:
            "kog_smile_gray"
        attribute laugh:
            "kog_laugh_gray"
        attribute angry:
            "kog_angry_gray"


layeredimage kog_gray_left:
    zoom 0.75
    
    group outfit:
        attribute shirt default:
            "kog_shirt_gray_left"
    
    group face:
        attribute neutral default:
            "kog_neutral_gray_left"
        attribute smile:
            "kog_smile_gray_left"
        attribute laugh:
            "kog_laugh_gray_left"
        attribute angry:
            "kog_angry_gray_left"


layeredimage kog_gray_right:
    zoom 0.75
    
    group outfit:
        attribute shirt default:
            "kog_shirt_gray_right"
    
    group face:
        attribute neutral default:
            "kog_neutral_gray_right"
        attribute smile:
            "kog_smile_gray_right"
        attribute laugh:
            "kog_laugh_gray_right"
        attribute angry:
            "kog_angry_gray_right"






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