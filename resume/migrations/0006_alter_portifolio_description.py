# Generated by Django 4.1.5 on 2023-06-24 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_about_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portifolio',
            name='description',
            field=models.TextField(blank=True, help_text='Short Description about the portifolio', max_length=20000, null=True),
        ),
    ]
