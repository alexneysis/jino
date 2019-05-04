import datetime
import smtplib
from email.header import Header
from email.mime.text import MIMEText

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

import secret
from users.forms import FormClient
from users.models import Client, Status


def home(request):
    return render(request, 'jino/index.html')


def task_3(request):
    return render(request, 'homework/materialize/task_3.html')


def task_4(request):
    return render(request, 'homework/materialize/task_4.html')

def task_4_html(request):
    return render(request, 'homework/html/task_4.html')


def agreement(request):
    return render(request, 'jino/agreement.html')


def about(request):
    return render(request, 'jino/about.html')


@csrf_exempt
def get(request):
    print("I get request: ", request.body)
    return HttpResponse(status=200)


def data(request):
    print("In data method")
    args = {}
    if request.method == "POST":
        try:
            form = FormClient(request.POST)
            if form.is_valid():
                FIO = form.cleaned_data["FIO"]
                phone = form.cleaned_data["phone"]
                phone = phone.replace(" ", "")
                email = form.cleaned_data["email"]
                address = form.cleaned_data["address"]
                first_name = FIO.strip().split(" ")[0]
                surname = ""
                if len(FIO.strip().split(" ")) >= 2:
                    surname = FIO.strip().split(" ")[1]
                patronymic = ""
                if len(FIO.strip().split(" ")) >= 3:
                    patronymic = FIO.strip().split(" ")[2]
                status = Status.objects.get(pk=10)
                print("Create all fields")
                client = Client(first_name=first_name, surname=surname, patronymic=patronymic, phone=phone, email=email,
                                status=status, address=address)
                print("don't save object", client.phone)
                client.save()
                print("save object")
                data_post(request, FIO, phone, email, address)
        except Exception as e:
            print(e)
    else:
        form = FormClient()
        args["login_error"] = "Используйте метод POST для отправки"
    print("This all")
    return render(request, "jino/index.html", {"from": form})


def data_post(request, FIO, phone, email, address):
    # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    print("Input to send mail")
    # mail_receiver = "sorokin.a.n.post@gmail.com,callcentr@32praktika.ru"
    mail_receiver = "sorokin.a.n.post@gmail.com,westyerst@gmail.com,sungurova.arina@gmail.com,SmerhsarP@gmail.com"
    mail_sender = "Jino.platform@gmail.com"
    username = "Jino.platform@gmail.com"
    password = secret.PASSWORD_MAIL
    server = smtplib.SMTP('smtp.gmail.com:587')

    # Формируем тело письма
    subject = u'Запись'
    print("FIO: , " + str(FIO) + ". phone: " + str(phone) + ", mail: " + str(email))

    html = """\
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8"  />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
      </head>
      <body style="font-family: Helvetica">
        <table style="background-color: #f0f0f0; padding: 50px 0;" width="100%" cellspacing="0">
          <tr>
            <td align="center">
              <table style="background-color: #fff; border-radius: 10px;" cellspacing="0">
                <tr>
                  <td style="background-color: #52C5FF; padding: 10px;" colspan="2" align="center">
                    <a href="http://jino24.ru"><img src="http://jino24.ru/static/jino/img/logo_w.png" alt="Jino" width="100px" /></a>
                  </td>
                  <td></td>
                </tr>
                <tr>
                  <td style="padding: 20px 20px 0 20px; font-weight: bold;" colspan="2" align="center">
                """ + str(FIO) + """
                  </td>
                  <td></td>
                </tr>
                <tr>
                  <td style="padding: 0 20px" colspan="2" align="center">
                    нуждается в вашей скорой помощи.
                  </td>
                  <td></td>
                </tr>

                <tr>
                  <td style="padding: 30px">
                  Телефон: """ + str(phone) + """
                  </td>
                  <td style="padding: 30px">
                  E-mail: """ + str(email) + """
                  </td>
                  <td style="padding: 30px">
                  Date: """ + str(datetime.datetime.now()) + """ UTC
                  Адрес: """ + str(address) + """
                  </td>
                </tr>
              </table>
            </td>
          </tr>
        </table>

      </body>
    </html>
    """
    print(datetime.datetime.now())
    msg = MIMEText(html, 'html')
    msg['Subject'] = Header(subject, 'utf-8')

    # Отпавляем письмо
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(mail_sender, mail_receiver.split(","), msg.as_string())
    server.quit()
    # return render(request, 'jino/index.html')
    return redirect("/")
