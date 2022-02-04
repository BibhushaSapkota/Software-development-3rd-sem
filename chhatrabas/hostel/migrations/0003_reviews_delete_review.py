# Generated by Django 4.0 on 2022-02-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('hostelname', models.CharField(max_length=200)),
                ('review', models.CharField(max_length=5000)),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
