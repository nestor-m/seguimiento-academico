# Generated by Django 2.0.8 on 2019-09-02 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiacursada',
            name='carrera',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cursadas', to='core.Carrera'),
            preserve_default=False,
        ),
    ]