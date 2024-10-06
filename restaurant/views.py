# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm, Logger
from .models import Menu, Booking, Feedback
from django.db.models import Avg

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def feedback(request):
    feedbacks = Feedback.objects.all()
    feed = Logger()
    if request.method == 'POST':
        feed =Logger(request.POST)
        if feed.is_valid():
            feed.save()
    average_rating = Feedback.objects.aggregate(Avg('rating'))
    average_rating_value = round(float(average_rating['rating__avg']) if average_rating['rating__avg'] is not None else 0, 2)
    context = {'feed':feed,
               'average_rating': average_rating_value,
               'feedbacks': feedbacks,}
    return render(request, 'feedback.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    main_data = {'menu':menu_data}
    return render(request,'menu.html',{"menu":main_data})

def display_menu_items(request, pk=None):
    if pk:
        try:
            menu_item = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            menu_item = ""
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})