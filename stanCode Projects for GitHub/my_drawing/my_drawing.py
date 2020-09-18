"""
File: my_drawing.py
Name: Tiffany Lin
----------------------
stanCode SC101 May2020
Assignment 1- Problem 1
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel, GLine
from campy.graphics.gwindow import GWindow

# Global variable
window = GWindow(width=1200, height=750, title="Tiffany's Masterpiece")


def main():
    """
    A drawing mainly consists of 5 components:
    1) Sun
    2) Clouds
    3) The house
    4) Minion
    5) "STAY HOME" sticker
    """
    draw_sun()
    draw_cloud()
    draw_house()
    draw_stay_home_sticker()
    draw_minion()


def draw_sun():
    """
    :return: A yellow sun on the upper left corner
    """
    add_sun()
    add_sunbeam()


def draw_cloud():
    """
    :return: Two blue clouds on the upper right area
    """
    l_cloud()
    r_cloud()


def draw_house():
    """
    :return: A house consists of a rooftop, a chimney and two walls
    """
    draw_rooftop()
    draw_walls()


def draw_stay_home_sticker():
    """
    :return: An "stay home" sticker similar to the one on IG added on the lower right area along with two hashtags
    """
    bg()
    add_heart()
    add_words()


def draw_minion():
    """
    :return: A minion wearing pink face mask in the house
    """
    add_head()
    add_hands()
    add_body()
    add_eyes()
    face_mask()


def add_sun():
    # The circle in the middle of the sun ; a part of the function -- "draw_sun()"
    sun = GOval(280, 280)
    sun.filled = True
    sun.fill_color = 'gold'
    sun.color = 'gold'
    window.add(sun, -100, -100)


def add_sunbeam():
    # The beams of lights from the sun ; a part of the function -- "draw_sun()"
    sunshine_1 = GRect(30, 65)
    sunshine_1.filled = True
    sunshine_1.fill_color = 'gold'
    sunshine_1.color = 'gold'
    window.add(sunshine_1, 25, 200)
    sunshine_2_1 = GPolygon()
    sunshine_2_1.add_vertex((115, 181))
    sunshine_2_1.add_vertex((110, 260))
    sunshine_2_1.add_vertex((90, 195))
    sunshine_2_1.filled = True
    sunshine_2_1.fill_color = 'gold'
    sunshine_2_1.color = 'gold'
    window.add(sunshine_2_1)
    sunshine_2_2 = GPolygon()
    sunshine_2_2.add_vertex((115, 181))
    sunshine_2_2.add_vertex((110, 260))
    sunshine_2_2.add_vertex((135, 245))
    sunshine_2_2.filled = True
    sunshine_2_2.fill_color = 'gold'
    sunshine_2_2.color = 'gold'
    window.add(sunshine_2_2)
    sunshine_3_1 = GPolygon()
    sunshine_3_1.add_vertex((148, 160))
    sunshine_3_1.add_vertex((165, 140))
    sunshine_3_1.add_vertex((190, 215))
    sunshine_3_1.filled = True
    sunshine_3_1.fill_color = 'gold'
    sunshine_3_1.color = 'gold'
    window.add(sunshine_3_1)
    sunshine_3_2 = GPolygon()
    sunshine_3_2.add_vertex((215, 195))
    sunshine_3_2.add_vertex((165, 140))
    sunshine_3_2.add_vertex((190, 215))
    sunshine_3_2.filled = True
    sunshine_3_2.fill_color = 'gold'
    sunshine_3_2.color = 'gold'
    window.add(sunshine_3_2)
    sunshine_4_1 = GPolygon()
    sunshine_4_1.add_vertex((198, 85))
    sunshine_4_1.add_vertex((248, 132))
    sunshine_4_1.add_vertex((188, 110))
    sunshine_4_1.filled = True
    sunshine_4_1.fill_color = 'gold'
    sunshine_4_1.color = 'gold'
    window.add(sunshine_4_1)
    sunshine_4_2 = GPolygon()
    sunshine_4_2.add_vertex((198, 85))
    sunshine_4_2.add_vertex((248, 132))
    sunshine_4_2.add_vertex((265, 100))
    sunshine_4_2.filled = True
    sunshine_4_2.fill_color = 'gold'
    sunshine_4_2.color = 'gold'
    window.add(sunshine_4_2)
    sunshine_5 = GRect(70, 30)
    sunshine_5.filled = True
    sunshine_5.fill_color = 'gold'
    sunshine_5.color = 'gold'
    window.add(sunshine_5, 200, 20)


def l_cloud():
    # The cloud on the left; a part of the function -- "draw_cloud()"
    l_c_1 = GOval(80, 80, x=665, y=40)
    l_c_1.filled = True
    l_c_1.fill_color = 'lightskyblue'
    l_c_1.color = 'lightskyblue'
    window.add(l_c_1)
    l_c_2 = GOval(80, 80, x=720, y=30)
    l_c_2.filled = True
    l_c_2.fill_color = 'lightskyblue'
    l_c_2.color = 'lightskyblue'
    window.add(l_c_2)
    l_c_3 = GOval(100, 90, x=780, y=40)
    l_c_3.filled = True
    l_c_3.fill_color = 'lightskyblue'
    l_c_3.color = 'lightskyblue'
    window.add(l_c_3)
    l_c_4 = GOval(100, 100, x=630, y=90)
    l_c_4.filled = True
    l_c_4.fill_color = 'lightskyblue'
    l_c_4.color = 'lightskyblue'
    window.add(l_c_4)
    l_c_5 = GOval(140, 120, x=700, y=90)
    l_c_5.filled = True
    l_c_5.fill_color = 'lightskyblue'
    l_c_5.color = 'lightskyblue'
    window.add(l_c_5)
    l_c_6 = GOval(100, 100, x=790, y=90)
    l_c_6.filled = True
    l_c_6.fill_color = 'lightskyblue'
    l_c_6.color = 'lightskyblue'
    window.add(l_c_6)


def r_cloud():
    # The cloud on the right; a part of the function -- "draw_cloud()"
    r_c_1 = GOval(80, 80, x=1015, y=40)
    r_c_1.filled = True
    r_c_1.fill_color = 'lightskyblue'
    r_c_1.color = 'lightskyblue'
    window.add(r_c_1)
    r_c_2 = GOval(80, 80, x=1070, y=30)
    r_c_2.filled = True
    r_c_2.fill_color = 'lightskyblue'
    r_c_2.color = 'lightskyblue'
    window.add(r_c_2)
    r_c_3 = GOval(100, 90, x=1130, y=40)
    r_c_3.filled = True
    r_c_3.fill_color = 'lightskyblue'
    r_c_3.color = 'lightskyblue'
    window.add(r_c_3)
    r_c_4 = GOval(100, 100, x=980, y=90)
    r_c_4.filled = True
    r_c_4.fill_color = 'lightskyblue'
    r_c_4.color = 'lightskyblue'
    window.add(r_c_4)
    r_c_5 = GOval(140, 120, x=1050, y=90)
    r_c_5.filled = True
    r_c_5.fill_color = 'lightskyblue'
    r_c_5.color = 'lightskyblue'
    window.add(r_c_5)
    r_c_6 = GOval(100, 100, x=1140, y=90)
    r_c_6.filled = True
    r_c_6.fill_color = 'lightskyblue'
    r_c_6.color = 'lightskyblue'
    window.add(r_c_6)


def draw_rooftop():
    # The rooftop and chimney of the house; a part of the function -- "draw_house()"
    rooftop = GPolygon()
    rooftop.add_vertex((40, 400)) #屋頂左
    rooftop.add_vertex((440, 210)) #屋頂
    rooftop.add_vertex((840, 400)) #屋頂右
    rooftop.filled = True
    rooftop.fill_color = 'grey'
    rooftop.color = 'grey'
    window.add(rooftop)

    chimney = GRect(115, 90, x=540, y=235)
    chimney.filled = True
    chimney.fill_color = 'grey'
    chimney.color = 'grey'
    window.add(chimney)

    sign_shadow = GLabel('stanCode \n   SC101')
    sign_shadow.color = 'ivory'
    sign_shadow.font = '-40-bold'
    window.add(sign_shadow, 348, 377)

    sign = GLabel('stanCode \n   SC101')
    sign.color = 'darkred'
    sign.font = '-40-bold'
    window.add(sign, 350, 375)


def draw_walls():
    # The walls on both left and right side of the house; a part of the function -- "draw_house()"
    left_wall = GRect(10, 350)
    left_wall.filled = True
    left_wall.fill_color = 'grey'
    left_wall.color = 'grey'
    window.add(left_wall, 140, 400)

    right_wall = GRect(10, 350)
    right_wall.filled = True
    right_wall.fill_color = 'grey'
    right_wall.color = 'grey'
    window.add(right_wall, 730, 400)


def bg():
    # The background color of the sticker ; a part of the function -- "draw_stay_home_sticker()"
    sticker_bg = GRect(300, 135, x=840, y=513)
    sticker_bg.filled = True
    sticker_bg.fill_color = 'ivory'
    sticker_bg.color = 'ivory'
    window.add(sticker_bg)


def add_heart():
    # The heart shape icon on the sticker ; a part of the function -- "draw_stay_home_sticker()"
    left_circle = GOval(61, 60, x=851, y=529)
    left_circle.filled = True
    left_circle.fill_color = 'pink'
    left_circle.color = 'pink'
    window.add(left_circle)

    right_circle = GOval(61, 60, x=907.5, y=529)
    right_circle.filled = True
    right_circle.fill_color = 'pink'
    right_circle.color = 'pink'
    window.add(right_circle)

    bottom_triangle = GPolygon()
    bottom_triangle.add_vertex((853.4, 571))
    bottom_triangle.add_vertex((966.8, 571))
    bottom_triangle.add_vertex((909, 640))
    bottom_triangle.filled = True
    bottom_triangle.fill_color = 'pink'
    bottom_triangle.color = 'pink'
    window.add(bottom_triangle)


def add_words():
    # The words on the sticker ; a part of the function -- "draw_stay_home_sticker()"
    word = GLabel('STAY \nHOME')
    word.font = 'Courier-50-bold'
    word.color = 'pink'
    window.add(word, 988, 638)

    label = GLabel('#May2020 #Taiwan')
    label.font = 'courier-17-italic'
    label.color = 'pink'
    window.add(label, 973, 675)


def add_head():
    # The head part of minion; a part of the function -- "draw_minion()"
    head = GOval(160, 160, x=345, y=455)
    head.filled = True
    head.fill_color = 'yellow'
    head.color = 'yellow'
    window.add(head)


def add_hands():
    # Minion's hands; a part of the function -- "draw_minion()"
    l_hand = GOval(100, 65, x=312, y=620)
    l_hand.filled = True
    l_hand.fill_color = 'yellow'
    l_hand.color = 'yellow'
    window.add(l_hand)
    l_hand_blank = GOval(85, 45, x=327, y=630)
    l_hand_blank.filled = True
    l_hand_blank.fill_color = 'white'
    l_hand_blank.color = 'white'
    window.add(l_hand_blank)
    l_thumb = GOval(16, 28, x=338, y=660)
    l_thumb.filled = True
    window.add(l_thumb)

    r_hand = GRect(60, 15, x=505, y=620)
    r_hand.filled = True
    r_hand.fill_color = 'yellow'
    r_hand.color = 'yellow'
    window.add(r_hand)
    r_thumb_1 = GOval(11, 32, x=560, y=605)
    r_thumb_1.filled = True
    window.add(r_thumb_1)
    r_thumb_2 = GOval(22, 24, x=560, y=616)
    r_thumb_2.filled = True
    window.add(r_thumb_2)


def add_body():
    # The body, pants, legs, shoes and pocket of the minion; a part of the function -- "draw_minion()"
    body = GRect(160, 160, x=345, y=520)
    body.filled = True
    body.fill_color = 'yellow'
    body.color = 'yellow'
    window.add(body)
    bottom = GOval(160, 80, x=345, y=640)
    bottom.filled = True
    bottom.fill_color = 'blue'
    bottom.color = 'blue'
    window.add(bottom)
    pants = GRect(160, 60, x=345, y=620)
    pants.filled = True
    pants.fill_color = 'blue'
    pants.color = 'blue'
    window.add(pants)

    left_leg = GRect(40, 60, x=380, y=680)
    left_leg.filled = True
    left_leg.fill_color = 'blue'
    left_leg.color = 'blue'
    window.add(left_leg)
    right_leg = GRect(40, 60, x=440, y=680)
    right_leg.filled = True
    right_leg.fill_color = 'blue'
    right_leg.color = 'blue'
    window.add(right_leg)

    left_shoe = GOval(60, 30, x=365, y=735)
    left_shoe.filled = True
    window.add(left_shoe)
    right_shoe = GOval(60, 30, x=430, y=735)
    right_shoe.filled = True
    window.add(right_shoe)

    pocket_circle = GOval(70, 50, x=390, y=640)
    pocket_circle.filled = True
    pocket_circle.fill_color = 'blue'
    pocket_circle.color = 'darkblue'
    window.add(pocket_circle)
    pocket_rect = GRect(70, 30, x=390, y=635)
    pocket_rect.filled = True
    pocket_rect.fill_color = 'blue'
    pocket_rect.color = 'darkblue'
    window.add(pocket_rect)
    pocket_circle_cover = GOval(69, 49, x=389.5, y=639.5)
    pocket_circle_cover.filled = True
    pocket_circle_cover.fill_color = 'blue'
    pocket_circle_cover.color = 'blue'
    window.add(pocket_circle_cover)


def add_eyes():
    # glasses and eyes of minion; a part of the function -- "draw_minion()"
    l_belt = GRect(20, 14, x=345, y=520)
    l_belt.filled = True
    window.add(l_belt)

    r_belt = GRect(20, 14, x=485, y=520)
    r_belt.filled = True
    window.add(r_belt)

    l_glasses = GOval(63, 63, x=363, y=495)
    l_glasses.filled = True
    l_glasses.fill_color = 'gray'
    window.add(l_glasses)
    r_glasses = GOval(62, 62, x=426, y=495)
    r_glasses.filled = True
    r_glasses.fill_color = 'gray'
    window.add(r_glasses)

    l_eye = GOval(42, 42, x=373, y=505)
    l_eye.filled = True
    l_eye.fill_color = 'white'
    window.add(l_eye)
    r_eye = GOval(42, 42, x=436, y=505)
    r_eye.filled = True
    r_eye.fill_color = 'white'
    window.add(r_eye)

    l_eyeball = GOval(16, 16, x=384.5, y=516.5)
    l_eyeball.filled = True
    window.add(l_eyeball)
    r_eyeball = GOval(16, 16, x=447.5, y=516.5)
    r_eyeball.filled = True
    window.add(r_eyeball)


def face_mask():
    # Minion's face mask; a part of the function -- "draw_minion()"
    mask = GRect(125, 52, x=362, y=560)
    mask.filled = True
    mask.fill_color = 'pink'
    mask.color = 'gold'
    window.add(mask)

    mask_shape_upper_l = GPolygon()
    mask_shape_upper_l.add_vertex((362, 560))
    mask_shape_upper_l.add_vertex((362, 565))
    mask_shape_upper_l.add_vertex((426, 560))
    mask_shape_upper_l.filled = True
    mask_shape_upper_l.fill_color = 'yellow'
    mask_shape_upper_l.color = 'yellow'
    window.add(mask_shape_upper_l)

    mask_shape_upper_r = GPolygon()
    mask_shape_upper_r.add_vertex((426, 560))
    mask_shape_upper_r.add_vertex((487, 565))
    mask_shape_upper_r.add_vertex((487, 560))
    mask_shape_upper_r.filled = True
    mask_shape_upper_r.fill_color = 'yellow'
    mask_shape_upper_r.color = 'yellow'
    window.add(mask_shape_upper_r)

    mask_shape_lower_l = GPolygon()
    mask_shape_lower_l.add_vertex((362, 612))
    mask_shape_lower_l.add_vertex((426, 612))
    mask_shape_lower_l.add_vertex((426, 617))
    mask_shape_lower_l.filled = True
    mask_shape_lower_l.fill_color = 'pink'
    mask_shape_lower_l.color = 'pink'
    window.add(mask_shape_lower_l)

    mask_shape_lower_r = GPolygon()
    mask_shape_lower_r.add_vertex((426, 612))
    mask_shape_lower_r.add_vertex((487, 612))
    mask_shape_lower_r.add_vertex((426, 617))
    mask_shape_lower_r.filled = True
    mask_shape_lower_r.fill_color = 'pink'
    mask_shape_lower_r.color = 'pink'
    window.add(mask_shape_lower_r)

    rope_1 = GLine(345, 565, 365, 575)
    rope_1.filled = True
    rope_1.color = 'pink'
    #rope_1.line_width = '3'
    window.add(rope_1)

    rope_2 = GLine(345, 612, 365, 607)
    rope_2.filled = True
    rope_2.color = 'pink'
    window.add(rope_2)

    rope_3 = GLine(485, 575, 505, 565)
    rope_3.filled = True
    rope_3.color = 'pink'
    window.add(rope_3)

    rope_4 = GLine(485, 607, 505, 612)
    rope_4.filled = True
    rope_4.color = 'pink'
    window.add(rope_4)


if __name__ == '__main__':
    main()
