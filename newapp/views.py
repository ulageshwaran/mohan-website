from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import * # Create your views here.

def index(request):

    if request.method == 'POST':    
        username6 = request.POST.get('username6')
        email6 = request.POST.get('email6')
        
        myuser = newsletter.objects.create(username=username6, email=email6)
        myuser.save()

    return render(request, "app/index.html")

def blog(request):

    if request.method == 'POST':    
        username2 = request.POST.get('username2')
        email2 = request.POST.get('email2')
        
        myuser = newsletter.objects.create(username=username2, email=email2)
        myuser.save()

    return render(request, "app/blog.html")

def cart(request):
    context = {}

    if request.method == 'POST':    
        username3 = request.POST.get('username3')
        email3 = request.POST.get('email3')
        
        myuser = newsletter.objects.create(username=username3, email=email3)
        myuser.save()

    return render(request, "app/cart.html", context)

def checkout(request):
    context = {}
    
    if request.method == 'POST':    
        username4 = request.POST.get('username4')
        email4 = request.POST.get('email4')
        
        myuser = newsletter.objects.create(username=username4, email=email4)
        myuser.save()

    return render(request, "app/checkout.html", context)

def contact(request):

    if request.method == 'POST':    
        username5 = request.POST.get('username5')
        email5 = request.POST.get('email5')
        
        myuser = newsletter.objects.create(username=username5, email=email5)
        myuser.save()

    return render(request, "app/contact.html")

def about(request):

    if request.method == 'POST':    
        username1 = request.POST.get('username1')
        email1 = request.POST.get('email1')
        
        myuser = newsletter.objects.create(username=username1, email=email1)
        myuser.save()

    return render(request, "app/about.html")

def service(request):

    if request.method == 'POST':    
        username7 = request.POST.get('username7')
        email7 = request.POST.get('email7')
        
        myuser = newsletter.objects.create(username=username7, email=email7)
        myuser.save()

    return render(request, "app/service.html")

def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    
    if request.method == 'POST':    
        username8 = request.POST.get('username8')
        email8 = request.POST.get('email8')
        
        myuser = newsletter.objects.create(username=username8, email=email8)
        myuser.save()
    
    return render(request, "app/shop.html", context)

def thankyou(request):
    return render(request, "app/thankyou.html")
