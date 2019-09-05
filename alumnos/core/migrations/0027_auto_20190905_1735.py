# Generated by Django 2.0.8 on 2019-09-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20190905_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiacursada',
            name='resultado',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='materiaenplan',
            name='tipo',
            field=models.CharField(choices=[('b', 'Basica'), ('a', 'Avanzada'), ('o', 'Optativa')], max_length=2, null=True),
        ),
    ]