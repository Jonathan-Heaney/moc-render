# Generated by Django 5.0.4 on 2024-04-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamousPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('occupation', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=2)),
                ('alive', models.BooleanField(blank=True, null=True)),
                ('bplace_name', models.CharField(blank=True, max_length=2000, null=True)),
                ('bplace_country', models.CharField(blank=True, max_length=255, null=True)),
                ('birthdate', models.CharField(blank=True, max_length=20, null=True)),
                ('birthyear', models.IntegerField(blank=True, null=True)),
                ('dplace_name', models.CharField(blank=True, max_length=2000, null=True)),
                ('dplace_country', models.CharField(blank=True, max_length=255, null=True)),
                ('deathdate', models.CharField(blank=True, max_length=20, null=True)),
                ('deathyear', models.IntegerField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('hpi', models.FloatField()),
            ],
        ),
    ]