# Generated by Django 3.2.6 on 2021-12-28 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0009_auto_20211228_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='items',
            field=models.ManyToManyField(related_name='categories', to='marketplace.Item'),
        ),
    ]