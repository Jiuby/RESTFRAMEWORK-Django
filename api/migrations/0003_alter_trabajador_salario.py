# Generated by Django 4.2.7 on 2023-12-04 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_trabajador_salario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajador',
            name='salario',
            field=models.CharField(max_length=15),
        ),
    ]