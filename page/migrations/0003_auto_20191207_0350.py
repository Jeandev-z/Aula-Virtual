# Generated by Django 3.0 on 2019-12-07 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]