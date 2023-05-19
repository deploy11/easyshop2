# Generated by Django 4.2.1 on 2023-05-17 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catigory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('ish_vaqti', models.CharField(max_length=30)),
                ('tel', models.CharField(max_length=300)),
                ('telegrma', models.CharField(max_length=300)),
                ('ish_kunlari', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('subject', models.CharField(max_length=500)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Snakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('more', models.TextField()),
                ('price_type', models.CharField(choices=[('so`m', 'so`m'), ('$', '$'), ('rubl', 'rubl')], default='so`m', max_length=10)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopapp.catigory')),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=156)),
                ('pthone', models.CharField(max_length=30)),
                ('how', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100)),
                ('map', models.TextField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('produck', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shopapp.snakers')),
            ],
        ),
    ]