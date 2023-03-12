from django.shortcuts import render
from laptop.models import *

from django.views.generic import TemplateView

class HomeTemplateView(TemplateView):
    template_name = 'index.html'