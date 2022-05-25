from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('familia', views.familia, name='familia'),
    path('familia/crear_familiar', views.crear_familiar, name='crear_familiar'),
    path('familia/editar_familiar/<int:id>', views.editar_familiar, name='editar_familiar'),
    path('borrar_familiar/<int:id>', views.borrar_familiar, name='borrar_familiar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
