import random
from kivy.config import Config
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import ObjectProperty

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')

ingredients = []

class FoodFactoryApp(App):   
    
    def build(self):
        game = FoodFactoryGame()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game

class FoodPaddle(Widget):
    
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            pass
            

class WindowSeparator(Widget):
    def test(self):
        pass

class FoodFactoryGame(Widget):
    
    paddle = ObjectProperty(None)
    separator = ObjectProperty(None)
    
    def update(self, dt):
        pass

    def on_touch_down(self, touch):
        if 'button' in touch.profile :
            if touch.button == 'left':
                if touch.x + self.paddle.width / 2 >= self.separator.x :
                    self.paddle.x = self.separator.x - self.paddle.width
                elif touch.x - self.paddle.width / 2 <= 0:
                    self.paddle.x = 0
                else :
                    self.paddle.center_x = touch.x
            elif touch.button == 'scroll':
                ingredients.append(FoodIngredient())
                
    
    def on_touch_move(self, touch):
        if 'button' in touch.profile and touch.button == 'left':            
            if touch.x + self.paddle.width / 2 >= self.separator.x :
                self.paddle.x = self.separator.x - self.paddle.width
            elif touch.x - self.paddle.width / 2 <= 0:
                self.paddle.x = 0
            else :
                self.paddle.center_x = touch.x
        
    
class FoodIngredient(Widget):    
    def __init__(self):
        super(FoodIngredient, self).__init__()
        x = random.random() * (800 - self.width)
        y = 600
        self.pos = (x, y)    
       
        

if __name__ == '__main__':
    FoodFactoryApp().run()
