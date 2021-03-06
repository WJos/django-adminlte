# Generated by Django 3.2.11 on 2022-02-21 19:53

import apps.home.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('parasitemie', models.IntegerField()),
            ],
            options={
                'db_table': 'diagnostic',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('sexe', models.CharField(max_length=1)),
                ('age', models.CharField(max_length=20)),
                ('tel', models.IntegerField()),
            ],
            options={
                'db_table': 'patient',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.home.models.get_image_filename, verbose_name='Image')),
                ('diagnostic', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='home.diagnostic')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.AddField(
            model_name='diagnostic',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.patient'),
        ),
    ]
