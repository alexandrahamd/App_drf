from django.conf import settings
from django.db import models

from blog.models import Blog


# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="пользователь", on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, verbose_name="статья", on_delete=models.CASCADE)
    context = models.CharField(verbose_name="текст", max_length=250, blank=True, null=True)
    date_of_change = models.DateTimeField(verbose_name="дата изменения", null=True, blank=True)
    date_of_creation = models.DateTimeField(verbose_name="дата создания", auto_created=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.context