from bottle import route, run,template


@route('<filepath:path>')
def send_static(filename):
    return static_file(filename, root='/HTML/jean/')

@route('/hello')
@route('/hello/<name>')
def greet(name='Stranger'):
     return template('HTML/jean/index.html',name=name)


run(host='localhost', port=8080, debug=True)
