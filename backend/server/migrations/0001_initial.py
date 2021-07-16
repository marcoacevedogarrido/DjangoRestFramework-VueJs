# Generated by Django 3.2.5 on 2021-07-16 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('razon_social', models.CharField(blank=True, max_length=50, null=True)),
                ('rut', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True, null=True)),
                ('fecha_envio', models.DateField(blank=True, null=True)),
                ('cliente', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='server.cliente')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('codigo', models.CharField(blank=True, max_length=50, null=True)),
                ('precio', models.FloatField(default=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField(blank=True, null=True)),
                ('cliente', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='server.cliente')),
                ('documento', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='server.documento')),
                ('producto', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='server.producto')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
