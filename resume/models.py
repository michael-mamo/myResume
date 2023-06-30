from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from datetime import datetime 
# validation functions 
def validateBackgroundImage(image):
    minWidth = 800
    maxHeight = 800
    height = image.height 
    width = image.width
    if width < minWidth or height < maxHeight:
        raise ValidationError("Please imput higher resolution image")

class Home(models.Model):
    firstName = models.CharField(max_length=200, null=True, blank=True, help_text='My First Name of the webiste owner')
    middleName = models.CharField(max_length=200, null=True, blank=True, help_text='My Middle Name of the webiste owner')
    lastName = models.CharField(max_length=200, null=True, blank=True, help_text='Mt Last Name of the webiste owner')
    specialization = models.TextField(max_length=1000,  null=True, blank=True, help_text='My Specialization list by separating them with ,')
    linkdinLink = models.TextField(null=True, blank=True)
    telegramLink = models.TextField(null=True, blank=True)
    websiteLink = models.TextField(null=True, blank=True)
    twitterLink = models.TextField(null=True, blank=True)
    facebookLink = models.TextField(null=True, blank=True)
    instagramLink = models.TextField(null=True, blank=True)
    tiktokLink = models.TextField(null=True, blank=True)
    backgroundImage = models.ImageField(upload_to = 'backgroundImage', null=True, help_text='Background image of the home page', validators=[validateBackgroundImage])
    choice = (
        ('1', 'Active'),
        ('0', 'In Active'),
    )
    status = models.CharField(
        max_length=1,
        unique=True,
        choices=choice,
        blank=True,
        null=True,
        default='1',
        help_text='Is Active',
    )
    datetime = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.firstName}, {self.middleName}, {self.lastName}, {self.specialization}, {self.linkdinLink}, {self.telegramLink}, {self.twitterLink}, {self.instagramLink}, {self.facebookLink}, {self.tiktokLink}, {self.backgroundImage}, {self.status}, {self.datetime}"


class About(models.Model):
    image = models.ImageField(upload_to = 'myImage', null=True, help_text='my Image')
    briefDescription = models.TextField(max_length=1000, null=True, blank=True, help_text='Brief Description that appears on the top of the about page')
    workTitle = models.CharField(max_length=200, null=True, blank=True, help_text='My tytle of work that I am woring on right now')
    dateofBirth = models.DateField(null=True, blank=True, help_text='My birthdate')
    websiteLink = models.TextField(null=True, blank=True, help_text='My Website link')
    phone_message = 'Phone number must be entered in the format: 251-000000000 eg:251-906625917' 
    phone_regex = RegexValidator(
        regex=r'^(251-)\d{9}$',
        message=phone_message
    )
    phone = models.CharField(validators=[phone_regex], max_length=60,
                             null=False, unique=True, help_text='My Phone Number')
    address = models.CharField(max_length=200, null=True, blank=True, help_text='My address')
    highestEducation = models.CharField(max_length=200, null=True, blank=True, help_text='My highest education')
    email = models.EmailField(max_length=200, null=True, blank=True, help_text='My highest education')
    choice = (
        ('1', 'Available'),
        ('0', 'Not Available'),
    )
    freelance = models.CharField(
        max_length=1,
        choices=choice,
        unique=True,
        blank=True,
        null=True,
        default='0',
        help_text='Status to show if I am available for freelance or not',
    )
    bottomDescription = models.TextField(max_length=1000, null=True, blank=True, help_text='Description for the bottom of the about page')
    
    choice2 = (
        ('1', 'Active'),
        ('0', 'In Active'),
    )
    status = models.CharField(
        max_length=1,
        choices=choice2,
        blank=True,
        null=True,
        default='1',
        help_text='Status to show if this about page data is active or not',
    )
    datetime = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.image}, {self.briefDescription}, {self.workTitle}, {self.dateofBirth}, {self.websiteLink}, {self.phone}, {self.address}, {self.highestEducation}, {self.email}, {self.freelance}, {self.bottomDescription}, {self.status}, {self.datetime}"

class SkillCategory(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, help_text='Skill category name')
    choice = (
        ('1', 'Active'),
        ('0', 'In Active'),
    )
    status = models.CharField(
        max_length=1,
        choices=choice,
        blank=True,
        null=True,
        default='1',
        help_text='status to show if the skill category is active and vissible to the website or not',
    )
    def __str__(self):
        return f"{self.name}, {self.status}"

