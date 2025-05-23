import os
import logging
import json
import falcon

from axpro import AxPro, AlreadyArmedError


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
        ax_resp = axpro.disarm()
        answer = 'OK' if ax_resp['statusCode'] == 1 else ax_resp['errorMsg']
        resp.text = json.dumps({'status': answer})
        resp.status = falcon.HTTP_200

class ArmResource:
    def on_post(self, req, resp):
        try:
            ax_resp = axpro.arm_away()
        except AlreadyArmedError as e:
            resp.status = falcon.HTTP_400
            answer = 'The partition is armed.'
        else:
            resp.status = falcon.HTTP_200
            answer = 'OK' if ax_resp['statusCode'] == 1 else ax_resp['errorMsg']

        resp.text = json.dumps({'status': answer})
        
