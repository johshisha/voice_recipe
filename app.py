import bottle
from bottle import run, route, template, static_file, url

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
    return template('steps', url=url)

run(debug=True)




