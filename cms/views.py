from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Ticket
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


@login_required
def event_details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        ticket_quantity = int(request.POST.get('ticket_quantity', 0))
        ticket_price = event.ticket_price
        total_price = ticket_quantity * ticket_price

        if ticket_quantity > 0:
            ticket = Ticket(user=request.user, event=event, quantity=ticket_quantity, price=total_price)
            ticket.save()
            return redirect('cms:user_tickets')

    return render(request, 'events/event_details.html', {'event': event})
@login_required
def user_events(request):
    events = Event.objects.filter(author=request.user)
    return render(request, 'events/user_events.html', {'events':events})


@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('cms:user_events')
    else:
        form = EventForm(instance=event)

    return render(request, 'events/edit_event.html', {'event': event, 'form': form})

@login_required
def user_tickets(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'events/user_tickets.html', {'tickets': tickets})

@login_required
def buy_tickets(request, event_id):
    event = Event.objects.get(pk=event_id)

    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        price = event.ticket_price * quantity

        ticket = Ticket(user=request.user, event=event, quantity=quantity, price=price)
        ticket.save()

        return redirect('cms:user_tickets')  # Przekierowanie do profilu po zakupie biletów

    return render(request, 'events/buy_tickets.html', {'event': event})
