from django.shortcuts import render
from eventflowng.decorators.render_response import render_response
from profitplatform_connector.ProfitPlatformRequest import ProfitPlatformRequest
from profitplatform_connector.models import PlatformCommonDao
def index(request):
    data = dict()
    platform_common_dao = PlatformCommonDao()
    
    data['session'] = platform_common_dao.get_session()

    return render_response(request, 'webmain_index.html', data)