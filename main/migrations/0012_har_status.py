# Generated by Django 5.0 on 2023-12-10 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_zaptrigger_instance_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='har',
            name='status',
            field=models.CharField(default=' ', max_length=250, verbose_name='Cтатус'),
        ),
    ]
