# Generated by Django 5.0.2 on 2024-02-27 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('emailaddress', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'wanafunzi',
            },
        ),
    ]
