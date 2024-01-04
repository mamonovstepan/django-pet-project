from django.db import models


class Lead(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.CharField(max_length=150, verbose_name='Адрес эл. почты')
    region = models.CharField(max_length=150, verbose_name='Область')
    city = models.CharField(max_length=100, verbose_name='Город')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    zipcode = models.CharField(max_length=10, verbose_name='Почтовый индекс')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
