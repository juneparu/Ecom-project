# Generated by Django 5.0.4 on 2024-05-28 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_wishlistmodel_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='wishlist',
            new_name='new_wishlist',
        ),
    ]
