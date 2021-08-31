# Generated by Django 3.2.6 on 2021-08-31 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.BooleanField()),
                ('phone', models.CharField(max_length=11)),
                ('pin', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'personal_information',
            },
        ),
    ]
