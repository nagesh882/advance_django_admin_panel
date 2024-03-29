# Generated by Django 5.0.1 on 2024-03-04 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=100)),
                ('user_phone', models.CharField(max_length=50)),
                ('user_dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('aadhar', models.CharField(max_length=20)),
                ('pan', models.CharField(max_length=20)),
                ('marital_status', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'User Details',
                'verbose_name_plural': 'User Information',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hsn_code', models.CharField(max_length=20)),
                ('manufacture_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='login.register')),
            ],
            options={
                'verbose_name': 'Product Details',
                'verbose_name_plural': 'Product Information',
            },
        ),
    ]
