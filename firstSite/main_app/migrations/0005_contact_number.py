# Generated by Django 4.2.7 on 2023-12-16 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
