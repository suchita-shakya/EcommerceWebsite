# Generated by Django 3.2.8 on 2021-10-23 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=50),
        ),
    ]
