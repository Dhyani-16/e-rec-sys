# Generated by Django 3.0.6 on 2020-12-04 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mycart',
            field=models.CharField(blank=True, default='{}', max_length=5000),
        ),
    ]
