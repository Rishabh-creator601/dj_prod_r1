# Generated by Django 3.2.10 on 2021-12-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_product_prod_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_img',
            field=models.ImageField(blank=True, null=True, upload_to='products'),
        ),
    ]
