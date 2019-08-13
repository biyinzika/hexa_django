# Generated by Django 2.2.3 on 2019-08-13 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('momo', '0002_auto_20190813_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('account_number', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='collectionrequest',
            old_name='collection',
            new_name='request_payment',
        ),
    ]
