# Generated by Django 4.2 on 2023-05-03 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_mag', '0008_rename_book_cartitem_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]