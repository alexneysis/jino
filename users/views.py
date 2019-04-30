from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from users.models import Client


def pool_clients(request):
    return render(request, 'jino/patients_pool.html')


def send_client_old(request):
    if request.method == "POST":
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404, content="It is't POST request")


@csrf_exempt
def send_client(request):
    data = {"name": "alex"}
    try:
        print(request.body)
        print(request.method)
        all_clients = Client.objects.all()
        # print(json.dumps(list(all_clients)))
        # data = serializers.serialize("json", Client.objects.all())
        data = serialize('json', Client.objects.all(), ensure_ascii=False)
        # data = Client.objects.all()
        # print(all_clients[0])
        # print(type(all_clients))
        # json_string = json.dumps(all_clients)
        # print(json_string)
        # print(type(json_string))

        print(data)
        print(type(data))

        # all_clients= []
        # for i in data:
        #     all_clients.append()

        # just return a JsonResponse
        # return JsonResponse(data)
        # header('Content-Type: application/json; charset=utf-8');
    except Exception as e:
        print(e)
    return HttpResponse(data, charset="utf-8")


@csrf_exempt
def chat(request):
    return render(request, 'chat/index.html')
