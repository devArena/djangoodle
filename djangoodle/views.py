
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.template.context import RequestContext
from djangoodle.models import Event, EventItem, Participant
from django.utils import timezone
from django.core import serializers
import datetime
import json

def main(request):
    context = RequestContext(request)
    return render_to_response('main.html', context)

def event(request):
    context = RequestContext(request)
    return render_to_response('event.html', context)

def event_detail(request,event_id):
    # context = RequestContext(request)
    e = get_object_or_404(Event, pk=event_id)
    # return render_to_response('eventdetail.html', context)
    return render(request, 'event_detail.html', {
        'event': e,
        'event_item_list': e.eventitem_set.all(),
    })

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

            for item in items:
                print item['time']
                time = datetime.datetime.strptime(item['time'], '%d.%m.%Y %H:%M')
                event.eventitem_set.add(EventItem(event_item_name=item['category'], event_item_time=time))

            return HttpResponse(event.id)
        except KeyError:
            HttpResponseServerError("Malformed data!")
    return HttpResponse(-1)


def add_participant(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print data
        try:
            p_name = data['participant_name']
            event_id = data['event_id']
            selected_items = data['selected_items']
                        
            participant = Participant(name=p_name)

            event = Event.objects.get(pk=event_id)
            event.participant_set.add(participant)
            
            participant.event_items.add(*selected_items)

            # return_data = [{
            #     'event': event,
            #     'event_items': event.eventitem_set.all().values_list('event_item_name', 'event_item_time'),
            # }]

            #return HttpResponse(serializers.serialize("json", return_data))

            # return_data ={
            #                 'event': event,
            #                 'event_items': event.eventitem_set.all()
            #             }
            #print serializers.serialize("json", return_data)
            return HttpResponse(1)
        except KeyError:
            HttpResponseServerError("Malformed data!")
    return HttpResponse(-1) 

