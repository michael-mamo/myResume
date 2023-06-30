# Generated by Django 4.1.5 on 2023-06-23 07:43

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import resume.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('briefDescription', models.TextField(blank=True, help_text='Brief Description that appears on the top of the about page', max_length=1000, null=True)),
                ('workTitle', models.CharField(blank=True, help_text='My tytle of work that I am woring on right now', max_length=200, null=True)),
                ('dateofBirth', models.DateField(blank=True, help_text='My birthdate', null=True)),
                ('websiteLink', models.TextField(blank=True, help_text='My Website link', null=True)),
                ('phone', models.CharField(help_text='My Phone Number', max_length=60, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: 251-000000000 eg:251-906625917', regex='^(251-)\\d{9}$')])),
                ('address', models.CharField(blank=True, help_text='My address', max_length=200, null=True)),
                ('highestEducation', models.CharField(blank=True, help_text='My highest education', max_length=200, null=True)),
                ('email', models.EmailField(blank=True, help_text='My highest education', max_length=200, null=True)),
                ('freelance', models.CharField(blank=True, choices=[('1', 'Available'), ('0', 'Not Available')], default='0', help_text='Status to show if I am available for freelance or not', max_length=1, null=True)),
                ('bottomDescription', models.TextField(blank=True, help_text='Description for the bottom of the about page', max_length=1000, null=True)),
                ('status', models.CharField(blank=True, choices=[('1', 'Active'), ('0', 'In Active')], default='1', help_text='Status to show if this about page data is active or not', max_length=1, null=True)),
                ('datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(blank=True, help_text='My Location', max_length=200, null=True)),
                ('email', models.EmailField(blank=True, help_text='Optional description about the menu', max_length=1000, null=True)),
                ('contactPhone', models.CharField(help_text='My Phone Number', max_length=60, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: 251-000000000 eg:251-906625917', regex='^(251-)\\d{9}$')])),
                ('status', models.CharField(blank=True, choices=[('1', 'Active'), ('0', 'In Active')], default='0', help_text='status to tell if the service is active or not', max_length=1, null=True)),
                ('datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, help_text='The full name of the person', max_length=200, null=True)),
                ('mail', models.EmailField(help_text='The email of the person who sent the feedback', max_length=254, null=True)),
                ('subject', models.CharField(blank=True, help_text='The subject of the feedback', max_length=200, null=True)),
                ('message', models.TextField(blank=True, help_text='Optional description about the menu', max_length=1000, null=True)),
                ('datetime', models.DateTimeField(blank=True, help_text='Date time when the feedback is sent', null=True)),
                ('phone', models.CharField(help_text='The phone number of the person who sent the feedback', max_length=60, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: 251-000000000 eg:251-906625917', regex='^(251-)\\d{9}$')])),
                ('status', models.CharField(blank=True, choices=[('1', 'Active'), ('0', 'In Active')], default='0', max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='The title of the footer', max_length=200, null=True)),
                ('description', models.TextField(blank=True, help_text='Optional description about the menu', max_length=1000, null=True)),
                ('copyrightMessage', models.CharField(blank=True, help_text='Copy right message', max_length=200, null=True)),
                ('status', models.CharField(blank=True, choices=[('1', 'Active'), ('0', 'In Active')], default='0', max_length=1, null=True)),
                ('datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, help_text='My First Name of the webiste owner', max_length=200, null=True)),
                ('middleName', models.CharField(blank=True, help_text='My Middle Name of the webiste owner', max_length=200, null=True)),
                ('lastName', models.CharField(blank=True, help_text='Mt Last Name of the webiste owner', max_length=200, null=True)),
                ('specialization', models.TextField(blank=True, help_text='My Specialization list by separating them with ,', max_length=1000, null=True)),
                ('LinkdinLink', models.TextField(blank=True, null=True)),
                ('websiteLink', models.TextField(blank=True, null=True)),
                ('twitterLink', models.TextField(blank=True, null=True)),
                ('facebookLink', models.TextField(blank=True, null=True)),
                ('instagramLink', models.TextField(blank=True, null=True)),
                ('tiktokLink', models.TextField(blank=True, null=True)),
                ('backgroundImage', models.ImageField(help_text='Background image of the home page', null=True, upload_to='backgroundImage', validators=[resume.models.validateBackgroundImage])),
                ('slogan', models.TextField(blank=True, help_text='Slogan representing the hotel separating with :', max_length=1000, null=True)),
                ('shortDescription', models.TextField(blank=True, help_text='Short description about the hotel', max_length=1000, null=True)),
                ('status', models.CharField(blank=True, choices=[('1', 'Active'), ('0', 'In Active')], default='1', help_text='Is Active', max_length=1, null=True)),
                ('datetime', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Portifolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(blank=True, help_text='The subtitle of the portifolio or project', max_length=200, null=True)),
                ('title', models.CharField(blank=True, help_text='The title of the portifolio or project', max_length=200, null=True)),
                ('startDate', models.DateField(null=True)),
                ('endDate', models.DateField(null=True)),
                ('projectUrl', models.TextField(blank=True, help_text='The url of the project if it is hosted', max_length=200, null=True)),
                ('descriptionTitle', models.CharField(blank=True, help_text='The title of the description of the portifolio', max_length=200, null=True)),
                ('description', models.TextField(blank=True, help_text='Short Description about the portifolio', max_length=200, null=True)),
                ('image', models.ImageField(help_text='The cover page of the portifolio', null=True, upload_to='portifolio/Cover')),
                ('status', models.CharField(blank=True, choices=[('1', 'Active'), ('0', 'In Active')], default='1', help_text='Status to show if the skill is active or not', max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PortifolioCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Portifolio category name', max_length=200, null=True)),
                ('status', models.CharField(blank=True, choices=[('1', 'Active'), ('0', 'In Active')], default='1', help_text='status to show if the portifolio categiry is active and vissible to the website or not', max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='The title of the service that I provide', max_length=200, null=True)),
                ('description', models.TextField(blank=True, help_text='Optional description about the menu', max_length=1000, null=True)),
                ('image', models.ImageField(help_text='Image icon to be displayed under the category', null=True, upload_to='media/hotel/package')),
                ('contactPhone', models.CharField(help_text='My Phone Number', max_length=60, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: 251-000000000 eg:251-906625917', regex='^(251-)\\d{9}$')])),
                ('contactLink', models.TextField(blank=True, help_text='Link to contact', null=True)),
                ('status', models.CharField(blank=True, choices=[('1', 'Active'), ('0', 'In Active')], default='0', help_text='status to tell if the service is active or not', max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Skill category name', max_length=200, null=True)),
                ('status', models.CharField(blank=True, choices=[('1', 'Active'), ('0', 'In Active')], default='1', help_text='status to show if the skill categiry is active and vissible to the website or not', max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(blank=True, help_text='The full name of my team member', max_length=200, null=True)),
                ('image', models.ImageField(help_text='Image icon to be displayed under the category', null=True, upload_to='media/hotel/package')),
                ('title', models.CharField(blank=True, help_text='The title of the member', max_length=200, null=True)),
                ('description', models.TextField(blank=True, help_text='Optional description about the menu', max_length=1000, null=True)),
                ('contactPhone', models.CharField(help_text='My Phone Number', max_length=60, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: 251-000000000 eg:251-906625917', regex='^(251-)\\d{9}$')])),
                ('contactLink', models.TextField(blank=True, help_text='Link to contact', null=True)),
                ('status', models.CharField(blank=True, choices=[('1', 'Active'), ('0', 'In Active')], default='0', help_text='status to tell if the member is active or not', max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='The name of the skill eg: HTML, PYTHON, DJANGO, CODING', max_length=200, null=True)),
                ('value', models.FloatField(blank=True, help_text='How much I know about this skill from 1-100', null=True)),
                ('status', models.CharField(blank=True, choices=[('1', 'Active'), ('0', 'In Active')], default='1', help_text='Status to show if the skill is active or not', max_length=1, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='resume.skillcategory')),
            ],
        ),
        migrations.CreateModel(
            name='PortifolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Sample image for the portifolio', null=True, upload_to='portifolio')),
                ('description', models.TextField(blank=True, help_text='Description abou the portifolio image', max_length=1000, null=True)),
                ('status', models.CharField(blank=True, choices=[('0', 'Hide'), ('1', 'Display')], default='0', help_text='status to tell if the portifolio image is displayed to the user or not', max_length=1, null=True)),
                ('portifolio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='resume.portifolio')),
            ],
        ),
        migrations.AddField(
            model_name='portifolio',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='resume.portifoliocategory'),
        ),
    ]