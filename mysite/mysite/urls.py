from django.contrib import admin
from django.urls import path, include
from tarjimon import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', views.salom, name='salom'),
    path('hello/', views.hello, name='hello'),
]
