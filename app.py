import bottle
from bottle import run, route, get, post, template, static_file, url, request

from recipe import Recipe

@route('/static/<filepath:path>', name='static_file')
def static(filepath):
    return static_file(filepath, root="./static")


@route('/example')
def hello():
    return template('example')

@route('/test')
def test():
    return 'test'

@get('/')
def index():
    return template('index', url=url)

@post('/making')
def steps():
    recipe_url = request.forms.get('recipe_url')

    recipe = Recipe(url=recipe_url)
    steps = recipe.steps

    return template('steps', url=url, recipe_url=recipe_url, steps=steps)

run(debug=True)




