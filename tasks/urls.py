from django.urls import path
from.views import admin_page, home

urlpatterns = [
    path('', home, name='home'),
    path('adminpage/', admin_page, name='adminpage'),
]
