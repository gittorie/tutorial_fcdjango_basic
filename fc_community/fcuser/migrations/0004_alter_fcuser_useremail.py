# Generated by Django 3.2.24 on 2024-02-23 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0003_auto_20240223_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='useremail',
            field=models.EmailField(max_length=128, verbose_name='이메일'),
        ),
    ]