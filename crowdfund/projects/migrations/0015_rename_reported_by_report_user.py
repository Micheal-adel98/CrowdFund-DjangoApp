# Generated by Django 3.2.9 on 2021-12-04 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20211204_0156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='reported_by',
            new_name='user',
        ),
    ]