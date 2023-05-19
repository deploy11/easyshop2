from django.db import models

# Create your models here.
class Blog(models.Model):
    img = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    sana = models.DateTimeField(auto_now_add=True)
    more = models.TextField()
    kim = models.ForeignKey('auth.User',on_delete=models.CASCADE)