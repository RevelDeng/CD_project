# Generated by Django 2.2 on 2022-02-15 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0006_auto_20220214_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
