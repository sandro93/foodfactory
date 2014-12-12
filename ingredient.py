import pyglet

from consts import GAMEAREA_W, GAMEAREA_W

class Ingredient(pyglet.sprite.Sprite):
    def __init__(self, image, collect_sound, drop_sound):
        ball_image = pyglet.resource.image(image)
        self.width = ball_image.width
        self.height = ball_image.height
        x = random.random() * (GAMEAREA_W - self.width)
        y = GAMEAREA_H - self.height

        super(Ingredient, self).__init__(self.ball_image, x, y, batch=balls_batch)
        self.collect_sound = pyglet.resource.media(collect_sound, streaming=False)
        self.drop_sound = pyglet.resource.media(drop_sound, streaming=False)
        self.dy = 1 * 300
        self.is_collected = False

    def collect(self):
        self.set_position(chef.x, chef.y + chef.height + 10)
        self.is_collected = True

    def update(self, dt, plate):
        if not self.is_collected:
            if self.y + self.height <= plate.height:
                if self.x >= plate.x and self.x <= plate.x + plate.width:
                    self.collect_sound.play()
                    balls[-1].collect()
                else:
                    self.drop_sound.play()
                    del balls[-1]
            self.y -= self.dy * dt
