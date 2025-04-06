# Generated by Django 5.1.6 on 2025-03-27 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_management', '0001_initial'),
        ('user_management', '0003_alter_vendor_is_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_management.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.customer')),
            ],
        ),
    ]
