# Generated by Django 5.1.3 on 2025-01-02 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Total', models.IntegerField(blank=True, null=True)),
                ('Product_Image', models.ImageField(blank=True, null=True, upload_to='Cart Images')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Message', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Place', models.CharField(blank=True, max_length=150, null=True)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('State', models.CharField(blank=True, max_length=100, null=True)),
                ('Pin', models.IntegerField(blank=True, null=True)),
                ('Total_Price', models.IntegerField(blank=True, null=True)),
                ('Message', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('PassWord', models.CharField(blank=True, max_length=100, null=True)),
                ('Confirm_Password', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
