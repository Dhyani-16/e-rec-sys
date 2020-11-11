# Generated by Django 3.0.6 on 2020-11-11 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('first_name2', models.CharField(blank=True, default='', max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('last_name2', models.CharField(blank=True, default='', max_length=100)),
                ('contact_no', models.BigIntegerField()),
                ('contact_no2', models.BigIntegerField(blank=True, default=11111111)),
                ('address1', models.TextField(default='', max_length=10000)),
                ('address2', models.TextField(blank=True, default='', max_length=10000)),
                ('city', models.CharField(choices=[('Ahmedabad', 'Ahmedabad'), ('Surat', 'Surat'), ('Rajkot', 'Rajkot'), ('Gandhinagar', 'Gandhinagar'), ('Bhavnagar', 'Bhavnagar')], default='Ahmedabad', max_length=50)),
                ('city2', models.CharField(blank=True, choices=[('Ahmedabad', 'Ahmedabad'), ('Surat', 'Surat'), ('Rajkot', 'Rajkot'), ('Gandhinagar', 'Gandhinagar'), ('Bhavnagar', 'Bhavnagar')], default='Ahmedabad', max_length=50)),
                ('state', models.CharField(max_length=100)),
                ('state2', models.CharField(blank=True, default='', max_length=100)),
                ('pincode', models.PositiveIntegerField()),
                ('pincode2', models.PositiveIntegerField(blank=True, default=111111)),
                ('default_address_value', models.IntegerField(default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]