from django.shortcuts import render
from django.conf import settings


# Create your views here.
def home(request):
    context = {
        "test": "TEST",
    }
    return render(request, "core/home.html", context=context)


def something_cool(request):
    context = {
        "test": "something_cool",
        "static": settings.STATICFILES_DIRS[0],
    }
    return render(request, "core/something_cool.html", context=context)
