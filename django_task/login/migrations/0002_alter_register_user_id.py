# Generated by Django 5.0.1 on 2024-01-24 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
