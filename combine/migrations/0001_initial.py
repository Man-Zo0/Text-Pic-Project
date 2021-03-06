# Generated by Django 3.2.6 on 2021-08-11 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(max_length=400)),
                ('posx', models.CharField(max_length=100)),
                ('posy', models.CharField(max_length=100)),
                ('start_size', models.CharField(max_length=100)),
                ('max_width', models.CharField(max_length=100)),
                ('font_family', models.CharField(max_length=100)),
                ('rotate', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('alpha', models.CharField(max_length=100)),
            ],
        ),
    ]
