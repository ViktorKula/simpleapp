# Generated by Django 5.0.1 on 2024-03-26 22:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0002_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simpleapp.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0, 'Price should be >= 0.0')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Quantity should be >= 0')]),
        ),
    ]