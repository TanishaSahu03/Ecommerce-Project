# Generated by Django 5.1.6 on 2025-03-31 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_management', '0003_order_vendor'),
        ('user_management', '0003_alter_vendor_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='vendor',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendors', to='user_management.vendor'),
        ),
    ]
