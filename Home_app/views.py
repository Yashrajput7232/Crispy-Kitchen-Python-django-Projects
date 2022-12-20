from django.shortcuts import render ,HttpResponse


# Create your views here.
def index(request):
    return render (request,"index.html")
    # return HHttpResponsettpResponse("This is our Home Page")
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def services (request):
    return render(request,'menu.html')
def news (request):
    return render(request,'news.html')
def news_detail (request):
    return render(request,'news-detail.html')
