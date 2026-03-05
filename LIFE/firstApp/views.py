from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request): 
    context = {'data':'Welcome Software Engineers!'} #data
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    context = {
        'email':'jd@example.com',
        'phoneNo'  : '07123456789',
        'year':2026, 
        'location':'Nairobi' 
        }
    return render(request, 'contact.html', context)