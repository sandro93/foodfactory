import xml.etree.ElementTree as ET
import level
import pprint
import os

class LevelParser:
    def __init__(self, level_file):
        self.tree = ET.parse(level_file)
        self.root = self.tree.getroot()
        
    def _obtain_ingredients(self, elem):
        ingredients = []
        for ing in elem:
            print("Count in ing = " + str(len(ing)))
            name = None
            image = None
            steps = []
            ingredient_id = ing.get('id')
            group = ing.get('group')
            for child in ing:
                if child.tag == 'name':
                    name = child.text
                elif child.tag == 'image':
                    image = child.text
                elif child.tag == 'steps':
                    for step in child:
                        steps.append(step.text)
            print(image)
            print(os.getcwd())
            # ingredient = level.Ingredient(image, ingredient_id, group, steps)
            # ingredients.append(ingredient)
        return ingredients

    def _obtain_dish_image(self, elem):
        return elem.text
        

    def _obtain_dish_states(self, elem):
        dish_states = []
        for dish_state in elem:
            image = None
            ingredient_ids = []
            for child in dish_state:
                if child.tag == 'image':
                    image = child.text
                elif child.tag == 'ingredientIDs':
                    for ingredientID in child:
                        ingredient_ids.append(ingredientID.text)
            dish_states.append(level.DishState(image, ingredient_ids))

    def parse_level(self):
        dish_image = None
        ingredients = None
        dish_states = None
        for child in self.root:
            if child.tag == 'ingredients':
                ingredients = self._obtain_ingredients(child)
            elif child.tag == 'dishImage':
                dish_image = self._obtain_dish_image(child)
            elif child.tag == 'dishStates':
                dish_states = self._obtain_dish_states(child)
        pprint.pprint(ingredients)
        print(dish_image)
        return level.Level(dish_image, ingredients, dish_states)
        # ingredients = self.root.iter('ingredients')
        # for ingredient in ingredients:
        #     print(ingredient.tag)
        #     print(ingredient.attrib)
            


