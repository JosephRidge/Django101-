from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request): 
    context = {'data':'Welcome Software Engineers!'} #data
    return render(request, 'firstApp/home.html', context)

def about(request):
    return render(request, 'firstApp/about.html')

def contact(request):
    context = {
        'email':'jd@example.com',
        'phoneNo'  : '07123456789',
        'year':2026, 
        'location':'Nairobi' 
        }
    return render(request, 'firstApp/contact.html', context)



def experiences(request):
    context= {
        'places':['Germany', 'Canada', 'Kuwait'],
        'year':2026,
        'age':20
    }  # dictionary tht will host our data
    return render(request, 'firstApp/experience.html', context)


def landing(request):
    return render(request, 'landing.html')