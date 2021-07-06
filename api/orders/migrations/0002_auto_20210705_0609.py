# Generated by Django 3.1.3 on 2021-07-05 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210702_1942'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.company'),
        ),
        migrations.AddField(
            model_name='order',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.company'),
        ),
    ]
