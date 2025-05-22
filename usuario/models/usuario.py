from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    email = models.CharField(max_length=50)

    class Meta:
        db_table = 'usuarios'