# Generated by Django 4.1.5 on 2023-06-26 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_alter_service_contactphone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='LinkdinLink',
            new_name='linkdinLink',
        ),
        migrations.AddField(
            model_name='home',
            name='telegramLink',
            field=models.TextField(blank=True, null=True),
        ),
    ]
