from . import views
from django.urls import path
urlpatterns = [
    path('servicesList/', views.servicesList,name="servicesList"),
    #path('servicesFilter/', views.servicesFilter),
    path('createServices/',views.createServices),
    path('createServicesWithForm/',views.createServicesWithForm,name="createServicesWithForm"),
    #path('createCourse/',views.createCourse),
    #path('deleteservices/',views.deleteservices,name="deleteservices")
    path("deleteServices/<int:id>",views.deleteServices,name="deleteServices"),
    #path("filterServices/",views.filterServices,name="filterServices"),
    path("updateServices/<int:id>",views.updateServices,name="updateServices"),
    path("sortServices/<int:id>",views.sortServices,name="sortServices")
]