# Generated by Django 3.2.24 on 2024-02-23 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='wirter',
            new_name='writer',
        ),
    ]
