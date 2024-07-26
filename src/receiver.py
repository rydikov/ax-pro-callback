import os
import logging
import json
import falcon

from axpro import AxPro

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

axpro = AxPro(
    os.environ.get('AX_PRO_HOST'),
    os.environ.get('AX_PRO_USER'),
    os.environ.get('AX_PRO_PASSWORD')
)

class DisarmResource:
    def on_post(self, req, resp):
        resp = axpro.disarm()
        answer = 'OK' if resp['statusCode'] == 1 else resp['errorMsg']
        resp.text = json.dumps({'status': answer})
        resp.status = falcon.HTTP_200
