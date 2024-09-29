# Generated by Django 5.1.1 on 2024-09-29 02:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleproducto',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='contacto',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Administrador', 'Administrador'), ('Gerente', 'Gerente'), ('Usuario Regular', 'Usuario Regular')], default='Usuario Regular', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
