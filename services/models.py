from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=100,null=True)
    category = models.CharField(null=True)
    cost = models.IntegerField(null=True)

    class Meta:
        db_table = "services"
        
    def __str__(self):
        return self.name