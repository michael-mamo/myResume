from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from simple_history.admin import SimpleHistoryAdmin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id','firstName', 'middleName', 'lastName', 'specialization', 'linkdinLink', 'telegramLink', 'twitterLink', 'facebookLink', 'instagramLink', 'tiktokLink', 'backgroundImage', 'status')
    search_fields = ['id','firstName', 'middleName', 'lastName', 'specialization', 'linkdinLink', 'telegramLink', 'twitterLink', 'facebookLink', 'instagramLink', 'tiktokLink', 'backgroundImage', 'status']
    link_display_fields=['id']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'briefDescription', 'workTitle', 'dateofBirth', 'websiteLink', 'phone', 'address', 'highestEducation', 'email',  'freelance', 'bottomDescription', 'status', 'datetime')
    search_fields = ['id','image', 'briefDescription', 'workTitle', 'dateofBirth', 'websiteLink', 'phone', 'address', 'highestEducation', 'email',  'freelance', 'bottomDescription', 'status', 'datetime']
    link_display_fields=['id']
    

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'status', 'view_skils_link')
    search_fields = ['id','name', 'status']
    link_display_fields=['id']
    def view_skils_link(self, obj):
        count = obj.skill_set.count()
        url = (
            reverse("admin:resume_skill_changelist")
            + "?"
            + urlencode({"category__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Skills</a>', url, count)

    view_skils_link.short_description = "Skills"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','get_category_name', 'name', 'value', 'status')
    search_fields = ['id','category', 'name', 'value', 'status']
    list_filter = ('category__name', )
    link_display_fields=['id']
    def get_category_name(self, obj):
        return obj.category.name
    get_category_name.short_description = 'Category'

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','subtile', 'fromDate', 'toDate', 'calender', 'calender', 'listOfActivities', 'address', 'description', 'status')
    search_fields = ['id', 'title','subtile', 'fromDate', 'toDate', 'calender', 'calender', 'listOfActivities', 'address', 'description', 'status']
    link_display_fields=['id']

@admin.register(PortifolioCategory)
class PortifolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'status', 'view_portifolio_link')
    search_fields = ['id','name', 'status']
    link_display_fields=['id']
    def view_portifolio_link(self, obj):
        count = obj.portifolio_set.count()
        url = (
            reverse("admin:resume_portifolio_changelist")
            + "?"
            + urlencode({"category__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Portifolios</a>', url, count)

    view_portifolio_link.short_description = "Portifolio"


@admin.register(Portifolio)
class PortifolioAdmin(admin.ModelAdmin):
    list_display = ('id','get_category_name', 'title', 'subtitle', 'technologies','startDate', 'endDate', 'projectUrl', 'descriptionTitle','description', 'image', 'status', 'view_portifolio_image_link')
    search_fields = ['id','get_category_name', 'title', 'subtitle', 'technologies','startDate', 'endDate', 'projectUrl', 'descriptionTitle','description', 'image', 'status']
    list_filter = ('category__name', )
    link_display_fields=['id']
    def get_category_name(self, obj):
        return obj.category.name
    get_category_name.short_description = 'Category'
    def view_portifolio_image_link(self, obj):
        count = obj.portifolioimage_set.count()
        url = (
            reverse("admin:resume_portifolioimage_changelist")
            + "?"
            + urlencode({"portifolio__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Images</a>', url, count)

    view_portifolio_image_link.short_description = "Portifolio"

@admin.register(PortifolioImage)
class PortifolioImageAdmin(admin.ModelAdmin):
    list_display = ('id','get_portifolio_name', 'image', 'description', 'status')
    search_fields = ['id','get_portifolio_name', 'image', 'description', 'status']
    list_filter = ('portifolio__title', )
    link_display_fields=['id']
    def get_portifolio_name(self, obj):
        return obj.portifolio.title
    get_portifolio_name.short_description = 'Portifolio'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'image', 'contactPhone', 'contactLink', 'status')
    search_fields = ['id','title', 'description', 'image', 'contactPhone', 'contactLink', 'status']
    link_display_fields=['id']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','fullName', 'image', 'title', 'description', 'contactPhone', 'contactLink', 'status')
    search_fields = ['id','fullName', 'image', 'title', 'description', 'contactPhone', 'contactLink', 'status']
    link_display_fields=['id']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','location', 'email', 'contactPhone','datetime', 'status')
    search_fields = ['id','location', 'email', 'contactPhone','datetime', 'status']
    link_display_fields=['id']

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id','fullName', 'mail', 'subject', 'message', 'datetime', 'phone')
    search_fields = ['id','fullName', 'mail', 'subject', 'message', 'datetime', 'phone']
    link_display_fields=['id']

@admin.register(Footer)
class FooterbackAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'copyrightMessage', 'status', 'datetime')
    search_fields = ['id','title', 'description', 'copyrightMessage', 'status', 'datetime']
    link_display_fields=['id']
