# Generated by Django 3.1.5 on 2021-01-08 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataPasien', '0003_auto_20210107_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapasien',
            name='no_telepon',
            field=models.CharField(max_length=12),
        ),
    ]