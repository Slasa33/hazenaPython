# Generated by Django 3.2 on 2021-04-26 15:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HazenaIS', '0002_auto_20210426_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='klub',
            name='adresa',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klub',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klub',
            name='prezident_klubu',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]