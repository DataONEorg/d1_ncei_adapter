# Generated by Django 2.2.3 on 2019-07-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='format_id',
            field=models.URLField(max_length=30, null=True),
        ),
    ]
