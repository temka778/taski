from django.db import models


class Task(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField('Описание')
    completed = models.BooleanField('Выполнено', default=False)

    def _str_(self):
        return self.title
