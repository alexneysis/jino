from django.db import models


# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "users"

    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    phone = models.CharField(max_length=19)
    email = models.CharField(max_length=255)
