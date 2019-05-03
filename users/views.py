import logging

from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from users.models import Client, Status


def pool_clients(request):
    return render(request, 'jino/patients_pool.html')

def wait(request):
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Wait client")
    logging.debug("Request body = " + str(request.body))
    try:
        logging.debug("Request id = " + str(request.POST["patientId"]))
        logging.debug("Request body = " + str(request.body))
        id = int(request.POST["patientId"])
        client = Client.objects.get(pk=id)
        logging.debug("Status before = " + str(client.status))
        client.status = Status.objects.get(pk=20)
        client.save()
        logging.debug("Status after = " + str(client.status))
    except Exception as e:
        print(e)
        logging.critical("Error in record client = " + str(e))
    return HttpResponse(status=200)

def busy(request):
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Busy client")
    logging.debug("Request body = " + str(request.body))
    try:
        logging.debug("Request id = " + str(request.POST["patientId"]))
        logging.debug("Request body = " + str(request.body))
        id = int(request.POST["patientId"])
        client = Client.objects.get(pk=id)
        logging.debug("Status before = " + str(client.status))
        client.status = Status.objects.get(pk=21)
        client.save()
        logging.debug("Status after = " + str(client.status))
    except Exception as e:
        print(e)
        logging.critical("Error in record client = " + str(e))
    return HttpResponse(status=200)


def record_client(request):
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Recording client")
    logging.debug("Request body = " + str(request.body))
    try:
        logging.debug("Request id = " + str(request.POST["patientId"]))
        logging.debug("Request body = " + str(request.body))
        id = int(request.POST["patientId"])
        client = Client.objects.get(pk=id)
        logging.debug("Status before = " + str(client.status))
        client.status = Status.objects.get(pk=31)
        client.save()
        logging.debug("Status after = " + str(client.status))
    except Exception as e:
        print(e)
        logging.critical("Error in record client = " + str(e))
    return HttpResponse(status=200)


def dont_record_client(request):
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Don't recording client ")
    logging.debug("Request body = " + str(request.body))
    try:
        logging.debug("Request id = " + str(request.POST["patientId"]))
        logging.debug("Request body = " + str(request.body))
        id = int(request.POST["patientId"])
        client = Client.objects.get(pk=id)
        logging.debug("Status before = " + str(client.status))
        client.status = Status.objects.get(pk=20)
        client.save()
        logging.debug("Status after = " + str(client.status))
    except Exception as e:
        print(e)
        logging.critical("Error in don't record client = " + str(e))
    return HttpResponse(status=200)

def spam_client(request):
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Spam client ")
    logging.debug("Request body = " + str(request.body))
    try:
        logging.debug("Request id = " + str(request.POST["patientId"]))
        logging.debug("Request body = " + str(request.body))
        id = int(request.POST["patientId"])
        client = Client.objects.get(pk=id)
        logging.debug("Status before = " + str(client.status))
        client.status = Status.objects.get(pk=30)
        client.save()
        logging.debug("Status after = " + str(client.status))
    except Exception as e:
        print(e)
        logging.critical("Error in spam client = " + str(e))
    return HttpResponse(status=200)


@csrf_exempt
def send_client(request):
    data = {"Result": "error"}
    try:
        print(request.body)
        print(request.method)
        all_client = Client.objects.all().exclude(status=30).exclude(status=31)
        data = serialize('json', all_client, ensure_ascii=False)
        print(data)
        print(type(data))
    except Exception as e:
        print(e)
    return HttpResponse(data, charset="utf-8")


@csrf_exempt
def chat(request):
    return render(request, 'chat/index.html')
