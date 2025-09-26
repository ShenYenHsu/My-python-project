"""
File: my_drawing.py
Name: Shane
----------------------
In this program, it draws a Stitch with a sealing mouth.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


def main():
    """
    Title: Stitch

    Hi! It;s Stitch here! I'm from different planet! I love the food on earth so much! I can't help but eating all the
    food from Shane, so he temporally sealed my mouth...
    """
    window = GWindow(width=800, height=400, title='Stitch')
    onmouseclicked(mouse_position)
    # ears
    l_ear = set_up_l_ear()
    l_ear1 = set_up_l_ear1()
    l_ear2 = set_up_l_ear2()
    l_ear3 = set_up_l_ear3()
    r_ear = set_up_r_ear()
    r_ear1 = set_up_r_ear1()
    r_ear2 = set_up_r_ear2()
    r_ear3 = set_up_r_ear3()
    window.add(r_ear, x=445, y=90)
    window.add(r_ear1)
    window.add(r_ear2)
    window.add(r_ear3, x=461, y=150)
    window.add(l_ear, x=295, y=90)
    window.add(l_ear1)
    window.add(l_ear2)
    window.add(l_ear3, x=325, y=150)
    # head
    head = set_up_head()
    head2 = set_up_head2()
    head3 = set_up_head3()
    jaw = set_up_jaw()
    hair = set_up_hair()
    hair1 = set_up_hair1()
    hair2 = set_up_hair2()
    hair3 = set_up_hair3()
    window.add(head, x=window.width//2-head.width//2, y=window.height//2-head.height//2-20)
    window.add(jaw, x=window.width//2-jaw.width//2, y=window.height//2-jaw.height//2)
    window.add(head2, x=window.width//2 - head2.width, y=window.height//2 - head2.height//2 - 15)
    window.add(head3, x=window.width//2, y=window.height//2 - head3.height//2 - 15)
    window.add(hair, x=window.width//2-hair.width//2, y=120)
    window.add(hair1)
    window.add(hair2, x=window.width//2+2, y=110)
    window.add(hair3, x=window.width//2+8, y=122)
    # eyes
    l_eye = set_up_l_eye()
    l_eye1 = set_up_l_eye1()
    l_eye2 = set_up_l_eye2()
    l_eye3 = set_up_l_eye3()
    l_eye4 = set_up_l_eye4()
    l_eye5 = set_up_l_eye5()
    l_eye6 = set_up_l_eye6()
    l_eye7 = set_up_l_eye7()

    r_eye = set_up_r_eye()
    r_eye1 = set_up_r_eye1()
    r_eye2 = set_up_r_eye2()
    r_eye3 = set_up_r_eye3()
    r_eye4 = set_up_r_eye4()
    r_eye5 = set_up_r_eye5()
    r_eye6 = set_up_r_eye6()
    # r_eye7 = set_up_r_eye7()
    window.add(l_eye, x=window.width//2-60, y=185)
    window.add(l_eye1, x=window.width//2-60, y=170)
    window.add(l_eye2, x=window.width//2-58, y=165)
    window.add(l_eye3, x=window.width//2-50, y=155)
    window.add(l_eye4, x=window.width//2-52, y=150)
    window.add(l_eye5)
    window.add(l_eye6, x=window.width//2-47, y=170)
    window.add(l_eye7, x=window.width//2-34, y=175)
    window.add(r_eye, x=window.width//2+14, y=185)
    window.add(r_eye1, x=window.width//2+22, y=170)
    window.add(r_eye2, x=window.width//2+38, y=165)
    window.add(r_eye3, x=window.width//2+34, y=155)
    window.add(r_eye4, x=window.width//2+14, y=150)
    window.add(r_eye5, x=window.width//2+20, y=170)
    window.add(r_eye6, x=window.width//2+25, y=175)

    # nose
    nose = GOval(25, 20)
    nose.filled = True
    nose.fill_color = 'steelblue'
    nose.color = 'steelblue'
    window.add(nose, x=window.width//2-13, y=200)

    # mouth
    mouth = set_up_mouth()
    mouth1 = set_up_mouth()
    mouth2 = set_up_mouth()
    mouth3 = set_up_mouth()
    mouth4 = set_up_mouth4()
    mouth5 = set_up_mouth5()
    window.add(mouth, x=375, y=235)
    window.add(mouth1, x=375+mouth.width+3, y=235)
    window.add(mouth2, x=mouth1.x+mouth.width+3, y=235)
    window.add(mouth3, x=mouth2.x+mouth.width+3, y=235)
    window.add(mouth4, x=mouth3.x+8, y=235)
    window.add(mouth5, x=mouth4.x+2, y=243)


def set_up_mouth5():
    oval = GOval(4, 4)
    oval.filled = True
    oval.fill_color = 'white'
    oval.color = 'white'
    return oval


def set_up_mouth4():
    oval = GOval(8, 15)
    oval.filled = True
    oval.fill_color = 'gray'
    oval.color = 'gray'
    return oval


def set_up_mouth():
    rect = GRect(10, 3)
    rect.filled = True
    rect.fill_color = 'gray'
    rect.color = 'gray'
    return rect


def set_up_r_eye():
    r_eye = GArc(46, 35, 200, 200)
    r_eye.filled = True
    r_eye.fill_color = 'lightblue'
    r_eye.color = 'lightblue'
    return r_eye


def set_up_r_eye1():
    r_eye1 = GArc(60, 70, 105, -120)
    r_eye1.filled = True
    r_eye1.fill_color = 'lightblue'
    r_eye1.color = 'lightblue'
    return r_eye1


def set_up_r_eye2():
    r_eye2 = GArc(40, 60, 90, -120)
    r_eye2.filled = True
    r_eye2.fill_color = 'lightblue'
    r_eye2.color = 'lightblue'
    return r_eye2


def set_up_r_eye3():
    r_eye3 = GArc(30, 40, 90, -110)
    r_eye3.filled = True
    r_eye3.fill_color = 'lightblue'
    r_eye3.color = 'lightblue'
    return r_eye3


def set_up_r_eye4():
    r_eye4 = GArc(50, 120, 60, 142)
    r_eye4.filled = True
    r_eye4.fill_color = 'lightblue'
    r_eye4.color = 'lightblue'
    return r_eye4


def set_up_r_eye5():
    r_eye5 = GOval(28, 35)
    r_eye5.filled = True
    r_eye5.fill_color = 'steelblue'
    r_eye5.color = 'steelblue'
    return r_eye5


def set_up_r_eye6():
    r_eye6 = GOval(10, 10)
    r_eye6.filled = True
    r_eye6.fill_color = 'white'
    r_eye6.color = 'white'
    return r_eye6


def set_up_l_eye():
    l_eye = GArc(46, 35, -20, -200)
    l_eye.filled = True
    l_eye.fill_color = 'lightblue'
    l_eye.color = 'lightblue'
    return l_eye


def set_up_l_eye1():
    l_eye1 = GArc(60, 70, 75, 120)
    l_eye1.filled = True
    l_eye1.fill_color = 'lightblue'
    l_eye1.color = 'lightblue'
    return l_eye1


def set_up_l_eye2():
    l_eye2 = GArc(40, 60, 90, 120)
    l_eye2.filled = True
    l_eye2.fill_color = 'lightblue'
    l_eye2.color = 'lightblue'
    return l_eye2


def set_up_l_eye3():
    l_eye3 = GArc(30, 40, 90, 110)
    l_eye3.filled = True
    l_eye3.fill_color = 'lightblue'
    l_eye3.color = 'lightblue'
    return l_eye3


def set_up_l_eye4():
    l_eye4 = GArc(50, 120, 120, -142)
    l_eye4.filled = True
    l_eye4.fill_color = 'lightblue'
    l_eye4.color = 'lightblue'
    return l_eye4


def set_up_l_eye5():
    l_eye5 = GPolygon()
    l_eye5.add_vertex((351, 165))
    l_eye5.add_vertex((350, 202))
    l_eye5.add_vertex((375, 201))
    l_eye5.add_vertex((363, 164))
    l_eye5.filled = True
    l_eye5.fill_color = 'lightblue'
    l_eye5.color = 'lightblue'
    return l_eye5


def set_up_l_eye6():
    l_eye6 = GOval(28, 35)
    l_eye6.filled = True
    l_eye6.fill_color = 'steelblue'
    l_eye6.color = 'steelblue'
    return l_eye6


def set_up_l_eye7():
    l_eye7 = GOval(10, 10)
    l_eye7.filled = True
    l_eye7.fill_color = 'white'
    l_eye7.color = 'white'
    return l_eye7


def set_up_r_ear():
    r_ear = GArc(90, 115, 110, -220)
    r_ear.filled = True
    r_ear.fill_color = 'lightpink'
    r_ear.color = 'lightpink'
    return r_ear


def set_up_r_ear1():
    r_ear1 = GPolygon()
    r_ear1.add_vertex((468, 180))
    r_ear1.add_vertex((470, 153))
    r_ear1.add_vertex((466, 125))
    r_ear1.add_vertex((464, 110))
    r_ear1.add_vertex((461, 108))
    r_ear1.add_vertex((461, 98))
    r_ear1.add_vertex((463, 96))
    r_ear1.add_vertex((465, 92))
    r_ear1.add_vertex((480, 148))
    r_ear1.filled = True
    r_ear1.fill_color = 'lightpink'
    r_ear1.color = 'lightpink'
    return r_ear1


def set_up_r_ear2():
    r_ear2 = GPolygon()
    r_ear2.add_vertex((488, 120))
    r_ear2.add_vertex((498, 109))
    r_ear2.add_vertex((503, 124))
    r_ear2.filled = True
    r_ear2.fill_color = 'ghostwhite'
    r_ear2.color = 'ghostwhite'
    return r_ear2


def set_up_r_ear3():
    r_ear3 = GArc(30, 60, 75, -140)
    r_ear3.filled = True
    r_ear3.fill_color = 'lightsteelblue'
    r_ear3.color = 'lightsteelblue'
    return r_ear3


def set_up_l_ear():
    l_ear = GArc(90, 115, 70, 220)
    l_ear.filled = True
    l_ear.fill_color = 'lightpink'
    l_ear.color = 'lightpink'
    return l_ear


def set_up_l_ear1():
    l_ear1 = GPolygon()
    l_ear1.add_vertex((333, 181))
    l_ear1.add_vertex((331, 149))
    l_ear1.add_vertex((335, 125))
    l_ear1.add_vertex((336, 110))
    l_ear1.add_vertex((338, 104))
    l_ear1.add_vertex((338, 100))
    l_ear1.add_vertex((335, 96))
    l_ear1.add_vertex((324, 148))
    l_ear1.filled = True
    l_ear1.fill_color = 'lightpink'
    l_ear1.color = 'lightpink'
    return l_ear1


def set_up_l_ear2():
    l_ear2 = GPolygon()
    l_ear2.add_vertex((310, 120))
    l_ear2.add_vertex((299, 113))
    l_ear2.add_vertex((298, 125))
    l_ear2.filled = True
    l_ear2.fill_color = 'ghostwhite'
    l_ear2.color = 'ghostwhite'
    return l_ear2


def set_up_l_ear3():
    l_ear3 = GArc(30, 60, 105, 140)
    l_ear3.filled = True
    l_ear3.fill_color = 'lightsteelblue'
    l_ear3.color = 'lightsteelblue'
    return l_ear3


def set_up_head():
    head = GOval(110, 100)
    head.filled = True
    head.fill_color = 'lightsteelblue'
    head.color = 'lightsteelblue'
    return head


def set_up_head2():
    head2 = GArc(130, 150, 100, 80)
    head2.filled = True
    head2.fill_color = 'lightsteelblue'
    head2.color = 'lightsteelblue'
    return head2


def set_up_head3():
    head3 = GArc(130, 150, 0, 80)
    head3.filled = True
    head3.fill_color = 'lightsteelblue'
    head3.color = 'lightsteelblue'
    return head3


def set_up_jaw():
    jaw = GOval(150, 100)
    jaw.filled = True
    jaw.fill_color = 'lightsteelblue'
    jaw.color = 'lightsteelblue'
    return jaw


def set_up_hair():
    hair = GArc(75, 50, 70, 40)
    hair.filled = True
    hair.fill_color = 'lightsteelblue'
    hair.color = 'lightsteelblue'
    return hair


def set_up_hair1():
    hair1 = GPolygon()
    hair1.add_vertex((394, 132))
    hair1.add_vertex((396, 122))
    hair1.add_vertex((402, 131))
    hair1.filled = True
    hair1.fill_color = 'lightsteelblue'
    hair1.color = 'lightsteelblue'
    return hair1


def set_up_hair2():
    hair2 = GArc(35, 90, 70, 100)
    hair2.filled = True
    hair2.fill_color = 'lightsteelblue'
    hair2.color = 'lightsteelblue'
    return hair2


def set_up_hair3():
    hair3 = GArc(35, 50, 50, 100)
    hair3.filled = True
    hair3.fill_color = 'lightsteelblue'
    hair3.color = 'lightsteelblue'
    return hair3


def mouse_position(mouse):
    """This program is to help the coder to locate the position"""
    print(mouse.x, mouse.y)


if __name__ == '__main__':
    main()
