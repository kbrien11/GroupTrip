# Generated by Django 3.2.12 on 2022-04-03 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grouptrip', '0003_rename_user_pk_message_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
    ]
