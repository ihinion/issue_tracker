# Generated by Django 2.2 on 2020-08-11 19:33

from django.db import migrations, models
import webapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20200811_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=200, validators=[webapp.validators.restricted_text_art], verbose_name='Description'),
        ),
    ]
