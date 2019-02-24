from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def home(request):
    return render(request, 'jino/index.html')

def email(request):
    return render(request, 'jino/email.html')

def test(request):
    return render(request, 'jino/test.html')