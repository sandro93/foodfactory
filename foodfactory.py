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

from ingredient import Ingredient

from pyglet.gl import *
from consts import config, WINDOW_W, WINDOW_H, SEP_BAR_W, STATUSBAR_W, STATUSBAR_H, GAMEAREA_W, GAMEAREA_H, STATUSBAR_X, GAMEAREA_CENTER_X, GAMEAREA_CENTER_Y, PLATE_SPEED, PLATE_IMG

import gamestate
from gameplay import PlayState
from pause import PauseState

state = None

window = pyglet.window.Window(WINDOW_W, WINDOW_H)
state = PauseState(window)

keys_pressed = []

@window.event
def on_key_press(key, modifiers):
    #if state.id == gamestate.PAUSE_STATE_ID:
    if key == pyglet.window.key.SPACE:
        # balls.append(Ingredient())
        # state = PlayState()
        global state
        state = PlayState(window)

    elif key == pyglet.window.key.ESCAPE:
        window.has_exit = True
    elif key in (pyglet.window.key.LEFT, pyglet.window.key.RIGHT):
            keys_pressed.append(key)

@window.event
def on_key_release(key, modifiers):
    if state.id == gamestate.PAUSE_STATE_ID:
        if key in (pyglet.window.key.LEFT, pyglet.window.key.RIGHT):
            keys_pressed.remove(key)

@window.event
def on_draw():
    window.clear()
    glClearColor(1, 1, 1, 1)
    glColor3f(1, 0, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    balls_batch.draw()
    state.on_draw()

def update(dt):
    for ball in balls:
        ball.update(dt, plate)
    state.update(keys_pressed, dt)

pyglet.clock.schedule_interval(update, 1/60.)

balls_batch = pyglet.graphics.Batch()
balls = []
label = pyglet.text.Label('Dish',
                          font_size=14,
                          x=STATUSBAR_X + STATUSBAR_W // 2, y=STATUSBAR_H - 100,
                          anchor_x='center')
# setup()

if __name__ == '__main__':
    pyglet.app.run()
