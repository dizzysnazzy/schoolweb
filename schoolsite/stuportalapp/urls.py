from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('student_portal/', views.student_portal, name='student_portal'),
    #path('login/', views.login_view, name='login'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'), 
]