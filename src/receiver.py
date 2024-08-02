import os
import logging
import json
import falcon

from axpro import AxPro

ALREADY_ARMED_STATUS_CODE = 1073774603

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
        ax_resp = axpro.arm_away()
        if ax_resp['errorCode'] == ALREADY_ARMED_STATUS_CODE:
            ax_resp = axpro.subsystem_status()
            disarmed_areas = [
                area for area in ax_resp['SubSysList'] 
                if area['SubSys']['enabled'] and area['SubSys']['arming'] != 'away'
            ]
            if disarmed_areas:
                axpro.disarm()
                ax_resp = axpro.arm_away()
                answer = 'OK' if ax_resp['statusCode'] == 1 else ax_resp['errorMsg']
            else:
                # all areas are already armed
                answer = 'OK'
        else:
            answer = 'OK' if ax_resp['statusCode'] == 1 else ax_resp['errorMsg']
        resp.text = json.dumps({'status': answer})
        resp.status = falcon.HTTP_200
