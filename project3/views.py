from django.http import HttpResponse
import datetime 
from django.template.loader import get_template
from django.template import Context 
# to use render_to_response
from django.shortcuts import render_to_response 
# to use render 
from django.shortcuts import render

def hello(request):
	return HttpResponse("hello, world!")

# version 1 
# def current_datetime(request):
# 	now = datetime.datetime.now()
# 	t = get_template('current_datetime.html') 
# 	html = t.render(Context({'current_date': now})) 
# 	return HttpResponse(html) 

# version 2 with render_to_response 
# def current_datetime(request):
# 	now = datetime.datetime.now()
# 	return render_to_response('current_datetime.html', {'current_date':now})
	
def current_datetime(request):
	now = datetime.datetime.now() 
	# or 
	# context = {'current_date': now} 
	# return render(Request, 'current_datetime.html', context)
	return render(request, 'current_datetime.html', {'current_date':now})

def hours_ahead(request, offset): 
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time' : dt})

def hours_behind(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() - datetime.timedelta(hours=offset)
	return render(request, 'hours_behind.html', {'hour_offset': offset, 'past_time': dt})

