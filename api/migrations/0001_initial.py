# Generated by Django 4.2.7 on 2023-12-04 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('cargo', models.CharField(max_length=50)),
                ('salario', models.IntegerField()),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]
