# Generated by Django 3.2.5 on 2021-08-29 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_remove_cart_discounted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='discounted',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
