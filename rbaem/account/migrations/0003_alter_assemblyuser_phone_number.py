# Generated by Django 4.2.8 on 2023-12-17 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_assemblyuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assemblyuser',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
