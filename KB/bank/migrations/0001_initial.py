# Generated by Django 2.1.2 on 2019-06-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('customer_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=100)),
                ('product_num', models.CharField(max_length=100)),
                ('account_num', models.CharField(max_length=100)),
                ('screening', models.CharField(max_length=100)),
                ('int_rate', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=100)),
                ('signed_date', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]
