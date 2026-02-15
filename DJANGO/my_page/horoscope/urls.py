

from django.urls import path, include
from . import views


urlpatterns = [
   path('leo/', views.leo),
   path('scorpio/', views.scorpio),
]