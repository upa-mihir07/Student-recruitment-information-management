# Generated by Django 3.1.2 on 2020-10-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=64)),
                ('mis', models.IntegerField(primary_key=True, serialize=False)),
                ('date_of_birth', models.DateTimeField()),
            ],
        ),
    ]
