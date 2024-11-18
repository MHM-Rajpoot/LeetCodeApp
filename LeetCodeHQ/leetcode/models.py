from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class CodeInject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cid = models.IntegerField(unique=True, null=True)
    title = models.TextField(max_length=130, verbose_name='Title')
    cpp = models.TextField(max_length=13000, blank=True, null=True, verbose_name='C++ Code')
    py = models.TextField(max_length=13000, blank=True, null=True, verbose_name='Python Code')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.title}'
