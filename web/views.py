from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Enrollment,News,Gallery
import africastalking
from django.conf import settings
from .forms import NewsForm, GalleryForm
from django.core.mail import send_mail
from django.conf import settings


# Initialize Africa's Talking
africastalking.initialize(username=settings.AFRICASTALKING_USERNAME, api_key=settings.AFRICASTALKING_API_KEY)
sms = africastalking.SMS


@login_required
def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('web:news')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})

@login_required
def add_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('web:gallery')
    else:
        form = GalleryForm()
    return render(request, 'add_gallery.html', {'form': form})

from .forms import EnrollmentForm

# @login_required
def enroll_view(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.user = request.user  # Associate the enrollment with the current user
            enrollment.save()

            # Send SMS
            try:
                response = sms.send(f'You have been enrolled, {enrollment.name}.', [enrollment.phone_number])
                print(response)
            except Exception as e:
                print(f'Error sending SMS: {e}')

            # Send Email
            try:
                send_mail(
                    'Enrollment Confirmation',
                    f'Dear {enrollment.name},\n\nYou have successfully enrolled.\n\nThank you!',
                    settings.DEFAULT_FROM_EMAIL,
                    [enrollment.email],
                    fail_silently=False,
                )
            except Exception as e:
                print(f'Error sending email: {e}')

            return redirect('web:index')  # Redirect to index page after enrollment

    else:
        form = EnrollmentForm()

    return render(request, 'enroll.html', {'form': form})
# Create your views here.

def about(request):
    
    return render(request, "about.html")

def cbc(request):
    
    return render(request, "cbc.html")

def contact(request):
    
    return render(request, "contact.html")

def daycare(request):
    
    return render(request, "daycare.html")

def elements(request):
    
    return render(request, "elements.html")

def gallery(request):
    gallery = Gallery.objects.all()
    return render(request, "gallery.html",{'gallery': gallery})

def index(request):
    
    return render(request, "index.html")

def login(request):
    
    return render(request, "login.html")

def news(request):
    news_items = News.objects.all()
    return render(request, "news.html",{'news_items': news_items})

def nursery(request):
    
    return render(request, "nursery.html")

def pp1(request):
    
    return render(request, "pp1.html")

def pp2(request):
    
    return render(request, "pp2.html")

def sign_up(request):
    
    return render(request, "sign_up.html")

def staff(request):
    
    return render(request, "staff.html")