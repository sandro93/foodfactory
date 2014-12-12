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

from ingredients import Ingredient

from pyglet.gl import *
from consts import config, WINDOW_W, WINDOW_H, SEP_BAR_W, STATUSBAR_W, STATUSBAR_H, GAMEAREA_W, GAMEAREA_H, STATUSBAR_X, GAMEAREA_CENTER_X, GAMEAREA_CENTER_Y, PLATE_SPEED, PLATE_IMG


window = pyglet.window.Window(WINDOW_W, WINDOW_H)

keys_pressed = []

@window.event
def on_key_press(key, modifiers):
    if key == pyglet.window.key.SPACE:
        balls.append(Ingredient())
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
        ball.update(dt, plate)
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
