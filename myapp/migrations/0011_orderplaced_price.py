# Generated by Django 3.2.5 on 2021-08-29 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_orderplaced_discounted'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]