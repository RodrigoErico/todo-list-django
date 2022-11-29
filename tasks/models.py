from django.db import models


class Task(models.Model):
    OPTIONS_CATEGORY = (
        ('urgent', 'Urgente'),
        ('important', 'Importante'),
        ('when_you_have_time', 'Quando tiver tempo')
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
