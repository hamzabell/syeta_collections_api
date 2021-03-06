# Generated by Django 3.1.3 on 2021-07-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('percentage', models.IntegerField()),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('EXPIRED', 'Expired'), ('SUSPENDED', 'Suspended')], default='ACTIVE', max_length=10)),
                ('expiryDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_code', models.ManyToManyField(to='orders.Discount')),
            ],
        ),
    ]
