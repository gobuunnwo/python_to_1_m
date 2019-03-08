# django.db モジュールの　modelsクラスの活用
from django.db import models
from django.utils import timezone
# Django内システムの活用（usernameとpasswordを活用できる）
from django.contrib.auth.models import User

# Create your models here.

# Postクラスの活用
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted=models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title