class Skill(models.Model): 
    category = models.ForeignKey('SkillCategory', on_delete=models.SET_NULL, null=True)    
    name = models.CharField(max_length=200, null=True, blank=True, help_text='The name of the skill eg: HTML, PYTHON, DJANGO, CODING')
    value= models.FloatField(blank=True, null=True, help_text='How much I know about this skill from 1-100')
    choice = (
        ('1', 'Active'),
        ('0', 'In Active'),
    )
    status = models.CharField(
        max_length=1,
        choices=choice,
        blank=True,
        null=True,
        default='1',
        help_text='Status to show if the skill is active or not',
    )
    
class Resume(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, help_text='The title of the resume')
    subtile = models.CharField(max_length=200, null=True, blank=True, help_text='My subtitle of the resume')
    fromDate = models.DateField(null=True)
    toDate = models.DateField(null=True)
    calenderChhoice = (
        ('1', 'E.C.'),
        ('2', 'G.C.'),
    )
    calender = models.CharField(
        max_length=1,
        choices=calenderChhoice,
        blank=True,
        null=True,
        default='2',
        help_text='Which callender is selected',
    )
    listOfActivities = models.TextField(max_length=1000,  null=True, blank=True, help_text='My list of activities separating with comma ,')
    address = models.TextField(max_length=1000,  null=True, blank=True, help_text='Description on the top')
    description = models.TextField(max_length=1000,  null=True, blank=True, help_text='Description on the bottom')
    choice = (
        ('1', 'Active'),
        ('0', 'In Active'),
    )
    status = models.CharField(
        max_length=1,
        choices=choice,
        blank=True,
        null=True,
        default='1',
        help_text='Is Active',
    )
    def split_activities(self):
        return self.listOfActivities.split(',')
class PortifolioCategory(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, help_text='Portifolio category name')
    choice = (
        ('1', 'Active'),
        ('0', 'In Active'),
    )
    status = models.CharField(
        max_length=1,
        choices=choice,
        blank=True,
        null=True,
        default='1',
        help_text='status to show if the portifolio categiry is active and vissible to the website or not',
    )

class Portifolio(models.Model): 
    category = models.ForeignKey('PortifolioCategory', on_delete=models.SET_NULL, null=True)    
    title = models.CharField(max_length=200, null=True, blank=True, help_text='The title of the portifolio or project')
    subtitle = models.CharField(max_length=200, null=True, blank=True, help_text='The subtitle of the portifolio or project')
    technologies = models.TextField(max_length=20000, null=True, blank=True, help_text='List the technologies used for this project separating with ,')
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    projectUrl = models.TextField(max_length=200, null=True, blank=True, help_text='The url of the project if it is hosted')
    descriptionTitle = models.CharField(max_length=200, null=True, blank=True, help_text='The title of the description of the portifolio')
    description = models.TextField(max_length=20000, null=True, blank=True, help_text='Short Description about the portifolio')
    image = models.ImageField(upload_to = 'portifolio/Cover', null=True, help_text='The cover page of the portifolio')
    choice = (
        ('1', 'Active'),
        ('0', 'In Active'),
    )
    status = models.CharField(
        max_length=1,
        choices=choice,
        blank=True,
        null=True,
        default='1',
        help_text='Status to show if the skill is active or not',
    )
    

class PortifolioImage(models.Model):    
    portifolio = models.ForeignKey('Portifolio', on_delete=models.SET_NULL, null=True)  
    image = models.ImageField(upload_to = 'portifolio', null=True, help_text='Sample image for the portifolio')
    description = models.TextField(max_length=1000, null=True, blank=True, help_text='Description abou the portifolio image')
    choice = (
        ('0', 'Hide'),
        ('1', 'Display'),
    )
    status = models.CharField(
        max_length=1,
        choices=choice,
        blank=True,
        null=True,
        default='0',
        help_text='status to tell if the portifolio image is displayed to the user or not',
    )


