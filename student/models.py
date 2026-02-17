from django.db import models

# Create your models here.
class Student(models.Model):
    studentName= models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)

    class Meta:
        db_table = "student" 
    def __str__(self):
        return self.studentName    

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "product"

class StudentProfile(models.Model):
    hobbies =(("reading","reading"),("travel","travel"),("music","music"))
    studentId = models.OneToOneField(Student,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=100,choices=hobbies)
    studentAddress = models.CharField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()
    
    class Meta:
        db_table = "studentprofile"

    def __str__(self):
        return self.studentId.studentName    


class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryName    

class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    discount = models.IntegerField(null=True)
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    
    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName    

class Member(models.Model):
    member_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = "Member"
    
    def __str__(self):
        return self.member_name
    
class MembershipProfile(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    plan_type = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = "MembershipProfile"

    def __str__(self):
        return f"{self.member.member_name} - {self.plan_type}"



class Trainer(models.Model):
    trainer_name = models.CharField(max_length=30)
    specialization = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = "Trainer"

    def __str__(self):
        return self.trainer_name



class WorkoutPlan(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=50)
    duration_weeks = models.IntegerField()

    class Meta:
        db_table = "WorkoutPlan"

    def __str__(self):
        return self.plan_name



class Session(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    workout_plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    session_date = models.DateField()
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "Session"

    def __str__(self):
        return f"{self.member.member_name} - {self.session_date}"



class Payment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField()
    payment_status = models.CharField(max_length=20)

    class Meta:
        db_table = "Payment"

    def __str__(self):
        return f"{self.member.member_name} - {self.amount}"