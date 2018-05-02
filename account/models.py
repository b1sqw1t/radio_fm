from django.db import models
from django.conf import settings



class Profile(models.Model):
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['user']
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name='Пользователь')
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    other_info = models.CharField(max_length=200,verbose_name='Дополнительная информация',blank=True,null=True)

    def __str__(self):
        return self.user.username

