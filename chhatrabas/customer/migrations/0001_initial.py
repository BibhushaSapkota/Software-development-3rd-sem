# Generated by Django 4.0 on 2022-02-04 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('hostel_name', models.CharField(max_length=100)),
                ('start_date', models.DateField(max_length=20)),
                ('end_date', models.DateField(max_length=20)),
                ('total_paid', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'bill',
            },
        ),
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=5000)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('customer_address', models.CharField(max_length=100)),
                ('customer_email', models.CharField(max_length=200)),
                ('customer_phone', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
                ('last_login', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
