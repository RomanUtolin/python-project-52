# Generated by Django 4.2.1 on 2023-05-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
