# Generated by Django 2.1.5 on 2019-06-29 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_delete_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='bc',
            fields=[
                ('tx', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=100)),
                ('org', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
                ('_type', models.CharField(max_length=100)),
                ('income', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
    ]
