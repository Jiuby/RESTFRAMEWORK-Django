# Generated by Django 4.2.7 on 2023-12-04 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='salario',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
