from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Category
from .forms import EventForm
from django.db.models import Q

def index(request):
    category = request.GET.get("category", "all")
    if category == "all":
        events = Event.objects.all()
    else:
        events = Event.objects.filter(category__slug=category)

    search = request.GET.get("search", "").strip()
    if search:
        events = events.filter(Q(name__icontains=search) | Q(description__icontains=search) | Q(place__icontains=search))
    context = {
        "events": events,
        "categories": Category.objects.all(),
        "category_select": category,
        "search": search
    }
    return render(request, 'app/index.html', context)

def detail(request, pk, slug):
    event = get_object_or_404(Event, pk=pk, slug=slug)
    context = {
        "event": event
    }
    return render(request, 'app/event_detail.html', context)

def create(request):
    error = ""
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            error = "Форма заполнена некорректно"
    else:
        form = EventForm()
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'app/event_create.html', context)