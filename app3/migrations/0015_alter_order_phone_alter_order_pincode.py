# Generated by Django 4.1.5 on 2023-02-18 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0014_rename_value_order_size_alter_order_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
