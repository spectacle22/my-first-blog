# Generated by Django 2.0 on 2017-12-18 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('phoneNum', models.CharField(max_length=11)),
                ('reason', models.CharField(max_length=100)),
            ],
        ),
    ]
