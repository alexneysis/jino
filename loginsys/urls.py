from django.conf.urls import url
from django.conf.urls.static import static

from loginsys import views
from startup import settings

urlpatterns = [
                  url('login', views.login),
                  url('logout', views.logout),
                  url('reg', views.registr)
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
