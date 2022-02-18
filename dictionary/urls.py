from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name = 'home'),
    path('word',views.word , name = 'word'),
    path('translation', views.translation , name = 'translation')
]
