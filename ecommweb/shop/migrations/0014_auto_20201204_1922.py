# Generated by Django 3.0.6 on 2020-12-04 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20201130_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating_detail',
            name='rating',
            field=models.CharField(choices=[('3', '3'), ('1', '1'), ('4', '4'), ('5', '5'), ('2', '2')], default='3', max_length=100),
        ),
    ]
