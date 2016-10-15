#coding:utf-8
import sys,subprocess, requests
from bs4 import BeautifulSoup


class Recipe():
    finish_flag = False

    def __init__(self, recipe_url):
        url = recipe_url #'http://cookpad.com/recipe/%s'%recipe_id
        html = subprocess.check_output(['curl', '%s'%url])
        self.soup = BeautifulSoup(html, "html.parser")
        self.steps = self.get_steps()
        self.ingredients = self.get_ingredients()

    def quantities(self, ingredient):
        text = self.ingredients[ingredient]
        self.text = text

    def get_ingredients(self):
        ingredients_class = 'ingredient_name'
        quantity_class = 'ingredient_quantity amount'
        ingredients = {}
        for ingredient, quantitity in zip(self.soup.find_all('div', class_=ingredients_class),self.soup.find_all('div', class_=quantity_class)):
            q = quantitity.string
            ingredient = ingredient.find('span', class_='name')
            if not ingredient.string:
                ingredient = ingredient.find('a')

            ingredients[ingredient.string] = q
        return ingredients


    def get_steps(self):
        steps = self.soup.find_all(class_='instruction')

        lists = []
        for step in steps:
            text = step.find(class_='step_text').text

            im_check = step.find(class_='image')

            if im_check:
                img = im_check.img.get('data-large-photo')
            else:
                img = None

            s_data = {'text': text, 'image':img}
            lists.append(s_data)
            
        return lists

if __name__ == '__main__':
    recipe_id = '1336653'
    url = 'http://cookpad.com/recipe/%s'%recipe_id
    recipe = Recipe(recipe_url=url)
    
