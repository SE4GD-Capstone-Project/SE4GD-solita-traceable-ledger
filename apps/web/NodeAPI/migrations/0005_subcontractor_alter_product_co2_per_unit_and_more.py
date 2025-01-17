# Generated by Django 5.0 on 2024-04-09 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NodeAPI', '0004_remove_product_subparts_remove_subpart_contractor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubContractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='co2_per_unit',
            field=models.FloatField(help_text='CO2 emitted per unit'),
        ),
        migrations.AlterField(
            model_name='product',
            name='number_of_units',
            field=models.IntegerField(help_text='Number of units available'),
        ),
        migrations.CreateModel(
            name='Subpart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('co2_footprint', models.FloatField(help_text='CO2 footprint per unit')),
                ('contractor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NodeAPI.subcontractor')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubpart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_needed_per_unit', models.FloatField(help_text='Quantity of the subpart needed to make one unit of product')),
                ('units_to_buy', models.FloatField(help_text='Number of units to buy from the subcontractor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_subparts', to='NodeAPI.product')),
                ('subpart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NodeAPI.subpart')),
            ],
        ),
    ]
