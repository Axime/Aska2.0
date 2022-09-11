from http import cookies
from flask import Flask, request
from jwt.jwt import JWT
import jwt

def client(app: Flask):
    @app.get('/<string:manifest>.json')
    @app.get('/<string:s>/<string:s1>/<string:s2>')
    @app.get('/<string:s>/<string:s1>')
    @app.get('/<string:s>')
    @app.get('/static/js/<string:js>.js')
    @app.get('/static/css/<string:css>.css')
    @app.get('/static/js/<string:js>.js.<string:map>')
    @app.get('/static/css/<string:css>.css.<string:map>')
    @app.get('/')
    def client_handler(**a):
        if (not a.get('js') and not a.get('css') and not a.get('manifest')):
            with open('./client/build/index.html', 'r', encoding='utf-8') as f:
                headers = {
                    'Content-Type': 'text/html',
                }
                if (not request.cookies.get('__secure_key')):
                    aaa = JWT()
                    # class a(jwt.AbstractJWKBase):
                        # pass
                    # b = a()
                    headers['Set-Cookie'] = F"__secure_key={aaa.encode({}, jwt.jwk.OctetJWK(b'123'))}; Max-Age=86400; samesite=lax"
                return f.read(), 200, headers
        if (a.get('manifest')):
            with open('./client/build/manifest.json') as f:
                return f.read()
        for i in ('js', 'css'):
            if (a.get(i)):
                url = './client/build/static/' + i + '/' + \
                    a.get(i) + '.' + i + ('.map' if a.get('map') else '')
                with open(url, 'r', encoding='utf-8') as f:
                    return f.read(), 200, {
                        'Content-Type': 'text/css' if i == 'js' else 'applicaiton/javascript'
                    }
    return client_handler
