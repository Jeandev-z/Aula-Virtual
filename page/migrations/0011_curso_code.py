# Generated by Django 3.0 on 2019-12-19 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_remove_curso_is_teach'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='code',
            field=models.CharField(default='', max_length=10),
        ),
    ]
