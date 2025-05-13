from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'myapp/index.html')
def about(request):
    return HttpResponse("<h4>About devlp</h4>")