# Generated by Django 5.1 on 2024-08-29 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_todo_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['title']},
        ),
    ]
