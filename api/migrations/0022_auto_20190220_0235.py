# Generated by Django 2.1.5 on 2019-02-20 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20190219_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
