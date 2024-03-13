from django.db import models
from config import settings
from modules.validators import validate_title


class Modules(models.Model):
    number = models.IntegerField(verbose_name='порядковый номер')
    title = models.CharField(max_length=300, verbose_name='название', validators=[validate_title])
    description = models.TextField(verbose_name='описание')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.number}, {self.title}, {self.description}'

    class Meta:
        verbose_name = 'Образовательный модуль'
        verbose_name_plural = 'Образовательные модули'
