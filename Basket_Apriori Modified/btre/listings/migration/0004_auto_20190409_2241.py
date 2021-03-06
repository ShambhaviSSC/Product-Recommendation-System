# Generated by Django 2.2 on 2019-04-09 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20190409_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('hp', 'hp'), ('dell', 'dell'), ('apple', 'apple'), ('onepluse', 'onepluse')], max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='display_size',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='processor_spped',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_type',
            field=models.CharField(choices=[('accessories', 'accessories'), ('Electronic_product', 'Electronic_product')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Mobile', 'Mobile'), ('Laptop', 'Laptop')], max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=8),
        ),
    ]
