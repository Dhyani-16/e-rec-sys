# Generated by Django 3.0.8 on 2020-11-30 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20201130_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating_detail',
            name='rating',
            field=models.CharField(choices=[('4', '4'), ('1', '1'), ('5', '5'), ('3', '3'), ('2', '2')], default='3', max_length=100),
        ),
    ]
