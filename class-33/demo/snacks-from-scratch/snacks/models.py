from django.contrib.auth import get_user_model
from django.db import models

class Snack(models.Model):
    name = models.CharField(max_length=200)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default="")
