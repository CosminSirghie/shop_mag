# Generated by Django 4.2 on 2023-05-03 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_mag', '0007_cart_cartitem_remove_order_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='book',
            new_name='item',
        ),
    ]