# Generated by Django 2.2 on 2021-11-10 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_comment_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
