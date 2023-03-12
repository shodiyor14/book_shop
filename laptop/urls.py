from django.urls import path

from laptop.views import HomeTemplateView

app_name = 'laptop'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),

]