class Service(models.Model): 
    title = models.CharField(max_length=200, null=True, blank=True, help_text='The title of the service that I provide')
    description = models.TextField(max_length=1000, null=True, blank=True, help_text='Optional description about the menu')
    image = models.ImageField(upload_to = 'media/hotel/package', null=True, help_text='Image icon to be displayed under the category')
    phone_message = 'Phone number must be entered in the format: 251-000000000 eg:251-906625917' 
    phone_regex = RegexValidator(
        regex=r'^(251-)\d{9}$',
        message=phone_message
    )
    contactPhone = models.CharField(validators=[phone_regex], max_length=60,
                             null=False, help_text='My Phone Number')
    contactLink = models.TextField(null=True, blank=True, help_text='Link to contact')
    choice = (
        ('1', 'Active'),
        ('0', 'In Active'),
    )
    status = models.CharField(
        max_length=1,
        choices=choice,
        blank=True,
        null=True,
        default='0',
        help_text='status to tell if the service is active or not',
    )

class Team(models.Model): 
    fullName = models.CharField(max_length=200, null=True, blank=True, help_text='The full name of my team member')
    image = models.ImageField(upload_to = 'media/hotel/package', null=True, help_text='Image icon to be displayed under the category')
    title = models.CharField(max_length=200, null=True, blank=True, help_text='The title of the member')
    description = models.TextField(max_length=1000, null=True, blank=True, help_text='Optional description about the menu')
    phone_message = 'Phone number must be entered in the format: 251-000000000 eg:251-906625917' 
    phone_regex = RegexValidator(
        regex=r'^(251-)\d{9}$',
        message=phone_message
    )
    contactPhone = models.CharField(validators=[phone_regex], max_length=60,
                             null=False, unique=True, help_text='My Phone Number')
    contactLink = models.TextField(null=True, blank=True, help_text='Link to contact')
    choice = (
        ('1', 'Active'),
        ('0', 'In Active'),
    )
    status = models.CharField(
        max_length=1,
        choices=choice,
        blank=True,
        null=True,
        default='0',
        help_text='status to tell if the member is active or not',
    )

class Contact(models.Model): 
    location = models.TextField(max_length=200, null=True, blank=True, help_text='My Location')
    email = models.EmailField(max_length=1000, null=True, blank=True, help_text='Optional description about the menu')
    phone_message = 'Phone number must be entered in the format: 251-000000000 eg:251-906625917' 
    phone_regex = RegexValidator(
        regex=r'^(251-)\d{9}$',
        message=phone_message
    )
    contactPhone = models.CharField(validators=[phone_regex], max_length=60,
                             null=False, unique=True, help_text='My Phone Number')
    choice = (
        ('1', 'Active'),
        ('0', 'In Active'),
    )
    status = models.CharField(
        max_length=1,
        choices=choice,
        blank=True,
        unique=True,
        null=True,
        default='0',
        help_text='status to tell if the service is active or not',
    )
    datetime = models.DateTimeField(default=datetime.now, blank=True)
class Feedback(models.Model): 
    fullName = models.CharField(max_length=200, null=True, blank=True, help_text='The full name of the person')
    mail = models.EmailField(null=True, help_text='The email of the person who sent the feedback')
    subject = models.CharField(max_length=200, null=True, blank=True, help_text='The subject of the feedback')
    message = models.TextField(max_length=1000, null=True, blank=True, help_text='Optional description about the menu')
    datetime = models.DateTimeField(null=True, blank=True, help_text='Date time when the feedback is sent')
    phone_message = 'Phone number must be entered in the format: 251-000000000 eg:251-906625917' 
    phone_regex = RegexValidator(
        regex=r'^(251-)\d{9}$',
        message=phone_message
    )
    phone = models.CharField(validators=[phone_regex], max_length=60,
                             null=False,  help_text='The phone number of the person who sent the feedback')

class Footer(models.Model): 
    title = models.CharField(max_length=200, null=True, blank=True, help_text='The title of the footer')
    description = models.TextField(max_length=1000, null=True, blank=True, help_text='Optional description about the menu')
    copyrightMessage = models.CharField(max_length=200, null=True, blank=True, help_text='Copy right message')
    choice = (
        ('1', 'Active'),
        ('0', 'In Active'),
    )
    status = models.CharField(
        max_length=1,
        choices=choice,
        blank=True,
        unique=True,
        null=True,
        default='0',
    )
    datetime = models.DateTimeField(default=datetime.now, blank=True)