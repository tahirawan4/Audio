# Generated by Django 2.0 on 2018-02-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('age_estimation', '0003_learn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learn',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
