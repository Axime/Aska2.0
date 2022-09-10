from flask import Flask


def client(app: Flask):
    @app.get('/<string:s>/<string:s1>/<string:s2>')
    @app.get('/<string:s>/<string:s1>')
    @app.get('/<string:s>')
    @app.get('/static/js/<string:js>.js')
    @app.get('/static/css/<string:css>.css')
    @app.get('/static/js/<string:js>.js.<string:map>')
    @app.get('/static/css/<string:css>.css.<string:map>')
    @app.get('/')
    def client_handler(**a):
        if (not a.get('js') and not a.get('css')):
            with open('./client/build/index.html', 'r', encoding='utf-8') as f:
                return f.read()
        for i in ('js', 'css'):
            if (a.get(i)):
                url = './client/build/static/' + i + '/' + \
                    a.get(i) + '.' + i + ('.map' if a.get('map') else '')
                with open(url, 'r', encoding='utf-8') as f:
                    return f.read()
    return client_handler
