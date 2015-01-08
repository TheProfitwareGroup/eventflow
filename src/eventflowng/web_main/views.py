from django.shortcuts import render
from eventflowng.decorators.render_response import render_response


def index(request):
	data = {}
	return render_response(request, 'webmain_index.html', data)