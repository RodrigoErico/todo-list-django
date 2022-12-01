from django.db import models


class Task(models.Model):
    OPTIONS_CATEGORY = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('quando tiver tempo', 'Quando tiver tempo')
    )
    OPTIONS_STATUS = (
        ('concluded', 'Concluído'),
        ('pending', 'Pendente'),
        ('suspended', 'Suspenso'),
    )

    description = models.CharField(max_length=400)
    creation = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=25, choices=OPTIONS_CATEGORY, default='important')
    status = models.CharField(
        max_length=25, choices=OPTIONS_STATUS, default='pending')
