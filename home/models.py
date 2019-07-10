from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length = 250)
    age = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to = 'pics')
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name
