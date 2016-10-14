import bottle
from bottle import run, route, template

@route('/static/<filepath:path>', name='static_file')
def static(filepath):
    return static_file(filepath, root="./static")


@route('/example')
def hello():
    return template('example')

@route('/test')
def test():
    return 'test'

@route('/')
def main():
    return template('steps')

run(debug=True)




