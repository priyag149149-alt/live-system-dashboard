from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Sessions(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE
    )

    login_time = models.DateTimeField(
        auto_now_add=True
    )

    active = models.BooleanField(default=True)