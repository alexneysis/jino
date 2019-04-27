from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def pool_clients(request):
    return render(request, 'jino/patients_pool.html')


def send_client(request):
    if request.method == "POST":
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404, content="It is't POST request")
