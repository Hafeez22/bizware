# Generated by Django 5.0 on 2024-01-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=50)),
                ('cphone', models.CharField(max_length=15)),
                ('cmail', models.CharField(max_length=100)),
                ('caddress', models.CharField(max_length=200)),
                ('cbalance', models.FloatField()),
            ],
        ),
    ]
