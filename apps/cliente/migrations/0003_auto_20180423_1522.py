# Generated by Django 2.0.1 on 2018-04-23 19:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='rol',
        ),
        migrations.AlterField(
            model_name='bitacoracliente',
            name='user',
            field=models.ForeignKey(default=None, on_delete='cascade', to=settings.AUTH_USER_MODEL),
        ),
    ]
