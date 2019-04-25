from django.conf.urls import url
from django.conf.urls.static import static

from loginsys import views
from startup import settings

urlpatterns = [
                  url('login', views.login),
                  url('logout', views.logout),
                  url('', views.auth_rend)
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
