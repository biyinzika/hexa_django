# Generated by Django 2.2.3 on 2019-08-19 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_auto_20190819_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listitems',
            old_name='listitems',
            new_name='list_item',
        ),
    ]
