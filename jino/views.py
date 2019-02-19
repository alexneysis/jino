from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def about(request):
    return render(request, 'jino/about.html')

def index(request):
    return render(request, 'jino/index.html')

def test(request):
    return render(request, 'jino/test.html')

def examplePage(request):
    return render(request, 'jino/examplePage.html')