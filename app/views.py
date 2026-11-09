from django.shortcuts import render, get_object_or_404
from .models import Event

def index(request):
    events = Event.objects.all()
    context = {
        "events": events
    }
    return render(request, 'app/index.html', context)

def detail(request, pk, slug):
    event = get_object_or_404(Event, pk=pk, slug=slug)
    context = {
        "event": event
    }
    return render(request, 'app/event_detail.html', context)

