# Generated by Django 3.0.5 on 2020-05-22 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200517_1656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleados',
            options={'managed': False, 'permissions': (('is_surgeon', 'Is_Surgeon'), ('is_secretary', 'Is_Secretary'), ('is_doctor', 'Is_Doctor'))},
        ),
    ]
