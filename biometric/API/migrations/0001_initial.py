# Generated by Django 3.2.4 on 2021-07-01 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('cheese', models.CharField(max_length=128)),
                ('pastry', models.CharField(max_length=128)),
                ('secret_ingredient', models.CharField(max_length=128)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.restaurant')),
            ],
        ),
    ]
