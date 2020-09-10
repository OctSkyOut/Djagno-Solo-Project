from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField('제목', max_length=126, null=False)
    content = models.TextField('내용', null=False)
    author = models.CharField('작성자', max_length=30, null=False)
    createDate = models.DateField('작성일', default=timezone.now)
