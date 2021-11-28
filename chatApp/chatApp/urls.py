from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as authentificationViews
# from application import views as chatViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('application.urls')),

]
