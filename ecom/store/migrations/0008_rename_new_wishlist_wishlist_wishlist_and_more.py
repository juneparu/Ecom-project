# Generated by Django 5.0.4 on 2024-05-28 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_wishlist_wishlist_new_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='new_wishlist',
            new_name='wishlist',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]