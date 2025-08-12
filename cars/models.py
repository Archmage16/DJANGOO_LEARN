from django.db import models

# Create your models here.
class Spare(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='spares/', blank=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'
        ordering = ['name']


class Machine(models.Model):
    name = models.CharField(max_length = 100)
    spare = models.ManyToManyField(Spare, through='Kit', through_fields=('machine', 'spare'))

    def str(self):
        return self.name

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ['name']
    

class Kit(models.Model):
    name = models.CharField(max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='kits')
    spare = models.ForeignKey(Spare, on_delete=models.CASCADE, related_name = 'kits')
    count = models.PositiveIntegerField()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комплект'
        verbose_name_plural = 'Комплекты'
        ordering = ['name']