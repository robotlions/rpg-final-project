# Generated by Django 3.1.7 on 2021-03-27 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobs', '0005_auto_20210326_2355'),
        ('rooms', '0009_auto_20210327_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='mobInRoom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mobs.mob'),
        ),
    ]
