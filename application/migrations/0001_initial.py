# Generated by Django 4.1.4 on 2023-03-29 20:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=150)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=150, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('show_price', models.FloatField()),
                ('description', models.TextField(max_length=500)),
                ('special_product', models.BooleanField(default=False, help_text='if product is special tick it or leave it unticked')),
                ('on_sale', models.BooleanField(default=False, help_text='if product is on-sale tick it or leave it unticked')),
                ('image', models.ImageField(upload_to='product')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('total', models.FloatField(default=0)),
                ('phone', models.CharField(max_length=15)),
                ('house', models.CharField(max_length=400)),
                ('location', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=400)),
                ('landmark', models.CharField(max_length=400)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Pending', max_length=20)),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
