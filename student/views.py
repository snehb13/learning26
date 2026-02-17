#<<<<<<< HEAD
#=======

#>>>>>>> 38ddcf7 (updated)
from django.shortcuts import render

# Create your views here.
def studentHome(request):
#<<<<<<< HEAD
    return render(request,"studentHome.html")
#=======
    return render(request,"student/studentHome.html")
#>>>>>>> 38ddcf7 (updated)

def studentDashboard(request):
    student = {"name":"Ray","age":21,"city":"Gandhinagar"}
    return render(request,"student/studentDashboard.html",student)   

def studentProfile(request):
    profile = {"email":"ray@gmail.com", "phone":"9876543210"}
    return render(request,"student/studentProfile.html",profile)

def studentTimetable(request):
    timetable = {
        "monday":"Maths",
        "tuesday":"Physics",
        "wednesday":"Chemistry"
    }
    return render(request,"student/studentTimetable.html",timetable)

def studentMarks(request):
    marks = {"maths":"88","chemistry":71,"physics":"90"}
#<<<<<<< HEAD
    return render(request,"student/studentMarks.html",marks)   
#=======
    return render(request,"student/studentMarks.html",marks)   
#>>>>>>> 38ddcf7 (updated)
