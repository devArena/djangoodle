
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.template.context import RequestContext
from djangoodle.models import Event, EventItem
from django.utils import timezone
import datetime
import json

def home(request):
    context = RequestContext(request)
    return render_to_response('home.html', context)

def event_detail(request,event_id):
    context = RequestContext(request)
    return render_to_response('eventdetail.html', context)

def create_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            name = data['name']
            description = data['description']
            email = data['email']
            items = data['items']
            # If time_of_creation is handled by database default value
            event = Event(name=name, description=description, email_of_creator=email)
            event.save()

            print event.id

            for item in items:
                event.eventitem_set.add(EventItem(event_item_name="dada"))

            return HttpResponse(event.id)
        except KeyError:
            HttpResponseServerError("Malformed data!")
    return HttpResponse(-1)

