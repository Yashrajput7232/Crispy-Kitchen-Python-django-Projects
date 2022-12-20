from django.shortcuts import render ,HttpResponse
from Home_app.models import Reservations


# Create your views here.
def index(request):
    return render (request,"index.html")
    # return HHttpResponsettpResponse("This is our Home Page")
def contact(request):
    if (request.method=='POST'):
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        people=request.POST.get('people')
        date=request.POST.get('date')
        message=request.POST.get('message')
        r=Reservations(name=name,email=email,phone=phone,people=people,date=date, message=message);
        r.save();
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def services (request):
    return render(request,'menu.html')
def news (request):
    return render(request,'news.html')
def news_detail (request):
    return render(request,'news-detail.html')
