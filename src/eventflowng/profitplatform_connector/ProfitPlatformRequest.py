__author__ = 'harlov'
import requests
from django.conf import settings
import logging
import traceback
logger = logging.getLogger('eventflowng.profitplatofrm_connector')
from django.utils.translation import ugettext as _


class ProfitPlatformRequest():
    STATUS_SUCCESS = 1
    STATUS_PLATFORM_CONNECT_ERROR = -1
    STATUS_PLATFORM_ERROR_OBSCURE = -100
    
    MESSAGE_SUCCESS = _("platform ping OK")
    MESSAGE_PLATFORM_CONNECT_ERROR = _("platform connect error")
    MESSAGE_PLATFORM_ERROR_OBSCURE = _("platform obscure error")
    
    def __init__(self):
        self.platform_root = "%s://%s:%s%s" % (
            settings.PROFIT_PLATFORM['protocol'],
            settings.PROFIT_PLATFORM['host'],
            settings.PROFIT_PLATFORM['port'],
            settings.PROFIT_PLATFORM['prefix'],
        )
        logger.debug("ProfitPlatform RPC client created")

    def request(self, schema, params=None):
        endpoint = self.platform_root
        send_data = dict(jsonrpc='2.0', id=1, method=schema, params=params)
        logger.debug("request endpoint : %s" % endpoint)
        try:
            req = requests.post(endpoint, send_data)
        except Exception as e:
            traceback.print_exc()
            traceback.print_stack()
            return dict(status=self.STATUS_PLATFORM_CONNECT_ERROR, status_message=self.MESSAGE_PLATFORM_CONNECT_ERROR)
        if req:
            return dict(data=req.json(), status=self.STATUS_SUCCESS, status_message=self.MESSAGE_SUCCESS)
        else:
            return dict(status=self.STATUS_PLATFORM_ERROR_OBSCURE, status_message=self.MESSAGE_PLATFORM_ERROR_OBSCURE)