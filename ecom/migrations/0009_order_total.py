# Generated by Django 4.1.4 on 2022-12-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0008_alter_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
