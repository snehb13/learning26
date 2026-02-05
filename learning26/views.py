from django.http import HttpResponse
from django.shortcuts import render

def test (request) :
    return HttpResponse("hello")

def aboutUs(request):
    return render(request,'aboutUs.html')

def contactUs(request):
    return render(request,'contactUs.html')

def home(request):
    return render(request,'home.html')

def movies(request):
    return render(request,'movies.html')

def news(request):
    return render(request,'news.html')

def shows(request):
    return  render(request,'shows.html')

def recipe(request):
    ingredient = ["maggie","tomato"]
    data = {
        "name":"maggie",
        "time":20,
        "ingredient":ingredient
    } 
    return render(request,"recipe.html",data)

def team(request):
    playerList= ["Asta","Finral","Charmi","Zora"]
    info = {
        "teamName":"Black Bulls",
        "captain":"Yami Sukehiro",
        "playerList":playerList,
        "trophy":9
    }
    return render(request,"team.html", info)    