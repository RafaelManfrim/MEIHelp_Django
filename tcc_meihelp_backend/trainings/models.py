from datetime import datetime

from django.db import models


class Training(models.Model):
    url = models.CharField('URL do vídeo', max_length=1028)
    title = models.CharField('Nome do vídeo', max_length=64)
    description = models.TextField('Descrição do vídeo', max_length=512, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now(), editable=False)
    updated_at = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = 'Training'
        verbose_name_plural = 'Trainings'
