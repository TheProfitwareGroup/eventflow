from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

def render_response(req, *args, **kwargs):
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)