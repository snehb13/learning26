from django.shortcuts import render,HttpResponse,redirect
from .models import Services
from .forms import ServicesForm


# Create your views here.
def servicesList(request):
    #services = services.objects.all() #select * from services
    services = Services.objects.all().order_by("id").values()
    #services = services.objects.all().values_list()
    print(services)
    return render(request, 'services/servicesList.html',{"services":services})

def createServices(request):    
    Services.objects.create(name="ajay",age=23,salary=23000,post="HR",join_date="2022-01-01")
    return HttpResponse("services CREATED...")

def createServicesWithForm(request):
    print(request.method)
    if request.method == "POST":
        form = ServicesForm(request.POST)
        form.save() #it same as create
        #return HttpResponse("services CREATED...")
        return redirect("servicesList")
    else:
        #form object create --> html
        form = ServicesForm() #form object        
        return render(request,"services/createServicesForm.html",{"form":form})
    
def deleteServices(request,id):
    #delete from services where id = 1
    print("id from url = ",id)
    Services.objects.filter(id=id).delete()
    #return HttpResponse("services DELETED...")
    #services list redirecr
    return redirect("servicesList") #url --> name -->


# def filterServices(request):
#     print("filter services called...")
#     services = services.objects.filter(age__gte=25).values()
#     print("filter services = ",services)
#     #return redirect("servicesList")
#     return render(request,"services/servicesList.html",{"services":services})


#update --->
def updateServices(request,id):
    #database existing user... id -->
    services = Services.objects.get(id=id) #select * from services where id = 1
    
    if request.method == "POST":
        form = ServicesForm(request.POST,instance=services)
        form.save()
        return redirect("servicesList")
    else:
        form = ServicesForm(instance=services)    
        return render(request,"services/updateservices.html",{"form":form})

def sortServices(request,id):
    if(id==1):
        services = Services.objects.order_by("id").values()
    else:
        services = Services.objects.order_by("-id").values()
    
    return render(request,"services/servicesList.html",{"services":services})
