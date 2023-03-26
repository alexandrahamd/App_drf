from django.db import models
from django.conf import settings


class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="пользователь", on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True, null=True)
    content = models.CharField(max_length=250, blank=True, null=True)
    image = models.ImageField(max_length=200, blank=True, null=True)
    date_of_change = models.DateField(verbose_name="дата изменения", null=True, blank=True)
    date_of_creation = models.DateField(verbose_name="дата создания", auto_created=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
