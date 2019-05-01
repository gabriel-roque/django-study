from django.db import models


# Create your models here.

class Pessoa(models.Model):
    pri_nome = models.CharField(max_length=30)
    seg_nome = models.CharField(max_length=30)
    idade = models.IntegerField()
    salario = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    def __str__(self):
        return self.pri_nome + ' ' + self.seg_nome