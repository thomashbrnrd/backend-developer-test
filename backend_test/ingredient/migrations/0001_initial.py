# Generated by Django 3.2.7 on 2021-10-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Ingredient')),
                ('category', models.CharField(choices=[('fresh', 'fresh'), ('staple', 'staple')], max_length=64)),
                ('unit', models.CharField(choices=[('g', 'g'), ('ml', 'ml'), ('tsp', 'tsp'), ('tbsp', 'tbsp')], max_length=64)),
                ('cost_per_unit', models.FloatField(blank=True, null=True, verbose_name='Cost Per Unit')),
                ('is_available', models.BooleanField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
