from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'website/home.html', context={'home_active': 'active'})


def about(request):
    return render(request, 'website/about.html', context={'about_active' : 'active'})


def quote(request):
    return render(request, 'website/quote.html', context={'pages_active' : 'active'})

