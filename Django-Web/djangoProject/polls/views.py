from django.http import HttpResponse


def index(request):
    # raise Exception
    return HttpResponse("Hello!")
