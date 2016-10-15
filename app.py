import bottle
from bottle import Bottle, run, route, get, post, template, static_file, url, request

from recipe import Recipe

app = Bottle()

@app.route('/static/<filepath:path>', name='static_file')
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
def steps():
    recipe_url = request.forms.get('recipe_url')

    recipe = Recipe(recipe_url=recipe_url)
    steps = recipe.steps

    return template('steps', url=app.get_url, recipe_url=recipe_url, steps=steps)

class StripPathMiddleware(object):
    '''
    Get that slash out of the request
    '''
    def __init__(self, a):
        self.a = a
    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e, h)

if __name__ == '__main__':
    run(app=StripPathMiddleware(app))




