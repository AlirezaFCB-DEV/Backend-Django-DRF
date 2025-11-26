from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Snippet(models.Model):
    owner = models.ForeignKey(User , related_name="snippets" , on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True , default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=100 , default="python")
    style = models.CharField(max_length=100 , default="friendly")
    
    class Meta :
        ordering = ["created"]