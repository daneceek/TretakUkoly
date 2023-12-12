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
class Spaceobject():
    speed_x = 0 #rychlost ve směru osy x
    speed_y = 0
    speed_koef = 1
    
    def __init__(self, image_path, speed_x=0, speed_y=0, batch = None, position_x=None, position_y=None, speed_koef=speed_koef):
        
        self.speed_koef = speed_koef
        
        self.img = pyglet.image.load(image_path)
        # super().__init__(img=self.img, batch = batch)
        # self.img.anchor_x = self.img.width // 2
        # self.img.anchor_y = self.img.height // 2
        
        self.sprite = pyglet.sprite.Sprite(self.img, batch = batch)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.sprite.x = position_x
        self.sprite.y = position_y
    def move(self, dt:float):
        self.sprite.x += self.speed_x * dt * 10 * self.speed_koef
        self.sprite.y += self.speed_y * dt * 10 * self.speed_koef
    
        
# class Meteor(Spaceobject):
    
#     def __init__(self, speed_x, speed_y, position_x, position_y, batch ,image_path="img/meteorBrown_big1.png", speed_koef=None):
#         self.speed_x = speed_x
#         self.speed_y = speed_y
#         self.speed_koef = speed_koef
#         super().__init__(image_path, speed_x= self.speed_x,speed_y=self.speed_y,  position_x=position_x, position_y=position_y, batch = batch, speed_koef=self.speed_koef) #zavolej toho předka 
        

class GreyMeteor(Spaceobject):
    
    
    def __init__(self,position_x, position_y, batch):
        
        self.speed_x = random.randint(-10,10)
        self.speed_y = random.randint(-10,10)
        super().__init__(image_path = "img/meteorGrey_big1.png", speed_x= self.speed_x,speed_y=self.speed_y,  position_x=position_x, position_y=position_y, batch = batch, speed_koef=2)

class BrownMeteor(Spaceobject):
    speed_koef = 1
    def __init__(self, position_x, position_y, batch):
        self.speed_y = random.randint(-10,10)
        self.speed_x = random.randint(-10,10)
    
        super().__init__(image_path = "img/meteorBrown_big1.png", speed_x= self.speed_x,speed_y=self.speed_y,  position_x=position_x, position_y=position_y, batch = batch)



meteor1 = BrownMeteor(500, 600, batch)
meteor2 = BrownMeteor(120, 600, batch)
meteor3 = GreyMeteor(500, 100, batch)

# bubble1 = Bubble(random.randint(0,20), random.randint(0,20), 500, 100, batch)
# bubble2 = Bubble(random.randint(0,20), random.randint(0,20), 120, 308, batch)
# bubble3 = Bubble(random.randint(0,20), random.randint(0,20), 700, 200, batch)
# bubble = Spaceobject("img/bubble.png", 4, 8)
# bubble2 = Spaceobject("img/meteorGrey_med2.png", 8, 16)
# objekty = []
# for _ in range(22):
#     o = Spaceobject(random.choice(glob.glob("img/*.png")), random.randint(0, 20), random.randint(0, 20))
#     objekty.append(o)


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
    # bubble.x = x
    # bubble.y = y


def tick(dt):
    meteor1.move(dt)
    meteor2.move(dt)
    meteor3.move(dt)
    
    # bubble1.move(dt)
    # bubble2.move(dt)
    # bubble3.move(dt)
    # bubble.move(dt)
    # meteor1.move(dt)
    # bubble.move(dt)
    # for o in objekty:
    #     o.move(dt)
    # print(dt)


# funkce tick se spustí 30x za sekundu
pyglet.clock.schedule_interval(tick, 1 / 30)

# nekonečná smyčka ve které se čeká na události, které se následně obsluhují
pyglet.app.run()

