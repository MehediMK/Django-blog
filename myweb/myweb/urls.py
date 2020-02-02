
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static
from django.conf import settings

import user_auth.urls as uaurl

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.base,name='base'),
    path('',include('main.urls')),
    path('blog/',include('blog.urls')),
    path('acco/',include(uaurl)),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
