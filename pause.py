import pyglet

from gamestate import GameState, PAUSE_STATE_ID

class PauseState(GameState):
    def __init__(self, window):
        self.label = pyglet.text.Label('Paused',
                                  font_name='Times New Roman',
                                  font_size=36,
                                  x=window.width//2, y=window.height//2,
                                  color=(155, 55, 24, 255),
                                  anchor_x='center', anchor_y='center')
        self.id = PAUSE_STATE_ID

    def on_draw(self):
        self.label.draw()

    def update(self, keys_pressed, dt):
        pass

    
