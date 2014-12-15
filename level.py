import pyglet
import random
from consts import GAMEAREA_W, GAMEAREA_H


class Level:
    ingredients = []
    
    def __init__(self, dish_image, ingredients, dish_states):
#        self.ingredients.append(Ingredient('carrot.png', 1, 1, [0, 1], None, None))
        self.dish_image = dish_image
        self.ingredients = ingredients
        self.dish_states = dish_states
        self.total_steps = 0
        
        for ing in self.ingredients:
            if len(ing.steps):
                self.total_steps += 1



class Ingredient(pyglet.sprite.Sprite):
    def __init__(self, image, ingredient_id, group, steps, collect_sound = 'collect.wav', drop_sound = 'drop.wav'):
        print("Image = {0}, ingredient_id = {1}, group = {2}, steps = {3}".format(image, ingredient_id, group, steps))
        self.steps = steps
        self.ingredient_id = ingredient_id
        self.grp = group
        ingredient_image = pyglet.resource.image(image)
        # self.width = ingredient_image.width
        # self.height = ingredient_image.height
        x = random.random() * (GAMEAREA_W - ingredient_image.width)
        y = GAMEAREA_H - ingredient_image.height
        super(Ingredient, self).__init__(ingredient_image, x, y)

        #super(Ingredient, self).__init__(self.ingredient_image, x, y, batch=balls_batch)

        self.collect_sound = pyglet.resource.media(collect_sound, streaming=False)
        self.drop_sound = pyglet.resource.media(drop_sound, streaming=False)
        self.dy = 1 * 300
        self.is_collected = False

##    def collect(self):
##        self.set_position(chef.x, chef.y + chef.height + 10)
##        self.is_collected = True

##    def update(self, dt, plate):
##        if not self.is_collected:
##            if self.y + self.height <= plate.height:
##                if self.x >= plate.x and self.x <= plate.x + plate.width:
##                    self.collect_sound.play()
##                    balls[-1].collect()
##                else:
##                    self.drop_sound.play()
##                    del balls[-1]
##            self.y -= self.dy * dt

class DishState():
    def __init__(self, image, ingredient_ids):
        self.image = image
        self.ingredient_ids = ingredient_ids
