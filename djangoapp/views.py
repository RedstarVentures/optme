# from django.template.loader import get_template
# from django.template import Template, Context
# from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
	return render(request, 'hello.html')
	# t = get_template('hello.html')
	# html = t.render(Context())	
	# return HttpResponse(html)

def current_datetime(request):
	tnow = datetime.datetime.now()
	return render(request, 'current_datetime.html', {'current_date': tnow})
	# t = get_template('current_datetime.html')
	# html = t.render(Context({'current_date': tnow}))
	# return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render(request, 'current_datetime.html', {'current_date': dt})
	# html = "<html><body>In %s hour(s), it will be %s. </body></html>" % (offset,dt)
	# return HttpResponse(html)