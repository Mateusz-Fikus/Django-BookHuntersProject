# Generated by Django 3.1.6 on 2021-03-01 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0005_auto_20210301_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='price',
            field=models.SmallIntegerField(default=300),
            preserve_default=False,
        ),
    ]