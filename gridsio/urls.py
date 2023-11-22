"""
URL configuration for gridsio project.

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
from gridsio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grids/', views.grid_list),
    path('grid/<int:id>', views.grid_info),
    path('add_grid/', views.add_grid),
    path('update_grid/<int:id>', views.update_grid),
    path('del_grid/<int:id>', views.del_grid),
    path('components/', views.component_list),
    path('component/<int:id>', views.component_info),
    path('add_component/', views.add_component),
    path('update_component/<int:id>', views.update_component),
    path('del_component/<int:id>', views.del_component),
]
