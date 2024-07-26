import os
import falcon

from falcon.http_status import HTTPStatus

from .receiver import DisarmResource


class AuthMiddleware:
    def process_request(self, req, resp):
        token = req.get_header('Authorization')

        if token is None:
            description = 'Please provide an auth token as part of the request.'
            raise falcon.HTTPUnauthorized(title='Auth token required', description=description)

        if not self._token_is_valid(token):
            description = 'The provided auth token is not valid. Please request a new token and try again.'
            raise falcon.HTTPUnauthorized(title='Authentication required', description=description)

    def _token_is_valid(self, token):
        return token == os.environ.get('SECRET_TOKEN')


class HandleCORS(object):
    def process_request(self, req, resp):
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', '*')
        resp.set_header('Access-Control-Allow-Headers', '*')
        resp.set_header('Access-Control-Max-Age', 1728000)  # 20 days
        if req.method == 'OPTIONS':
            raise HTTPStatus(falcon.HTTP_200, body='\n')


app = application = falcon.App(middleware=[HandleCORS(), AuthMiddleware()])

disarm = DisarmResource()

app.add_route('/disarm', disarm)
