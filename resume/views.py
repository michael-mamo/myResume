from .models import *
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, render, redirect
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.db.models import Q
import datetime
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage, get_connection
# from django.conf import settings

def displayMyResume(request):
    messages =""
    message_types =""
    home = Home.objects.filter(status=1).last()
    about = About.objects.filter(status=1).last()
    skillCategories =SkillCategory.objects.filter(status = 1)
    skills = Skill.objects.filter(status=1)
    resumes = Resume.objects.filter(status=1)
    portifolios = Portifolio.objects.filter(status=1)
    portifolioCategories = PortifolioCategory.objects.filter(status = 1)
    services = Service.objects.filter(status = 1)
    teams = Team.objects.filter(status = 1)
    contact = Contact.objects.filter(status = 1).last()
    footer = Footer.objects.filter(status = 1).last()
    if request.method == "POST":
        feedback = Feedback();
        feedback.fullName = request.POST.get('senderName') 
        feedback.mail = request.POST.get('senderMail') 
        feedback.phone = request.POST.get('senderPhone') 
        feedback.subject = request.POST.get('subject') 
        feedback.message = request.POST.get('message') 
        feedback.datetime = datetime.datetime.now() 
        feedback.save()
        messages = "Thanks, Your feedback is sent successfully!"
        message_types = "success"
        
        return render(request, 'index.html', {'home': home, 'about': about, 'skills': skills, 'resumes': resumes, 'portifolios':portifolios, 'skillCategories': skillCategories, 'portifolioCategories': portifolioCategories,'services': services, 'teams': teams, 'contact': contact, 'footer': footer, 'messages': messages, 'message_types': message_types})

    return render(request, 'index.html', {'home': home, 'about': about, 'skills': skills, 'resumes': resumes, 'portifolios':portifolios, 'skillCategories': skillCategories, 'portifolioCategories': portifolioCategories,'services': services, 'teams': teams, 'contact': contact, 'footer': footer})

def portifolioDetails(request, id):
    portifolioDetail = Portifolio.objects.get(id=id)
    portifolioImages = PortifolioImage.objects.filter(portifolio=portifolioDetail)
    return render(request, 'portifolioDetails.html', {'portifolioDetail': portifolioDetail, 'portifolioImages': portifolioImages})

    

    
