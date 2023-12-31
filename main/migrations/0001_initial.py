# Generated by Django 4.2.2 on 2023-06-29 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='kategori adi')),
            ],
        ),
        migrations.CreateModel(
            name='IHA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marka', models.CharField(max_length=500)),
                ('model', models.CharField(max_length=500)),
                ('agirlik', models.CharField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='main.category', verbose_name='Kategori')),
            ],
        ),
    ]
