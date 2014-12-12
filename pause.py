from gamestate import GameState

class PauseState(GameState):
    def __init__(self):
        self.label = pyglet.text.Label('Paused',
                                  font_name='Times New Roman',
                                  font_size=36,
                                  x=window.width//2, y=window.height//2,
                                  anchor_x='center', anchor_y='center')

    def on_draw():
        self.label.draw()

    
