
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, HttpResponseServerError
from django.template.context import RequestContext
from djangoodle.models import Event, EventItem, Participant
from django.utils import timezone
from django.core import serializers
import datetime
import json
import uuid

def main(request):
    context = RequestContext(request)
    return render_to_response('main.html', context)

def event(request):
    context = RequestContext(request)
    return render_to_response('event.html', context)

def event_detail(request,event_id):
    # context = RequestContext(request)
    e = get_object_or_404(Event, pk=event_id)
    e_items = e.eventitem_set.all()
    # return render_to_response('eventdetail.html', context)
    return render(request, 'event_detail.html', {
        'event': e,
        'event_item_list': e_items,
        'event_item_id_list': e_items.values_list("id", flat=True),
        'participant_list': e.participant_set.all()
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
	    event_id = str(uuid.uuid4())[1:8]
	    event = Event(name=name, description=description, email_of_creator=email, id = event_id)
            event.save()

            for item in items:
                print item['time']
                time = datetime.datetime.strptime(item['time'], '%d.%m.%Y %H:%M')
                event.eventitem_set.add(EventItem(event_item_name=item['category'], event_item_time=time))

            return_data = {
                'success':True,
                'id':event.id,
            }
            return HttpResponse(json.dumps(return_data), content_type="application/json") 
        except KeyError:
            HttpResponseServerError("Malformed data!")
    return HttpResponse(-1)


def add_participant(request):
    if request.method == 'POST':
        data = json.loads(request.body)        
        try:
            p_name = data['participant_name']
            event_id = data['event_id']
            selected_items = data['selected_items']
                        
            participant = Participant(name=p_name)

            event = Event.objects.get(pk=event_id)
            event.participant_set.add(participant)
            
            participant.event_items.add(*selected_items)

            return_data = {
                'success':True,
                'participant_id':participant.id,
                'participant_name':participant.name,
                'selected_items':selected_items
            }
            return HttpResponse(json.dumps(return_data), content_type="application/json") 

        except Exception as e:
            return HttpResponseServerError(e.message, type(e))

    return HttpResponseServerError("Error!")

def get_participants(request, event_id):
    if request.method == 'GET':

        try:
            event = Event.objects.get(pk=event_id)
            participants = event.participant_set.all()

            return_data = {
                'success':True,
                'participants':[]
            }

            for par in participants:                   
                return_data['participants'].append({
                    'participant_id': par.id,
                    'participant_name':par.name,
                    'selected_items':map(str, par.event_items.values_list('id', flat=True).order_by('id'))
                })                

            #print return_data

            return HttpResponse(json.dumps(return_data), content_type="application/json")
        except Exception as e:
            return HttpResponseServerError(e.message, type(e))

    return HttpResponseServerError("Error!")

def delete_participant(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            participant_id = data['participant_id']
            participant = Participant.objects.get(pk=participant_id)
            participant.delete()
            return HttpResponse(json.dumps({'success':True}), content_type="application/json")
        except Exception as e:
            return HttpResponseServerError(e.message, type(e))

    return HttpResponseServerError("Error!")

def edit_participant(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            participant_id = data['participant_id']
            p_name = data['participant_name']
            sel_items = data['selected_items']

            participant = Participant.objects.get(pk=participant_id)
            participant.name = p_name

            participant.event_items.clear()
            participant.event_items.add(*sel_items)

            participant.save()

            return HttpResponse(json.dumps({'success':True}), content_type="application/json")
        except Exception as e:
            return HttpResponseServerError(e.message, type(e))

    return HttpResponseServerError("Error!")


