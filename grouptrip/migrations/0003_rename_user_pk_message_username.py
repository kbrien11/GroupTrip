# Generated by Django 3.2.12 on 2022-04-03 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grouptrip', '0002_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user_pk',
            new_name='username',
        ),
    ]
