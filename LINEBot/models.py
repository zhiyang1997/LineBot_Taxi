from django.db import models

# 司機驗證資料庫


class Register(models.Model):

    user_id = models.CharField(max_length=20)
    driver_id = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

# Create your models here.
