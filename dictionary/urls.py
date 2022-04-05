from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home, name = 'home'),
    path('meaning',views.word , name = 'word'),
    path('translation', views.translation , name = 'translation'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
