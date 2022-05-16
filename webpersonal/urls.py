
from django.conf import settings
from django.contrib import admin
from django.urls import path
from core import views

# se redireccionan las plantillas url
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path('about/',views.about,name="about"),
    path('portafolio/',views.portafolio,name="portafolio"),
    path('contacto/',views.contacto,name="contacto")
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)