from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def pool_clients(request):
    return render(request, 'jino/patients_pool.html')

def send_client(request):
    # if request.method == "POST":
    #     print("post = ", request.POST)
    #     return "Hi 1"
    # else:
    #     print(request.method + "It is not POST")
    #     return "Hi 2"
    print("Hello, I at the send_client")
    return HttpResponse(status=200)

    # return render(request, 'jino/patients_pool.html')t