from django.db import models


# Create your models here.

class Cliente(models.Model):
    pri_nome = models.CharField(max_length=30)
    seg_nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    salario = models.CharField(max_length=30)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    def __str__(self):
        return self.pri_nome + ' ' + self.seg_nome