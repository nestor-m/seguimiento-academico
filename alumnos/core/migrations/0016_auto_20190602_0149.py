# Generated by Django 2.0.8 on 2019-06-02 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_plandeestudio_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscripcion',
            name='materia',
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='comision',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Comision'),
            preserve_default=False,
        ),
    ]