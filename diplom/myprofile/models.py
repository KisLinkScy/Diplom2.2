from django.contrib.auth.models import User
from django.db import models


# Модель профайла пользователя
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatars/')
    birth_date = models.DateField(null=True, default=None)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=20)
    apartment_number = models.CharField(max_length=20)

    class Meta:
        verbose_name='Профиль'
        verbose_name_plural='Профиль'

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"
