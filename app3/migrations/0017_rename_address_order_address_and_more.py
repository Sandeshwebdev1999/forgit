# Generated by Django 4.1.5 on 2023-02-18 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0016_rename_address_order_address_remove_order_phone_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Mobile_Number',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='Pin_Code',
            new_name='pincode',
        ),
    ]
