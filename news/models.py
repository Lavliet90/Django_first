from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField("Date of publication")
    def __str__(self):
        return f'News:{self.title}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'Many news'
