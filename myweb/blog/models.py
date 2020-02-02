from django.db import models

# Create your models here.
class allpost(models.Model):
    img=models.ImageField(upload_to='pimage/')
    ptitle=models.CharField(max_length=150)
    post=models.TextField(max_length=1000)
    up_date=models.DateTimeField()


    def __str__(self):
        return self.ptitle
    def summery(self):
        return self.post[0:100]+'...'
