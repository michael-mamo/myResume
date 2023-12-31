# Generated by Django 4.1.5 on 2023-06-23 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='The title of the resume', max_length=200, null=True)),
                ('subtile', models.CharField(blank=True, help_text='My subtitle of the resume', max_length=200, null=True)),
                ('listOfActivities', models.TextField(blank=True, help_text='My list of activities separating with comma ,', max_length=1000, null=True)),
                ('briefDescription', models.TextField(blank=True, help_text='Description on the top', max_length=1000, null=True)),
                ('bottomDescription', models.TextField(blank=True, help_text='Description on the bottom', max_length=1000, null=True)),
                ('status', models.CharField(blank=True, choices=[('1', 'Active'), ('0', 'In Active')], default='1', help_text='Is Active', max_length=1, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='home',
            name='shortDescription',
        ),
        migrations.RemoveField(
            model_name='home',
            name='slogan',
        ),
    ]
