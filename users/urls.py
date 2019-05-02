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

from startup import settings
from users import views

urlpatterns = [
                  url('send', views.send_client),
                  url('chat', views.chat),
                  url('dontrecord', views.dont_record_client),
                  url('record', views.record_client),
                  url('spam', views.spam_client),
                  url('', views.pool_clients)
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
