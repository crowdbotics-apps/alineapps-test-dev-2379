# Generated by Django 2.2.12 on 2020-04-07 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='field_test',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
