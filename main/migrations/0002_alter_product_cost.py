# Generated by Django 4.2.5 on 2023-10-08 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.FloatField(default=0, editable=False),
        ),
    ]
