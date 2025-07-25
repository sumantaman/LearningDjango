# Generated by Django 5.1.3 on 2025-06-11 05:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(max_length=200)),
                ('item_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.item')),
            ],
        ),
    ]
