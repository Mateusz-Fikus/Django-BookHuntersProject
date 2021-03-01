# Generated by Django 3.1.6 on 2021-02-26 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='id_buer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
    ]