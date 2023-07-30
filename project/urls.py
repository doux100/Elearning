"""
URL configuration for project project.

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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('supervisor/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('our-team/', include('our_team.urls', namespace='our_team')),
    path('courses/', include('courses.urls', namespace='courses')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('about/', include('about.urls', namespace='about')),
    path('users/', include('users.urls', namespace='users')),
    # (r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #                     {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'home.views.error_404'