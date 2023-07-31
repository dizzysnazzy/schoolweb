from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('downloads/', views.downloads, name='downloads'),
    path('e_learning/', views.e_learning, name='e_learning'),
    path('', views.home, name='home'),
    path('school_admin/', views.school_admin, name='school_admin'),
    path('tenders/', views.tenders, name='tenders')
]