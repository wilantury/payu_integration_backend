# Generated by Django 3.2.6 on 2021-08-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('description', models.TextField(default='Descripcion', max_length=200)),
                ('image_url', models.CharField(default='https://images.freeimages.com/images/large-previews/5fb/wool-1-1530392.jpg', max_length=200)),
                ('price', models.IntegerField(default=1000)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
    ]