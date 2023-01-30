from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import pic, tourism, ethnic
from comments.models import comment
import json
import markdown
from comments.forms import CommentForm


# Create your views here.
def index(request):
    img = pic.objects.all()
    attractions = tourism.objects.all()
    ethnics = ethnic.objects.all()
    current_user = request.user
    return render(request, 'index.html',
                  {'img': img, 'attractions': attractions, 'ethnic': ethnics, 'user': current_user})


def about(request):
    current_user = request.user
    return render(request, 'about.html', {'user': current_user})


def contacts(request):
    current_user = request.user
    return render(request, 'contacts.html', {'user': current_user})


def typography(request):
    comment_list = comment.objects.all()
    current_user = request.user
    img = pic.objects.all()
    attractions = tourism.objects.all()
    ethnics = ethnic.objects.all()
    address_longitude = []
    address_latitude = []
    address_data = []
    form = CommentForm()

    for i in range(len(attractions)):
        address_longitude.append(attractions[i].longitude)
        address_latitude.append(attractions[i].latitude)
        address_data.append(attractions[i].intro)

    return render(request, 'typography.html', {'img': img, 'attractions': attractions, 'ethnic': ethnics,
                                               'address_longitude': json.dumps(address_longitude),
                                               'address_latitude': json.dumps(address_latitude),
                                               'address_data': json.dumps(address_data),
                                               'user': current_user,
                                               'comment_list': comment_list,
                                               'form': form})
