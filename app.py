import bottle
from bottle import Bottle, run, route, get, post, template, static_file, url, request, debug

from recipe import Recipe


app = Bottle()
debug(False)

@app.route('/static/<filepath:path>', name='static_file')#this path is hard coding!! so must change code
def static(filepath):
    return static_file(filepath, root="./static")


@app.route('/example')
def hello():
    return template('example')

@app.route('/test')
def test():
    return 'test'

@app.get('/')
def index():
    return template('index', url=app.get_url)

@app.post('/making')
@app.post('/')
def making():
    recipe_url = request.forms.get('recipe_url')

    recipe = Recipe(recipe_url=recipe_url)
    steps = recipe.steps
    ingredients = recipe.ingredients

    return template('steps', url=app.get_url, recipe_url=recipe_url, 
    	steps=steps, ingredients=ingredients)

if __name__ == '__main__':
    run(app=app, debug=True)


