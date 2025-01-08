# Generated by Django 5.1.3 on 2025-01-02 08:26

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
                ('C_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('C_Desc', models.CharField(blank=True, max_length=150, null=True)),
                ('C_Image', models.ImageField(blank=True, null=True, upload_to='Category Image')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PC_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('P_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('P_Quant', models.IntegerField(blank=True, null=True)),
                ('P_Price', models.IntegerField(blank=True, null=True)),
                ('P_Desc', models.CharField(blank=True, max_length=150, null=True)),
                ('P_Image', models.ImageField(blank=True, null=True, upload_to='Product Image')),
            ],
        ),
    ]
