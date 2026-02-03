from django.urls import path
from . import views
urlpatterns=[
    path('home/',views.studentHome),
    path('dashboard/',views.studentDashboard),
    path('marks/',views.studentMarks),
    path('profile/',views.studentProfile),
    path('timetable/',views.studentTimetable)
]