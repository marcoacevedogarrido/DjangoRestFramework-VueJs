# Generated by Django 3.2.5 on 2021-08-03 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_pandas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proceso',
            name='documento',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='server.documento'),
        ),
    ]