# Generated by Django 3.1.3 on 2021-07-02 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='permission',
            new_name='permissions',
        ),
    ]