# Generated by Django 3.1.7 on 2021-03-27 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0020_auto_20210327_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='equippedWeapon',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
