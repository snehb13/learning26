from django.contrib import admin
from .models import Student,Product,StudentProfile,Category,Service,Member,MembershipProfile,Trainer,WorkoutPlan,Session,Payment 
# Register your models here.

admin.site.register(Student)
admin.site.register(Product)
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Member)
admin.site.register(MembershipProfile)
admin.site.register(Trainer)
admin.site.register(WorkoutPlan)
admin.site.register(Session)
admin.site.register(Payment)
