from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render
from testapp.models import tourism, ethnic


def dashboard(request):
    user_count = User.objects.count()
    attractions_count = tourism.objects.count()
    ethnics_count = ethnic.objects.count()

    context = {'user_count': user_count, 'attactions_count': attractions_count, 'ethnics_count': ethnics_count}
    return render(request, 'backend/dashboard.html', context)
