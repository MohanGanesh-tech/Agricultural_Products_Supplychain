# Generated by Django 3.2 on 2021-04-30 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplychainapp', '0002_rename_manufacturer_manufacture'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='manufacture',
            new_name='manufacturer',
        ),
    ]
