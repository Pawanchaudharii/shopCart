# Generated by Django 3.2.6 on 2021-09-03 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
        ('app', '0005_auto_20210903_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mycart',
            name='fashionproduct',
        ),
        migrations.AlterField(
            model_name='mycart',
            name='eleproduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.electronicsproduct'),
        ),
    ]
