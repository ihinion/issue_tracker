# Generated by Django 2.2 on 2020-08-11 19:48

from django.db import migrations, models
import webapp.validators


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20200811_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='detailed_desc',
            field=models.TextField(blank=True, max_length=1500, null=True, validators=[webapp.validators.at_least_200, webapp.validators.restricted_text_art], verbose_name='Detailed description'),
        ),
    ]
