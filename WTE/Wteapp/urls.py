from django.urls import path

from . import views



app_name = 'Wte_app'


urlpatterns = [
    path ('home/',views.home_Page,name='HomePage'),
    path("restaurant/add/", views.add_restaurant, name="add_restaurant"),
    path("restaurant/list/", views.list_restaurant, name="list_restaurant"),
    path("restaurant/detail/<res_id>/", views.restaurant_details, name="restaurant_details"),
    path("restaurant/delete/<res_id>/", views.delete_post, name="delete_post"),
    path("cafe/delete/<res_id>/", views.delete_cafe, name="delete_cafe"),
    path("cafe/add/", views.add_cafe, name="add_cafe"),
    path("cafe/list/", views.list_cafe, name="list_cafe"),
    path("cafe/detail/<cafe_id>/", views.cafe_details, name="cafe_details"),
    path("comment/<res_id>/", views.add_comment, name="comment"),
    path("comment/cafe/<cafe_id>/", views.add_comment_cafe, name="comments"),





]