#!/bin/env python3
'''
Bounces balls around a window and plays noises.

This is a simple demonstration of how pyglet efficiently manages many sound
channels without intervention.

'''

import os
import random
import sys
import math
import pyglet

from pyglet.gl import *
from consts import config, WINDOW_W, WINDOW_H, SEP_BAR_W, STATUSBAR_W, STATUSBAR_H, GAMEAREA_W, GAMEAREA_H, STATUSBAR_X, GAMEAREA_CENTER_X, GAMEAREA_CENTER_Y, PLATE_SPEED, PLATE_IMG                


##WINDOW_W = 800
##WINDOW_H = 600
##
##STATUSBAR_W = WINDOW_W // 4
##STATUSBAR_H = WINDOW_H
##SEP_BAR_W = 1
##GAMEAREA_W = WINDOW_W - STATUSBAR_W - SEP_BAR_W
##GAMEAREA_H = WINDOW_H
##
##
##STATUSBAR_X = GAMEAREA_W + SEP_BAR_W
##
##GAMEAREA_CENTER_X = WINDOW_W / 2
##GAMEAREA_CENTER_Y = WINDOW_H / 2
##
##PLATE_SPEED = 10
##
##INGREDIENT1_IMG = 'ingredient1.png'
##PLATE_IMG = 'plate.png'
##CHEF_IMG = 'chef.png'
##
##FOOD_DROP = 'drop.wav'
##COLLECT_SOUND = 'collect.wav'

window = pyglet.window.Window(WINDOW_W, WINDOW_H)

keys_pressed = []

class Plate(pyglet.sprite.Sprite):
    plate_img = pyglet.resource.image(PLATE_IMG)
    width = plate_img.width
    height = plate_img.height

    def __init__(self):
        x = GAMEAREA_CENTER_X - self.width // 2
        y = 0
        dx = PLATE_SPEED
        super(Plate, self).__init__(self.plate_img, x, y)
        self.collect_sound = pyglet.resource.media(COLLECT_SOUND, streaming=False)

    def update(self, keys_pressed, dt):
        rect_x, rect_y = math.ceil(self.position[0]), 0
        if len(keys_pressed) > 0:
            if  keys_pressed[0] == pyglet.window.key.LEFT:
                if rect_x >= 0 :
                    if rect_x > PLATE_SPEED:
                        self.dx = PLATE_SPEED
                    else :
                        self.dx = rect_x
                self.x -= self.dx
            elif keys_pressed[0] == pyglet.window.key.RIGHT:
                if rect_x + self.width < GAMEAREA_W :
                    if GAMEAREA_W - (rect_x + self.width) > PLATE_SPEED :
                        self.dx = PLATE_SPEED
                    else :
                        self.dx = GAMEAREA_W - (rect_x + self.width)
                    self.x += self.dx

class Ball(pyglet.sprite.Sprite):
    ball_image = pyglet.resource.image(INGREDIENT1_IMG)
    width = ball_image.width
    height = ball_image.height

    def __init__(self):
        x = random.random() * (GAMEAREA_W - self.width)
        y = random.random() * (GAMEAREA_H - self.height)

        super(Ball, self).__init__(self.ball_image, x, y, batch=balls_batch)
        self.collect_sound = pyglet.resource.media(COLLECT_SOUND, streaming=False)
        self.drop_sound = pyglet.resource.media(FOOD_DROP, streaming=False)
        self.dy = 1 * 300
        self.is_collected = False

    def collect(self):
        self.set_position(chef.x, chef.y + chef.height + 10)
        self.is_collected = True

    def update(self, dt):
        if not self.is_collected:
            if self.y + self.height <= plate.height:
                if self.x >= plate.x and self.x <= plate.x + plate.width:
                    self.collect_sound.play()
                    balls[-1].collect()
                else:
                    self.drop_sound.play()
                    del balls[-1]
            self.y -= self.dy * dt



def draw_status_bar():
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                         ('v2i', (STATUSBAR_X, 0, STATUSBAR_X, STATUSBAR_H)))

@window.event
def on_key_press(key, modifiers):
    if key == pyglet.window.key.SPACE:
        balls.append(Ball())
    elif key == pyglet.window.key.ESCAPE:
        window.has_exit = True
    elif key in (pyglet.window.key.LEFT, pyglet.window.key.RIGHT):
        keys_pressed.append(key)

@window.event
def on_key_release(key, modifiers):
    if key in (pyglet.window.key.LEFT, pyglet.window.key.RIGHT):
        keys_pressed.remove(key)

@window.event
def on_draw():
    window.clear()
    glClearColor(1, 1, 1, 1)
    glColor3f(1, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_status_bar()
    plate.draw()
    balls_batch.draw()
    label.draw()
    chef.draw()
    

def update(dt):
    for ball in balls:
        ball.update(dt)
    plate.update(keys_pressed, dt)

pyglet.clock.schedule_interval(update, 1/30.)

balls_batch = pyglet.graphics.Batch()
balls = []
plate = Plate()
chef_img = pyglet.resource.image(CHEF_IMG)
chef = pyglet.sprite.Sprite(chef_img, x=(STATUSBAR_X + STATUSBAR_W // 2), y=10)
label = pyglet.text.Label('Dish',
                          font_size=14,
                          x=STATUSBAR_X + STATUSBAR_W // 2, y=STATUSBAR_H - 100,
                          anchor_x='center')
# setup()

if __name__ == '__main__':
    pyglet.app.run()
