from django.urls import path
from . import views

urlpatterns = [
    path("", views.displayMyResume, name="displayMyResume"),     
    path("<int:id>/portifolioDetails", views.portifolioDetails, name="portifolioDetails"),     
]