from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('../accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
