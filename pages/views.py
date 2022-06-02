from re import template
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    '''
    Home Page View class
    '''
    template_name = 'home.html'


class AboutPageView(TemplateView):
    '''
    About Page View Class
    '''
    template_name = 'about.html'

