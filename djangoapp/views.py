from django.template.loader import get_template
from django.template import Template, Context
from django.http import HttpResponse
import datetime

def hello(request):
	t = get_template('hello.html')
	html = t.render(Context())	
	return HttpResponse(html)

def current_datetime(request):
	tnow = datetime.datetime.now()
	t = get_template('current_datetime.html')
	#t = Template("<html><body> Current time is %s. </body></html>")
	html = t.render(Context({'current_date': tnow}))
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s. </body></html>" % (offset,dt)
	return HttpResponse(html)