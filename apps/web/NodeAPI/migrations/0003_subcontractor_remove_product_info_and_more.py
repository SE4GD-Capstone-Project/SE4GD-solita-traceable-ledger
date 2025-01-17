# Generated by Django 5.0 on 2024-04-09 05:21

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NodeAPI', '0002_auto_20240305_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubContractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='info',
        ),
        migrations.RemoveField(
            model_name='product',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subpart1_hash',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subpart1_product_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subpart1_quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subpart2_hash',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subpart2_product_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subpart2_quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subpart3_hash',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subpart3_product_id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subpart3_quantity',
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Subpart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('co2_footprint', models.FloatField(help_text='CO2 footprint per unit')),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NodeAPI.subcontractor')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubpart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(help_text='Quantity of the subpart needed for one unit of product')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NodeAPI.product')),
                ('subpart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NodeAPI.subpart')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subparts',
            field=models.ManyToManyField(through='NodeAPI.ProductSubpart', to='NodeAPI.subpart'),
        ),
    ]
