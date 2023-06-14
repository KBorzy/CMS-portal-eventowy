from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm


def index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {'events': events})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.save()
            return redirect('cms:index')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})


def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_details.html', {'event': event})
