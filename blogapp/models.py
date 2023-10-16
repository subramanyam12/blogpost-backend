from django.db import models
from django.contrib.auth.models import User



class Blog(models.Model):
    #user=models.ForeignKey(User,on_delete=models.CASCAD)
    title=models.CharField(max_length=200)
    post=models.TextField()
    def __str__(self):
        return self.title
