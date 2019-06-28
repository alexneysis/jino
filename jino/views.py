import base64
import datetime
import logging
import smtplib
import xml.etree.ElementTree as xml
from email.header import Header
from email.mime.text import MIMEText

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

import secret
from users.forms import FormClient
from users.models import Client, Status


def home(request):
    return render(request, 'jino/index.html')


def not_found(request):
    return render(request, 'loginsys/error.html')

@csrf_exempt
def logout(request):
    # response = render(request, 'homework/html/task_10.html', status=401)
    # response["WWW-Authenticate"] = "Basic realm=\"Jino24.ru\""
    if "HTTP_AUTHORIZATION" in request.META:
        del request.META["HTTP_AUTHORIZATION"]
    return render(request, "homework/html/task_10.html", status=401)

@csrf_exempt
def login(request):
    try:
        if "HTTP_AUTHORIZATION" in request.META:
            print("in HTTP_AUTHORIZATION")
            auth = request.META["HTTP_AUTHORIZATION"].split()
            if len(auth) == 2 and auth[0].lower() == "basic":
                auth = base64.b64decode(auth[1])
                auth = auth.decode("utf-8")
                username, password = auth.split(":")
                if username == "admin" and password == "1111":
                    args = {}
                    args["answer"] = "Вы авторизированы"
                    return render(request, 'homework/html/task_10.html', args, status=200)
        response = render(request, 'homework/html/task_10.html', status=401)
        response["WWW-Authenticate"] = "Basic realm=\"Jino24.ru\""
        return response
    except Exception as e:
        print(e)


def task_10(request):
    return render(request, 'homework/html/task_10.html')


def task_3_html(request):
    return render(request, 'homework/html/task_3.html')


def task_4_html(request):
    return render(request, 'homework/html/task_4.html')


def task_3_mat(request):
    return render(request, 'homework/materialize/task_3.html')


def task_4_mat(request):
    return render(request, 'homework/materialize/task_4.html')


def send_form(request):
    try:
        c = {}
        c.update(csrf(request))
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("Request post = " + str(request.POST))
        logging.debug("Type request post = " + str(type(request.POST)))
        logging.debug("Request post superpowers = " + str(request.POST["superpowers"]))
        logging.debug("Type request post superpowers = " + str(type(request.POST["superpowers"])))
        logging.debug("Request post selectCountry = " + str(request.POST.getlist("selectCountry")))
        logging.debug("Type request post selectCountry = " + str(type(request.POST.getlist("selectCountry"))))
        data = request.POST
        root = xml.Element("form")
        contactInf = xml.Element("contact_Information")
        aboutYou = xml.Element("about_you")
        rate_form = xml.Element("rate_form")
        root.append(contactInf)
        root.append(aboutYou)
        root.append(rate_form)

        # contact_Information
        surname = xml.SubElement(contactInf, "surname")
        surname.text = data.getlist("surname")[0]

        first_name = xml.SubElement(contactInf, "first_name")
        first_name.text = data.getlist("firstName")[0]

        patronomic = xml.SubElement(contactInf, "patronomic")
        patronomic.text = data.getlist("patronomic")[0]

        email = xml.SubElement(contactInf, "email")
        email.text = data.getlist("email")[0]

        # about you
        birthday = xml.SubElement(aboutYou, "birthday")
        birthday.text = data.getlist("birthday")[0]

        sex = xml.SubElement(aboutYou, "sex")
        sex.text = data.getlist("sex")[0]

        extremity = xml.SubElement(aboutYou, "extremity")
        extremity.text = data.getlist("member")[0]

        interesting_facts = xml.SubElement(aboutYou, "interesting_facts")
        interesting_facts.text = data.getlist("interesting_facts")[0]

        ##Superowers
        superpowerEl = xml.Element("superpowers")
        aboutYou.append(superpowerEl)

        for i in data.getlist("superpowers"):
            superpower = xml.SubElement(superpowerEl, "superpower")
            superpower.text = i

        ##Black list
        black_listEl = xml.Element("black_list")
        aboutYou.append(black_listEl)

        for i in data.getlist("selectCountry"):
            country = xml.SubElement(black_listEl, "country")
            country.text = i

        property = xml.SubElement(aboutYou, "property")
        property.text = data.getlist("property")[0]

        # Form rate
        rate = xml.SubElement(rate_form, "rate")
        rate.text = data.getlist("rate")[0]

        tree = xml.ElementTree(root)
        file_name = "form_" + str(datetime.datetime.now()) + ".xml"
        tree.write(file_name, encoding="UTF-8")
        logging.debug("This all")
    except Exception as e:
        logging.critical(str(e))
    return HttpResponse(status=200)


@csrf_exempt
def task_7(request):
    print(request)
    return render(request, 'homework/html/task_7.html')


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
    # return render(request, "jino/index.html", {"from": form})
    return redirect("/")


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
