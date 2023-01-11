from django.shortcuts import render
from .models import pic, tourism, ethnic
import json


# Create your views here.
def index(request):
    img = pic.objects.all()
    attractions = tourism.objects.all()
    ethnics = ethnic.objects.all()
    return render(request, 'index.html', {'img': img, 'attractions': attractions, 'ethnic': ethnics})


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def typography(request):
    img = pic.objects.all()
    attractions = tourism.objects.all()
    ethnics = ethnic.objects.all()
    address_longitude = []
    address_latitude = []
    address_data = []
    for i in range(len(attractions)):
        address_longitude.append(attractions[i].longitude)
        address_latitude.append(attractions[i].latitude)
        address_data.append(attractions[i].intro)

    return render(request, 'typography.html', {'img': img, 'attractions': attractions, 'ethnic': ethnics,
                                               'address_longitude': json.dumps(address_longitude),
                                               'address_latitude': json.dumps(address_latitude),
                                               'address_data': json.dumps(address_data)})
