"""
URL configuration for erp_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from erp_app.views import KundeListView, KundeDetailView, KundeCreateView, KundeUpdateView, KundeDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
     path('kunde/', KundeListView.as_view(), name='kunde_list'),
    path('kunde/<int:pk>/', KundeDetailView.as_view(), name='kunde_detail'),
    path('kunde/create/', KundeCreateView.as_view(), name='kunde_create'),
    path('kunde/<int:pk>/edit/', KundeUpdateView.as_view(), name='kunde_edit'),
    path('kunde/<int:pk>/delete/', KundeDeleteView.as_view(), name='kunde_delete'),
]
