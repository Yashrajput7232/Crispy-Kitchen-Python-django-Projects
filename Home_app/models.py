from django.db import models

# Create your models here.
class  Reservations(models.Model):
    name=models.CharField(max_length=55)
    email=models.CharField( max_length=50)
    phone=models.CharField(max_length=50)
    people=models.CharField(max_length=50)
    date=models.DateField()
    time=models.CharField(default=6,max_length=5)
    message=models.TextField()

    def __str__(self) -> str:
        return self.name+"  "+self.people


