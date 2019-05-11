"""startup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static

from jino import views
from startup import settings

urlpatterns = [
                  url('data', views.data),
                  url('homework/request', views.get),
                  url('homework/task_3_html', views.task_3_html),
                  url('homework/task_3_mat', views.task_3_mat),
                  url('homework/task_4_html', views.task_4_html),
                  url('homework/task_4_mat', views.task_4_mat),
                  url('homework/task_7', views.task_7),
                  url('homework/send_form', views.send_form),
                  url('about', views.about),
                  url('agreement', views.agreement),
                  url('', views.home)
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
