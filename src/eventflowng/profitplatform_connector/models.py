__author__ = 'harlov'
from profitplatform_connector.ProfitPlatformRequest import ProfitPlatformRequest


class PlatformCommonDao:
    schema_prefix = 'platform.common'
    
    def __init__(self):
        self.rpc = ProfitPlatformRequest()
        
    def request(self, method, params=None):
        return self.rpc.request(self.schema_prefix+'.'+method, params)

    def get_session(self):
        return self.request('getsession')

    def schema_list(self):
        return self.request('schemalist')