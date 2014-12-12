from gamestate import GameState

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


class PlayState(GameState):
    def on_draw():
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
                         ('v2i', (STATUSBAR_X, 0, STATUSBAR_X, STATUSBAR_H)))
        plate.draw()
        
