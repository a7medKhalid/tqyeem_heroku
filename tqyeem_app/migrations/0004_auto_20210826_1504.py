# Generated by Django 3.2.5 on 2021-08-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tqyeem_app', '0003_alter_product_productid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='approvedseller',
            name='productId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
