from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from .models import restaurant ,Comment ,cafe ,User,CommentCafes
from django.db.models import Avg
from django.contrib.auth.decorators import login_required



# Create your views here.
def home_Page (request: HttpRequest) :
    return render (request , "Wteapp/base.html")



def add_restaurant(request : HttpRequest):

    if request.method == "POST":
        new_restaurant = restaurant(name=request.POST["name"], city = request.POST["city"], address=request.POST["address"], cuisine = request.POST.get('cuisine','international'), description =request.POST["description"] ,  work_time =request.POST["work_time"], picture=request.FILES.get('picture',False), location =request.POST["location"], menu=request.POST["menu"] , rating=request.POST["rating"])
        new_restaurant.save()

    return render(request, "Wteapp/Add_res.html", {"restaurants" : restaurant})


def list_restaurant(request: HttpRequest):
    
    
    if "search" in request.GET:
        view_restaurants = restaurant.objects.filter(name=request.GET["search"])
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

    average=Comment.objects.filter(post=restaurants).aggregate(Avg('rating'))
    
    return render(request, "Wteapp/view_Res.html", {"restaurant" : restaurants ,"comments" : comments ,"averages" : average })



def add_cafe(request : HttpRequest):

    if request.method == "POST":
        new_cafe = cafe(name=request.POST["name"], city = request.POST["city"], address=request.POST["address"], cuisine = request.POST.get('cuisine','international'), description =request.POST["description"] ,  work_time =request.POST["work_time"], picture=request.FILES.get('picture',False), location =request.POST["location"], menu=request.POST["menu"] , rating=request.POST["rating"])
        new_cafe.save()

    return render(request, "Wteapp/add_cafe.html", {"cafes" : cafe})

def list_cafe(request: HttpRequest):
    
    
    if "search" in request.GET:
        view_cafe = cafe.objects.filter(name=request.GET["search"])
    else:
        view_cafe = cafe.objects.all()

 
    return render(request, "Wteapp/cafe_list.html", {"cafes" : view_cafe})


def cafe_details(request : HttpRequest, cafe_id : int):

    try:
        cafes = cafe.objects.get(id=cafe_id)
        comments = CommentCafes.objects.filter(post = cafes)
    except:
        return render(request , "Wteapp/not_found.html")

    average=CommentCafes.objects.filter(post=cafes).aggregate(Avg('rating'))

    return render(request, "Wteapp/view_cafe.html", {"cafe" : cafes ,"comments" : comments , "Averages" : average})    



def add_comment(request: HttpRequest, res_id : int):


    try:
        post = restaurant.objects.get(id=res_id)
        user : User = request.user
    except:
        return render(request , "Wteapp/not_found.html")

    if not (user.is_authenticated):
        return redirect("accounts:login_user")

    if request.method == "POST":
        
        new_comment = Comment(post=post,user=user,content=request.POST["content"],rating=request.POST["rating"])
        new_comment.save()

    return redirect("Wte_app:restaurant_details", post.id)

def add_comment_cafe(request: HttpRequest, cafe_id : int):
    print("hellooooo")
    print(cafe_id)

    try:
        post = cafe.objects.get(id=cafe_id)
        user : User = request.user
    except Exception as e:
        print(e)
        return render(request , "Wteapp/not_found.html")

    if not (user.is_authenticated):
        return redirect("accounts:login_user")

    if request.method == "POST":
        
        new_comment = CommentCafes(post=post,user=user,content=request.POST["content"],rating=request.POST["rating"])
        new_comment.save()

    return redirect("Wte_app:cafe_details", post.id)   


def delete_cafe(request: HttpRequest, res_id:int):

    try:
        rest = cafe.objects.get(id=res_id)
    except:
        return render(request , "Wteapp/not_found.html")

    rest.delete()

    return redirect ("Wte_app:list_cafe")     