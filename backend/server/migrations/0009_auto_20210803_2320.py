# Generated by Django 3.2.5 on 2021-08-04 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('server', '0008_remove_proceso_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proceso',
            name='proceso',
        ),
        migrations.AlterField(
            model_name='proceso',
            name='documento',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='server.documento'),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(blank=True, help_text='Clientes asociados a este usuario', null=True, on_delete=django.db.models.deletion.CASCADE, to='server.cliente', verbose_name='Cliente')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
