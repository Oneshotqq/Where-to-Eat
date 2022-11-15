from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from .models import restaurant ,Comment



# Create your views here.
def home_Page (request: HttpRequest) :
    return render (request , "Wteapp/base.html")



def add_restaurant(request : HttpRequest):

    if request.method == "POST":
        new_restaurant = restaurant(name=request.POST["name"], city = request.POST["city"], address=request.POST["address"], cuisine = request.POST.get('cuisine',False), description =request.POST["description"] ,  work_time =request.POST["work_time"], picture=request.FILES.get('picture',False), location =request.POST["location"], menu=request.POST["menu"] , rating=request.POST["rating"])
        new_restaurant.save()

    return render(request, "Wteapp/Add_res.html", {"restaurants" : restaurant})


def list_restaurant(request: HttpRequest):
    
    
    if "search" in request.GET:
        view_restaurants = restaurant.objects.filter(title__contains=request.GET["search"])
    else:
        view_restaurants = restaurant.objects.all()

 
    return render(request, "Wteapp/Res_list.html", {"restaurants" : view_restaurants})


def delete_post(request: HttpRequest, res_id:int):

    try:
        rest = restaurant.objects.get(id=res_id)
    except:
        return render(request , "Wteapp/not_found.html")

    rest.delete()

    return redirect ("Wte_app:list_restaurant")



def restaurant_details(request : HttpRequest, res_id : int):

    try:
        restaurants = restaurant.objects.get(id=res_id)
        comments = Comment.objects.filter(post = restaurants)
    except:
        return render(request , "Wteapp/not_found.html")

    return render(request, "Wteapp/view_Res.html", {"restaurant" : restaurants , "comments" : comments})