from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100 , default="student name")
    uni_id = models.CharField(max_length=20 , unique=True)
    age=models.IntegerField()
    dob= models.DateField(null=False, blank=False)
    address=models.TextField(blank=True)
    salary=models.DecimalField(max_digits=10, decimal_places=2)
    photo=models.ImageField(upload_to = 'images/', default="images/icon1.jpg")

    def __str__(self):
        return self.name

