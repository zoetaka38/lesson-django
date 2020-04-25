from django.db import models

# Create your models here.

class Post(models.Model):
    task = models.CharField(
        max_length=100,
        verbose_name="タスク",
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="登録日時",
        )