"""
URL configuration for mysite project.

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
from django.conf import settings     #this two lines gives access for uploading static files from the user for profile image
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from users import views as users_views    #from users app this view(register/)
from django.contrib.auth import views as auth_views #for login and logout functionality in users app

urlpatterns = [
    path("admin/", admin.site.urls),
    path('food/',include('food.urls')),
    path('register/',users_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),   #the both login and logout are come under class based view in-built function so we use as_view()
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',users_views.profilepage,name='profile')
]


urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

