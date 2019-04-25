import smtplib
from email.header import Header
from email.mime.text import MIMEText

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'jino/index.html')


def homework(request):
    return render(request, 'homework/main.html')


@csrf_exempt
def get(request):
    print("I get request: ", request.body)
    return HttpResponse(status=200)


def data(request):
    # if this is a POST request we need to process the form data
    # if request.method == 'POST':
    print("Input to send mail")
    # mail_receiver = "sorokin.a.n.post@gmail.com,callcentr@32praktika.ru"
    mail_receiver = "sorokin.a.n.post@gmail.com"
    mail_sender = "Jino.platform@gmail.com"
    username = "Jino.platform@gmail.com"
    password = "546879Jino"
    server = smtplib.SMTP('smtp.gmail.com:587')

    # Формируем тело письма
    subject = u'Запись'
    print("FIO: , " + str(request.GET["FIO"]) + ". phone: " + str(request.GET["PHONE"]) + ", mail: " + str(
        request.GET["MAIL"]))

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
                """ + str(request.GET["FIO"]) + """
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
                  Телефон: """ + str(request.GET["PHONE"]) + """
                  </td>
                  <td style="padding: 30px">
                  E-mail: """ + str(request.GET["MAIL"]) + """
                  </td>
                </tr>
              </table>
            </td>
          </tr>
        </table>

      </body>
    </html>
    """

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
