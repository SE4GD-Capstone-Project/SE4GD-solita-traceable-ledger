# Generated by Django 5.0 on 2024-04-09 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NodeAPI', '0003_subcontractor_remove_product_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subparts',
        ),
        migrations.RemoveField(
            model_name='subpart',
            name='contractor',
        ),
        migrations.AddField(
            model_name='product',
            name='co2_per_unit',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='product',
            name='number_of_units',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='ProductSubpart',
        ),
        migrations.DeleteModel(
            name='SubContractor',
        ),
        migrations.DeleteModel(
            name='Subpart',
        ),
    ]
