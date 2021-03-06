# Generated by Django 3.2.12 on 2022-04-03 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grouptrip', '0004_alter_message_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='group_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='plan',
            name='group_name',
            field=models.CharField(default='', max_length=40),
        ),
    ]
