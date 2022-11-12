from django.urls import path

from . import views



app_name = 'Wte_app'


urlpatterns = [
 path ('home/',views.home_Page,name='HomePage'),
]