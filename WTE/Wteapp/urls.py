from django.urls import path

from . import views



app_name = 'Wte_app'


urlpatterns = [
    path ('home/',views.home_Page,name='HomePage'),
    path("restaurant/add/", views.add_restaurant, name="add_restaurant"),
    path("restaurant/list/", views.list_restaurant, name="list_restaurant"),
    path("restaurant/detail/<res_id>/", views.restaurant_details, name="restaurant_details"),
    path("restaurant/delete/<res_id>/", views.delete_post, name="delete_post"),




]