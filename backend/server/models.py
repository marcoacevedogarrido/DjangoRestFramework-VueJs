from django.db import models
from django_pandas.managers import DataFrameManager


class Pandas(models.Model):
    objects = DataFrameManager()


class Cliente(models.Model):
    nombre = models.CharField(max_length=50,null=True, blank=True)
    razon_social = models.CharField(max_length=50,null=True, blank=True)
    rut = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['id']

    def int(self):
        return int(self.id)


class Producto(models.Model):
    nombre = models.CharField(max_length=50,null=True, blank=True)
    codigo = models.CharField(max_length=50,null=True, blank=True)
    precio = models.FloatField(default=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.nombre)


class Documento(models.Model):
    cliente = models.ForeignKey('server.Cliente', on_delete=models.CASCADE, default=True)
    nombre = models.CharField(max_length=50,null=True, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True, null=True)
    fecha_envio = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.nombre)


class Proceso(models.Model):
    proceso = models.ForeignKey('auth.User', related_name='procesos', on_delete=models.CASCADE, default=True)
    cliente = models.OneToOneField('server.Cliente', on_delete=models.CASCADE, null=False, blank=True)
    documento = models.OneToOneField('server.Documento', on_delete=models.CASCADE, null=False, blank=True)
    producto = models.ForeignKey('server.Producto', on_delete=models.CASCADE, default=True)
    cantidad = models.FloatField(null=False, blank=True)

    class Meta:
        ordering = ['id']

    def __int__(self):
        return int(self.id)
