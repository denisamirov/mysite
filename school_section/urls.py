"""school_section URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_1.views import project, timetable_edit, all_classes, courses, gallery, RegistrationCreateView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('administration_web_page/', admin.site.urls),
    path('', include('app_1.urls')),
    path('projects/', project, name='project'),
    path('gallery/', gallery, name='gallery'),
    path('registration/', RegistrationCreateView.as_view(), name='add'),
    path('courses/', courses, name='courses'),
    path('all_classes/', all_classes, name='all_classes'),
    path('form/<str:class_id>/', timetable_edit),
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user='app_1/shedule.html',
                                              redirect_field_name='app_1/shedule.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='app_1/shedule.html'), name='logout')
]
