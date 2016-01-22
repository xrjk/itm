from django.shortcuts import render_to_response
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    #t = get_template('current_datetime.html')
    #html = "<html><body>It is now %s.</body></html>" % now
    #html = t.render(Context({'current_date': now}))
    return render_to_response('current_datetime.html',{'current_date': now})

def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return render_to_response('hours_ahead.html',{'hours_offset': offset,'next_time': dt})
