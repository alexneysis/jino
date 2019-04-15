import smtplib
from email.header import Header
from email.mime.text import MIMEText

from django.shortcuts import render, redirect


def home(request):
    return render(request, 'jino/index.html')


def clinic(request):
    # https://jino24.ru/clinic/?FIO=Alexey&PHONE=%2B7+%28999%29+99+-+99+-+999&MAIL=sdfjadskf%40gmail.com

    # print("FIO: " + str(request.GET["FIO"]) + ", phone: " + str(request.GET["PHONE"]) + ", mail: " + str(request.GET["MAIL"]))

    # html = """{% load static %} <!DOCTYPE html> <html prefix="og: http://ogp.me/ns#
    #       profile: http://ogp.me/ns/profile#"> <head> {# Open grapg begin#} <meta property=og:title content="Jino"/> <meta property=og:type content="website"/> <meta property=og:url content="https://jino24.ru"/> <meta property=og:site_name content="Jino"/> <meta property=og:image content="https://jino24.ru/static/jino/img/logo_w.png"/> <meta property=og:locale content="ru_RU"/> <meta property=og:description content="Платформа, соединяющая стоматологов и пациентов. Воспользуйтесь Jino для того, чтобы выбрать клинику и врача и записаться на прием в удобное для вас время"/> {# Open grapg end#} {# User settings#} {# END#} <script async src="https://www.googletagmanager.com/gtag/js?id=UA-93952064-3"></script> <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag("js",new Date());gtag("config","UA-93952064-3");</script> <script async src="https://www.googletagmanager.com/gtag/js?id=UA-93952064-2"></script> <script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag("js",new Date());gtag("config","UA-93952064-2");</script> <meta name=yandex-verification content="ab484731ce9a2f0a"/> {# Alex Panichev yandex#} <meta name=yandex-verification content="8ddcc606db60ccb4"/> {# Stanislav #} <meta name=yandex-verification content="6b137c6729fdd6d7"/> <meta name=google-site-verification content="I7Q0Q7uar8awEclHtWGrSF2yDY0z6yeG9A8fiGv2roc"/> <meta name=wmail-verification content='23d5e1463baaf9eba62216a76326937f'/> <script type=text/javascript>(function(b,j,g,h,f,d,c){b[f]=b[f]||function(){(b[f].a=b[f].a||[]).push(arguments)};b[f].l=1*new Date();d=j.createElement(g),c=j.getElementsByTagName(g)[0],d.async=1,d.src=h,c.parentNode.insertBefore(d,c)})(window,document,"script","https://mc.yandex.ru/metrika/tag.js","ym");ym(52553323,"init",{id:52553323,clickmap:true,trackLinks:true,accurateTrackBounce:true,webvisor:true});</script> <noscript> <div><img src=https://mc.yandex.ru/watch/52553323 style=position:absolute;left:-9999px alt=""/></div> </noscript> {# User settings#} {# END#} <meta name=description content="Сервис для быстрой записи к стоматологу. Лучшие клиники Перми. Вам перезвонят сразу!"/> <script type=application/ld+json>
    # {"@context": "http://schema.org","@type": "Organization","url" : "https://jino24.ru","logo" : "https://jino24.ru/static/jino/img/logo_w.png","email": "jino.platform@gmail.com","name": "Jino","telephone": "+79523338228"}
    # </script> <link rel=stylesheet href="{% static 'jino/css/materialize.min.css' %}"> <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel=stylesheet> <link rel="shortcut icon" href="{% static 'jino/img/favicon.png' %}" type=image/png> <link rel=stylesheet type=text/css href="{% static 'jino/css/style.css' %}"> <meta charset="utf-8"/> <meta name=viewport content="width=device-width, initial-scale=1"/> <title>Jino – сервис для быстрой записи к стоматологу в лучшие клиники Перми</title> </head> <body> <nav> <div class=container> <div class=row> <a href=/ class="brand-logo col s2 l2"> <img class=nLogo src="{% static 'jino/img/logo_w.png' %}"/> </a> <div class="dNav right"> <a href=#! class=subLink>Подписка</a> </div> </div> </div> </nav> <main> <section class=searchBlock> <div class=container> <div class="row center-align"> <h2 class="btnDesc col s12 m10 offset-m1"> Поздравляю, вы успели </h2> </div> <div class="row center-align"> <h5>Ваш клиент:</h5> <p>""" + str(request.GET["FIO"]) + """</p> </div> <div class="row center-align"> <p class="col s12 m6"> <span class=bold>Телефон:</span> <a href=tel:+78005555535>""" + str(request.GET["PHONE"]) + """</a> </p> <p class="col s12 m6"> <span class=bold>E-mail:</span> <a href=mailto:mail@mail.ru>""" + str(request.GET["MAIL"]) + """</a> </p> </div> <div class="row center-align reactionBtnBlock"> <div class="col s12 m4"> <a class="waves-effect waves-light btn-large teal accent-3">Записали</a> </div> <div class="col s12 m4"> <a class="waves-effect waves-light btn-large red accent-4">Не записали</a> </div> <div class="col s12 m4"> <a class="waves-effect waves-light btn-large grey">Неадекват</a> </div> </div> </div> </section> </main> <footer class=page-footer> <div class=container> <div class="row valign-wrapper"> <div class="col s12 l4"> <ul class=social> <li> <a class="grey-text text-lighten-3" href="https://www.instagram.com/jinoplatform/?hl=ru"> <img src="{% static 'jino/img/icon_5.png' %}"/> </a> </li> <li> <a class="grey-text text-lighten-3" href=https://www.facebook.com/jinoplatform> <img src="{% static 'jino/img/icon_6.png' %}"/> </a> </li> <li> <a class="grey-text text-lighten-3" href=https://vk.com/jinoplatform> <img src="{% static 'jino/img/icon_7.png' %}"/> </a> </li> </ul> </div> <div class="col s12 l2 offset-l6 right-align"> <div class="row valign-wrapper"> <a href=/ class=brand-logo> <img class="nLogo logoBottom" src="{% static 'jino/img/logo_b.png' %}"/> </a> </div> </div> </div> </div> <div class=footer-copyright> <div class=container> <p> jino.platform@gmail.com </p> <p> +79523338228 </p> © JINO24.RU 2019 </div> </div> </footer> <script src="{% static 'jino/js/materialize.min.js' %}"></script> <script src=https://code.jquery.com/jquery-3.3.1.min.js integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin=anonymous></script> <script src="{% static 'jino/js/jquery.maskedinput.min.js' %}"></script> <script>document.addEventListener("DOMContentLoaded",function(){var a=document.querySelectorAll(".collapsible");var b=M.Collapsible.init(a,{accordion:true})});</script> <script src="{% static 'jino/js/main.js' %}"></script> </body> </html>"""

    # return render(request, html)
    return render(request, 'jino/clinic_reaction.html')


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
