from django.db import models

# Create your models here.
class services(models.Model):
    img = models.ImageField(upload_to='images/',default='')
    title=models.CharField(max_length=150)
    desc=models.TextField(max_length=500)

    def __str__(self):
        return self.title
    
    
