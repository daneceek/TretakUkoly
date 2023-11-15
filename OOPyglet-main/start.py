#!/usr/bin/env python3
# Soubor:  kameny.py
# Datum:   06.11.2018 10:01
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
############################################################################
import pyglet
import random
import glob


# from pyglet.window.key import LEFT, RIGHT, UP, DOWN, LCTRL
# from pyglet.window.mouse import LEFT as MouseLEFT

import pyglet.window.key
import pyglet.window.mouse

window = pyglet.window.Window(width=1500, height=800)
batch = pyglet.graphics.Batch()  # pro optimalizované vyreslování objektů


class Spaceobject(object):
    speed_x = 0 #rychlost ve směru osy x
    speed_y = 0
    def __init__(self, image_path, speed_x=0, speed_y=0):
          
        self.speed_x = speed_x
        self.speed_y = speed_y

        self.img = pyglet.image.load(image_path)
        self.img.anchor_x = self.img.width // 2
        self.img.anchor_y = self.img.height // 2

        self.sprite = pyglet.sprite.Sprite(self.img, batch = batch)
  
    def move(self, dt:float):
        self.sprite.x += self.speed_x * dt * 10
        self.sprite.y += self.speed_y * dt * 10


suter = Spaceobject("img/meteorBrown_big1.png", 10, 4)
bubble = Spaceobject("img/bubble.png", 4, 8)
bubble2 = Spaceobject("img/meteorGrey_med2.png", 8, 16)
objekty = []
for _ in range(22):
    o = Spaceobject(random.choice(glob.glob("img/*.png")), random.randint(0, 20), random.randint(0, 20))
    objekty.append(o)


@window.event
def on_draw():
    window.clear()
    batch.draw()


@window.event
def on_key_press(sym, mod):
    print(sym, mod)


@window.event
def on_key_release(sym, mod):
    print(sym, mod)


@window.event
def on_mouse_press(x, y, button, mod):
    print(x, y, button)
    bubble.x = x
    bubble.y = y


def tick(dt):
    bubble.move(dt)
    suter.move(dt)
    bubble2.move(dt)
    for o in objekty:
        o.move(dt)
    # print(dt)


# funkce tick se spustí 30x za sekundu
pyglet.clock.schedule_interval(tick, 1 / 30)

# nekonečná smyčka ve které se čeká na události, které se následně obsluhují
pyglet.app.run()

