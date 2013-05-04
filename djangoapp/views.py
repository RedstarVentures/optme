from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello visitor")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body> Current time is %s. </body></html>" % now
	return HttpResponse(html)