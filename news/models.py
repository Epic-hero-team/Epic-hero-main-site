from django.db import models
 
class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=100, null=True)
    img = models.ImageField(upload_to='images/', null=True)
    body = models.TextField()
    startPage = models.TextField(null=True)
 
    def __str__(self):
        return self.title