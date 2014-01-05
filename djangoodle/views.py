
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.template.context import RequestContext
import json

def home(request):
    context = RequestContext(request)
    return render_to_response('home.html', context)

def create_event(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            items = data['items']
            print items
        except KeyError:
            HttpResponseServerError("Malformed data!")
    return HttpResponse("Got json data")