# Generated by Django 5.0 on 2024-01-30 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='size',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('date', models.DateTimeField()),
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=100)),
                ('pzinc', models.CharField(choices=[('Not coated', 'Not coated'), ('Coated', 'Coated'), ('Silver coated', 'Silver coated')], max_length=50)),
                ('pprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('psellingprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('psize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.size')),
            ],
        ),
    ]