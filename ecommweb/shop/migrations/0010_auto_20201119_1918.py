# Generated by Django 3.1.3 on 2020-11-19 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_merge_20201111_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail',
            name='productrating',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('1', '1'), ('4', '4'), ('5', '5')], default='3', max_length=100),
        ),
        migrations.AlterField(
            model_name='rating_detail',
            name='rating',
            field=models.CharField(choices=[('2', '2'), ('3', '3'), ('1', '1'), ('4', '4'), ('5', '5')], default='3', max_length=100),
        ),
    ]
